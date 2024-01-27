# -*- coding: utf-8 -*-

"""
File: Network.py
Author: Yunheng Wang
Begin Date: 2023/12/18
Description:
"""


# 引入类的头文件
from Expressway.Graph.Head import Head_Network


# 调取局内文件代码
from Expressway.Dataset.Filter_Data import ExpressData
from Expressway.Dataset.Extract_Data import Position
from Expressway.Tool.Buffer import SaveLoad


# 引入第三方库
import time
import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm


class AboutNetwork(ExpressData, Position):
    def __init__(self, file_path, Host_file_path = None, Expressway = True, *args, **kwargs):
        """
        :param file_path: 数据文件的路径，输入可以是两种形式，如下：
                          1. 字符串型 str 。这通常用于构建单个网络，离散点图 或 路网图
                          2. 列表形式 list 。这通常用于构建最终的组合式路网图

        :param Host_file_path: 宿主文件路径：用于保存最终路网结果信息 及 查看是否已存在计算过的结果 避免重复计算

        :param Expressway: 1.  True -  基础路网为 高速公路
                           2.  False - 基础路网为 全路网

        % function -> 初始化 AboutNetwork 类
        """

        self.Host_file_path = Host_file_path                                                # 宿主文件路径：用于保存最终路网结果信息 及 查看是否已存在计算过的结果 避免重复计算

        self.G_Road = None                                                                  # 构建 路网图
        self.G_Point = None                                                                 # 构建 离散点图
        self.G_Simplify = None                                                              # 构建 简化式路网图
        self.G_Plus = None                                                                  # 构建 制定的组合式路网图

        self.mapping_relation_table = None                                                  # point 与 最近的 路网点 的映射表 - {point: road_node, ... }
        self.mapping_relation_table_overturn = None                                         # point 与 最近的 路网点 的映射表 - {road_node: point, ... }

        self.G_Simplify_pos = None                                                          # 简化式路网的位置信息 (被映射之后的) {point:(经度，纬度), ...}
        self.G_Plus_pos = None                                                              # 组合式路网的位置信息 (被映射之后的) {point:(经度，纬度), ...}

        # 继承 AboutData 父类
        super(AboutNetwork, self).__init__(file_path = file_path)                           # 继承 ExpressData, Position 父类 的 __init__ 函数 , 且需要加载位置信息

        # 判断 是否 仅仅要高速公路路网
        if Expressway:
            # 基本思路：
            #           1. 高速公路（True） - 将基类中的全路网数据（self.data）用过滤的高速公路数据（self.Express_Data）覆盖
            #           2. 全路网数据（False） - 全路网数据（self.data）不变，跳过该步骤
            self.data = self.Express_Data  # 将基类中的全数据 用 过滤好的高速公路数据覆盖掉


    def __build__(self, *args, **kwargs):
        """

        % function -> 该函数用于构建 两个基础的路网 ： 1. 离散点图 ； 2. 路网图
        """

        G_Road = nx.Graph()                             # 仅仅构建路网相关的模型
        G_Point = nx.Graph()                            # 仅仅构建点相关的模型

        for idx in tqdm(range(self.number), desc='Load foundation network', unit="file"):

            # 加载 离散点图
            if self.data_type[idx] == 'Point':
                random.seed(idx)
                color = "#{:06x}".format(random.randint(0, 0xAAAAAA))
                G_Point.add_nodes_from(list(self.data[idx]['CROWID']), pos=self.node_pos, color = color)

            # 加载 路网图
            elif self.data_type[idx] == 'LineString':
                nodes, edges = Head_Network.generate_nodes_and_edges(self.data[idx], self.road_pos)
                G_Road = Head_Network.build_network(G_Road, idx + 5000, nodes, edges, self.road_pos_overturn)

        # 删除自连边
        G_Road.remove_edges_from(nx.selfloop_edges(G_Road))
        self.G_Road = G_Road                            # 将路网图保存至成员变量
        # 删除自连边
        G_Point.remove_edges_from(nx.selfloop_edges(G_Point))
        self.G_Point = G_Point                          # 将离散点图保存至成员变量


    def __private_building_simplify_network(self):
        """

        % function -> 构建简化路网图

        % authority -> 不可被外部调用
        """

        # 找到构建简化路网的节点
        road_node_join = list(self.mapping_relation_table.values())                                                     # 相对应的点
        road_node_degree_greater_2, road_node_degree_equal_1 = Head_Network.find_node_degree_e1_b2(self.G_Road)         # 路网上度大于2 ，度等于1 的节点
        simplify_road_nodes = set(road_node_degree_greater_2 + road_node_degree_equal_1 + road_node_join)               # 简化路网的节点集合 度大于2, 度等于1 , 相对应的点

        G_Simplify = nx.Graph()
        G_Simplify_Road = nx.Graph()                                                                                    # 构建简化路网 G_Simplify_Road
        simplify_road_edges = []                                                                                        # 构建简化路网 连边关系列表
        simplify_road_pos = {}                                                                                          # 构建简化路网 位置信息

        for idx in range(self.number):
            if self.data_type[idx] == 'LineString':
                for index, row in tqdm(list(self.data[idx].iterrows()), desc='Simplify network building', unit=" node"):
                    """
                    注意：在构建路网图的基础数据中存在两种数据类型格式，分别为：MultiLineString(线段)，LineString(直线)
                    思路：基本思路是将 MultiLineString 转化为 LineString 也就是说线段 到 直线的转化
                    """

                    # geometry 上可能存在空值
                    if row['geometry'] is not None:

                        # MultiLineString 类型的处理方式
                        if row['geometry'].geom_type == 'MultiLineString':
                            geo_row = []
                            geoms = list(row['geometry'].geoms)
                            for geo in geoms:
                                for lin in list(geo.coords):
                                    geo_row.append(lin)

                        # LineString 类型的处理方式
                        elif row['geometry'].geom_type == 'LineString':
                            geo_row = list(row['geometry'].coords)

                        num = len(geo_row)
                        mid_node_list = [self.road_pos[(geo_row[i][0], geo_row[i][1])] for i in range(num) if
                                         (i == 0) or (i == num - 1) or (
                                                 self.road_pos[(geo_row[i][0], geo_row[i][1])] in simplify_road_nodes)]
                        for i in range(0, len(mid_node_list)):
                            if i > 0:
                                simplify_road_edges.append([mid_node_list[i], mid_node_list[i - 1]])
                            simplify_road_nodes.add(mid_node_list[i])
                            simplify_road_pos[mid_node_list[i]] = self.road_pos_overturn[mid_node_list[i]]

        self.G_Simplify_pos = simplify_road_pos
        G_Simplify = Head_Network.build_network(G_Simplify_Road, 9999, simplify_road_nodes, simplify_road_edges, self.G_Simplify_pos)
        G_Simplify.remove_edges_from(nx.selfloop_edges(G_Simplify))
        self.G_Simplify = G_Simplify



    def __private_building_composite_network(self):
        """

        % function -> 构建组合式路网图
        """

        # 找到构建简化路网的节点
        road_node_join = list(self.mapping_relation_table.values())                                                     # 相对应的点

        # %%找全局的最短路径时较为费时
        a = time.time()
        print("\033[91m计算简化路网的全局最短路径中，请耐心等待...\033[0m")
        all_shortest_paths = dict(nx.all_pairs_shortest_path(self.G_Simplify))
        print("\033[91m简化网络的全局最短路径已计算完成，用时：{}\033[0m".format(time.time()-a))

        G_Plus = nx.Graph()                                                                                             # 构建 组合网络
        G_composite_edges_weights = []                                                                                  # 构建组合式路网图 的连边关系及权重
        G_composite_nodes = []                                                                                          # 构建组合式路网图 的节点
        G_composite_pos = {}                                                                                            # 构建组合式路网图 的位置信息
        road_node_join_set = set(road_node_join)                                                                        # point 对应的路网点 进行集合化
        display_num  = len(road_node_join)

        for source in tqdm(road_node_join, desc='Composite network building', unit='node', total=display_num):
            source_paths = all_shortest_paths[source]
            source_neighbors = set(source_paths.keys())

            for target in (source_neighbors & road_node_join_set - {source}):
                path = source_paths[target]
                miden = []

                for v in path:
                    if v in road_node_join_set:
                        miden.append(v)

                for r in range(0, len(miden)):
                    point = self.mapping_relation_table_overturn[miden[r]]
                    prior_point = self.mapping_relation_table_overturn[miden[r - 1]]
                    distance = Head_Network.count_distance(all_shortest_paths[miden[r - 1]][miden[r]], self.road_pos_overturn)
                    if r > 0 :
                        G_composite_edges_weights.append([point, prior_point, distance])
                    G_composite_nodes.append(point)
                    G_composite_pos[point] = self.road_pos_overturn[miden[r]]

        self.G_Plus_pos = G_composite_pos
        self.G_Plus = Head_Network.build_network(G_Plus, 1000, G_composite_nodes, G_composite_edges_weights, self.G_Plus_pos, weight=True)


    def draw_network(self, G, pos):
        """
        :param G: 图

        :param pos: 图的位置信息

        % function -> 将图画出来
        """
        point_colors = list(nx.get_node_attributes(G, 'color').values())
        nx.draw(G, node_size = 0.1, pos=pos, node_color=point_colors)
        plt.show()


    def __call__(self, combined_network = True, draw = True, save = True, *args, **kwargs):
        """
        :param combined_network: 是否构建组合式路网
                                 1. True - 构建组合式路网。这个操作将会消耗巨大的时间
                                 2. False - 不组合式路网v。这个操作仅仅会输出两个基础图：路网图及点图

        :param draw: 是否将简化式路网及组合式路网图画出来

        :param save: 是否将 四个路网结果保存到宿主文件中

        :return:    返回四个networkx图

        % function -> 用户根据形参 来选取输出的网络 及 可视化
        """

        # 继承父类 AboutData 的 __call__ 的成员函数
        # 主要目的: 为在 执行__call__之前先执行__build__
        super(AboutNetwork, self).__call__(self, *args, **kwargs)                           # 继承 ExpressData, Position 父类 的 __call__ 函数 ， 为了达到 在执行 __call__ 函数前 ， 先执行 __build__ 的目的

        # 判断 是否符合条件
        if save == True and self.Host_file_path == None:
            raise ValueError("若要保存构建的网络，请设置宿主路径（Host_file_path参数）")

        # 画 离散点图 及 网图
        self.draw_network(self.G_Point,self.node_pos)
        self.draw_network(self.G_Road, self.road_pos_overturn)

        # 构建组合式路网
        if combined_network:
            self.mapping_relation_table, self.mapping_relation_table_overturn = Head_Network.mapping(self.G_Road, self.G_Point, self.road_pos_overturn, self.node_pos)      # 获取 点 与 路网 的映射关系
            self.__private_building_simplify_network()                    # 构建简化路网

            # 画出简化路网
            if draw:
                self.draw_network(self.G_Simplify, self.road_pos_overturn)

            self.__private_building_composite_network()                   # 构造组合式路网

            # 画出组合式路网
            if draw:
                self.draw_network(self.G_Plus, self.G_Plus_pos)

        # 保存图到宿主路径
        if save:
            # 保存离散点图
            save_name = 'Point_' + '_'.join(sorted(self.file_name))  # 固定命名格式 这样能保证 两次相同的输入 每次输入即使文件路径的顺序不同 也可以保存成同样的文件
            class_SaveLoad = SaveLoad()
            class_SaveLoad.save_networkx(self.G_Point, self.Host_file_path, save_name, self.node_pos)

            # 保存路网图
            save_name = 'Road_' + '_'.join(sorted(self.file_name))  # 固定命名格式 这样能保证 两次相同的输入 每次输入即使文件路径的顺序不同 也可以保存成同样的文件
            class_SaveLoad = SaveLoad()
            class_SaveLoad.save_networkx(self.G_Road, self.Host_file_path, save_name, self.road_pos_overturn)

            # 保存简化路网
            save_name = 'Simplify_road_' + '_'.join(sorted(self.file_name))  # 固定命名格式 这样能保证 两次相同的输入 每次输入即使文件路径的顺序不同 也可以保存成同样的文件
            class_SaveLoad = SaveLoad()
            class_SaveLoad.save_networkx(self.G_Simplify, self.Host_file_path, save_name, self.G_Simplify_pos)

            # 保存组合式路网
            save_name = 'Composite_' + '_'.join(
                sorted(self.file_name))  # 固定命名格式 这样能保证 两次相同的输入 每次输入即使文件路径的顺序不同 也可以保存成同样的文件
            class_SaveLoad = SaveLoad()
            class_SaveLoad.save_networkx(self.G_Plus, self.Host_file_path, save_name, self.G_Plus_pos)

        return self.G_Point,self.G_Road,self.G_Simplify,self.G_Plus


if __name__ == "__main__":
    pass