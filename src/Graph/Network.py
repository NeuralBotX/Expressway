from src.Graph.Data import AboutData
import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import math
from scipy.spatial import KDTree


class AboutNetwork(AboutData):
    def __init__(self, file_path, *args, **kwargs):
        self.G_Road = None      # 仅仅构建路网相关的模型
        self.G_Point = None     # 仅仅构建点相关的模型
        self.G_Plus = None      # 用于构建制定的组合式路网

        # 继承 AboutData 父类
        super(AboutNetwork, self).__init__(file_path = file_path, get_pos = True)
        super(AboutNetwork, self).__call__(self, *args, **kwargs)


    '''
    def __getitem__(self, index):
        if index > len(self.file_path)-1:
            raise IndexError( "迭代次数不得超过输入文件路径的最大索引")

        G = nx.Graph()
        self.__private_graph_from_gdf(G, [self.data[index]])
        node_colors = list(nx.get_node_attributes(G, 'color').values())
        nx.draw(G, node_size=0.1, pos=self.node_pos, node_color=node_colors)
        plt.show()
        return G
    '''


    def __private_get_road_edges_and_nodes(self, road_data):
        """
        :return:

        % function ->
        """
        edges = []
        nodes = []
        for index, row in road_data.iterrows():
            geo_row = list(row['geometry'].coords)
            for i in range(len(geo_row)):
                # 添加 点数据
                nodes.append(self.road_pos[(geo_row[i][0],geo_row[i][1])])

                # 添加 连边数据
                if i == 0:
                    pass
                else:
                    edges.append([self.road_pos[(geo_row[i][0],geo_row[i][1])],self.road_pos[(geo_row[i-1][0],geo_row[i-1][1])]])

        return nodes,edges


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
                nodes, edges = self.__private_get_road_edges_and_nodes(self.data[idx])
                random.seed(idx + 5000)
                color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                G_Road.add_nodes_from(nodes,pos=self.road_pos_overturn, color = color)
                G_Road.add_edges_from(edges, pos=self.road_pos_overturn, edge_color = color)

        self.G_Road = G_Road  # 仅仅构建路网相关的模型
        self.G_Point = G_Point  # 仅仅构建点相关的模型


    def composite_network(self):
        """
        :return:

        % function ->
        """
        '''
        # KD 树构建步骤：
            # 1. 确定一个分割维度（通常选择方差最大的维度）
            # 2. 根据选定的分割维度 确定一个分割值（一般用中位数）
            # 3. 根据分割值的索引 划分左子树 与 右子树
            # 4. 迭代 1到3 的过程 直至树不可被划分 生成一个完整的 KD树
        # KD 树查找步骤：
            # 1. 根据分割维度 对 目标节点 进行向下遍历 直至到达叶节点
            # 2. 从叶节点逐步向上回退 并 不断更新最近邻点
            # 3. 当左侧树遇到 当前节点与目标节点的距离 与 目标节点的 分割维度 轴上的数值之和 大于等于 当前节点的分割值 则 立刻转向另一侧树进行继续回溯；右侧树与之相反
        '''

        # 使用 KD树 的算法来快速查找 每个每个节点对应最近的道路网络点
        road_positions = [self.road_pos_overturn[k] for k in self.G_Road.nodes()]
        road_KDtree = KDTree(road_positions) # 创建了 KD 树

        for i in tqdm(self.G_Point.nodes(), desc='Composite Network building', unit="ms"):
            i_JD, i_WD = self.node_pos[i]
            # 查询最近的道路节点
            _, nearest_road_index = road_KDtree.query([i_JD, i_WD], k=1) # [i_JD, i_WD] - 目标节点的经纬度 ,k 表示要返回的最近邻点的数量
            nearest_road_point_node = list(self.G_Road.nodes())[nearest_road_index]
            nearest_road_point_distance = math.sqrt((i_JD - road_positions[nearest_road_index][0]) ** 2 + (i_WD - road_positions[nearest_road_index][1]) ** 2)





    def draw_network(self):
        """
        :return:

        % function -> 用于将制定网络可视化
        """
        road_colors = list(nx.get_edge_attributes(self.G_Road, 'color').values())
        nx.draw(self.G_Road, node_size=0.1, pos=self.all_pos, node_color=road_colors)

        point_colors = list(nx.get_node_attributes(self.G_Point, 'color').values())
        nx.draw(self.G_Point, node_size=0.1, pos=self.all_pos, node_color=point_colors)

        plt.show()


    def __call__(self,  draw = True, *args, **kwargs):

        if draw:
            self.draw_network()

        self.composite_network()
        return


if __name__ == "__main__":

    G = AboutNetwork([
                       'E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/JJLJDP.shp' ,
                       'E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/CBJZCP.shp' ,
                       'E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/Road_G.shp',
                      # 'E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/Road_S.shp'
                    ])

    # G = AboutNetwork('E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/Road_G.shp')
    G(False)



