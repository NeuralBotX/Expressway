from src.Graph.Get_Data import Get_Data
import networkx as nx
from shapely.geometry import Point
import matplotlib.pyplot as plt
import random
import geopandas as gpd


class Graph(Get_Data):
    def __init__(self, path):
        super(Graph,self).__init__(path = path, get_pos = True)


    def __private_graph_from_gdf(self, G, data):

        if isinstance(data,list):
            for index in range(len(data)):
                color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                G.add_nodes_from(data[index]['CROWID'].tolist(), pos = self.pos, color = color)

        return G


    def __len__(self):
        num = len(self.data)
        return num


    def __getitem__(self, index):
        if index > len(self.path)-1:
            raise IndexError( "迭代次数不得超过输入文件路径的最大索引")

        G = nx.Graph()
        self.__private_graph_from_gdf(G, [self.data[index]])
        node_colors = list(nx.get_node_attributes(G, 'color').values())
        nx.draw(G, node_size=0.1, pos=self.pos, node_color=node_colors)
        plt.show()
        return G


    def __call__(self, draw = False, *args, **kwargs):
        G = nx.Graph()
        self.__private_graph_from_gdf(G, self.data)

        if draw:
            node_colors = list(nx.get_node_attributes(G, 'color').values())
            nx.draw(G,node_size = 0.1, pos=self.pos, node_color = node_colors)
            plt.show()
        return G


if __name__ == "__main__":
    G = Graph(['E:/expressway project/Data/source_sichuang/Catsicgl_51_2022年报_2023022717背景/CBJZCP.shp','E:/expressway project/Data/source_sichuang/Catsicgl_51_2022年报_2023022717背景/SDP.shp'])




