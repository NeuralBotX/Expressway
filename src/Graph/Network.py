# 引入类的头文件
import head_Network

import time
from src.Graph.Data import AboutData
import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm


class AboutNetwork(AboutData):
    def __init__(self, file_path, *args, **kwargs):

        self.G_Road = None          # 仅仅构建路网相关的模型
        self.G_Point = None         # 仅仅构建点相关的模型
        self.G_Plus = None          # 用于构建制定的组合式路网
        self.G_Simplify = None

        self.mapping_relation_table = None # point 与 最近的 路网点 的映射表 - {point: road_node, ... }
        self.mapping_relation_table_overturn = None  # point 与 最近的 路网点 的映射表 - {road_node: point, ... }

        self.G_Plus_pos = None # 用于保存 组合式路网 的位置信息 (被映射之后的) {point:(经度，纬度), ...}

        # 继承 AboutData 父类
        super(AboutNetwork, self).__init__(file_path = file_path, get_pos = True)
        super(AboutNetwork, self).__call__(self, *args, **kwargs)


    def __build__(self, *args, **kwargs):
        """
        :return:

        % function ->
        """
        G_Road = nx.Graph() # 仅仅构建路网相关的模型
        G_Point = nx.Graph() # 仅仅构建点相关的模型

        for idx in tqdm(range(self.number), desc='Load foundation network', unit="file"):
            if self.data_type[idx] == 'Point':
                random.seed(idx)
                color = "#{:06x}".format(random.randint(0, 0xAAAAAA))
                G_Point.add_nodes_from(list(self.data[idx]['CROWID']), pos=self.node_pos, color = color)

            elif self.data_type[idx] == 'LineString':
                nodes, edges = head_Network.generate_nodes_and_edges(self.data[idx],self.road_pos)

                self.G_Simplify = head_Network.build_network(G_Road, idx + 5000, nodes, edges, self.road_pos_overturn)

        self.G_Road = G_Road  # 仅仅构建路网相关的模型
        self.G_Point = G_Point  # 仅仅构建点相关的模型


    def __building_simplify_network(self):
        """
        :return:

        % function ->
        """
        road_node_join = list(self.mapping_relation_table.values())

        # 找到路网上度大于2 和 度等于1 的节点
        road_node_degree_greater_2, road_node_degree_equal_1 = head_Network.find_node_degree_e1_b2(self.G_Road)

        # 简化路网的节点集合 度大于2, 度等于1 , 相对应的点
        simplify_road_nodes = set(road_node_degree_greater_2 + road_node_degree_equal_1 + road_node_join)

        # 构建简化路网 G_Simplify_Road
        G_Simplify_Road = nx.Graph()

        simplify_road_edges = []
        for idx in range(self.number):
            if self.data_type[idx] == 'LineString':
                for index, row in tqdm(list(self.data[idx].iterrows()), desc='Simplify network building', unit=" node"):
                    # 在路网中 存在两中 数据类型的格数 MultiLineString(线段) 与 LineString(直线)
                    # 我们的基本思路是将 MultiLineString 转化为 LineString 也就是说线段 到 直线的转化

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

        self.G_Simplify = head_Network.build_network(G_Simplify_Road,9999,simplify_road_nodes,simplify_road_edges,self.road_pos_overturn)


    def __composite_network(self):
        """
        :return:

        % function ->
        """

        road_node_join = list(self.mapping_relation_table.values())

        # 根据 简化路网 G_Simplify_Road 找到 特殊节点的连边关系 从而 进行组合式路网的构建
        G_composite_edges = []
        G_composite_nodes = []
        G_composite_pos = {}
        road_node_join_set = set(road_node_join) # point 对应的路网点 进行集合化

        a = time.time()
        print("\033[91m计算简化路网的全局最短路径中，请耐心等待...\033[0m")
        # %%找全局的最短路径时较为费时
        all_shortest_paths = dict(nx.all_pairs_shortest_path(self.G_Simplify))
        print("\033[91m简化网络的全局最短路径已计算完成，用时：{}\033[0m".format(time.time()-a))

        display_num  = len(road_node_join)
        for source in tqdm(road_node_join, desc='Composite network building', unit='node', total=display_num):
            source_paths = all_shortest_paths[source]
            source_neighbors = set(source_paths.keys())
            for target in (source_neighbors & road_node_join_set - {source}):
                path = source_paths[target]
                miden = [v for v in path if v in road_node_join_set]
                for r in range(0, len(miden)):
                    point = self.road_pos_overturn[miden[r]]
                    if r > 0 :
                        G_composite_edges.append([point, self.road_pos_overturn[miden[r - 1]]])
                    G_composite_nodes.append(point)
                    G_composite_pos[point] = self.road_pos_overturn[miden[r]]

        self.G_Plus_pos = G_composite_pos
        # 创建 组合网络
        G_Plus = nx.Graph()
        self.G_Plus = head_Network.build_network(G_Plus, 1000, G_composite_nodes, G_composite_edges, self.G_Plus_pos)


    def draw_network(self, G, pos):
        """
        :param G:

        :param pos:

        :return:

        % function ->
        """
        point_colors = list(nx.get_node_attributes(G, 'color').values())
        nx.draw(G, node_size=0.1, pos=pos, node_color=point_colors)
        plt.show()


    def __call__(self, combined_network = True, draw_point = False, draw_road = False, draw_simplify_road = False, draw_composite_road = False, *args, **kwargs):

        if draw_point:
            self.draw_network(self.G_Point,self.node_pos)

        if draw_road:
            self.draw_network(self.G_Road, self.road_pos_overturn)

        if combined_network:
            # 获取 点 与 路网 的映射关系
            self.mapping_relation_table, self.mapping_relation_table_overturn = head_Network.mapping(self.G_Road, self.G_Point, self.road_pos_overturn, self.node_pos)

            # 构建简化路网
            self.__building_simplify_network()
            if draw_simplify_road:
                self.draw_network(self.G_Simplify, self.road_pos_overturn)

            # 构造组合式路网
            self.__composite_network()
            if draw_composite_road:
                self.draw_network(self.G_Plus, self.G_Plus_pos)

            # combined_network = True  获取 输入的节点网络 与 道路网络 与 道路简化网络 与 组合网络
            return self.G_Point,self.G_Road,self.G_Simplify,self.G_Plus

        # combined_network = Flase 仅仅获取 输入的节点网络 与 道路网络
        return self.G_Point, self.G_Road



if __name__ == "__main__":
    a = time.time()
    G = AboutNetwork([
        'E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/JTLJDP.shp',
        'E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/Road_G.shp',
    ])

    G_Point,G_Road,G_Simplify,G_Plus = G(combined_network = True, draw_point = True, draw_road = True, draw_simplify_road = True, draw_composite_road = True)

    print("总计用时：{}".format(time.time()-a))


