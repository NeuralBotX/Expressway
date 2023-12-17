from src.Graph.Data import AboutData
import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm

class AboutNetwork(AboutData):
    def __init__(self, file_path, *args, **kwargs):
        self.G = None

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
        GG = nx.Graph()

        for idx in tqdm(range(self.number), desc='Load foundation network', unit="file"):
            if self.data_type[idx] == 'Point':
                random.seed(idx)
                color = "#{:06x}".format(random.randint(0, 0xAAAAAA))
                GG.add_nodes_from(list(self.data[idx]['CROWID']), pos=self.node_pos, color = color)

            elif self.data_type[idx] == 'LineString':
                nodes, edges = self.__private_get_road_edges_and_nodes(self.data[idx])
                random.seed(idx + 5000)
                color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                GG.add_nodes_from(nodes,pos=self.road_pos_overturn, color = color)
                GG.add_edges_from(edges, pos=self.road_pos_overturn, edge_color = color)

        self.G = GG


    def __call__(self, draw = False, *args, **kwargs):

        if draw:
            node_colors = list(nx.get_node_attributes(self.G, 'color').values())
            edge_colors = list(nx.get_edge_attributes(self.G, 'edge_color').values())

            nx.draw(self.G, node_size=0.1, pos=self.all_pos, node_color=node_colors)
            plt.show()

        return self.G


if __name__ == "__main__":

    G = AboutNetwork(['E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/JJLJDP.shp' ,'E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/CBJZCP.shp' ,'E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/Road_G.shp'])
    # G = AboutNetwork('E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/Road_G.shp')
    G(True)



