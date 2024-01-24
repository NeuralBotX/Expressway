from Expressway.Tool.Buffer import SaveLoad
from Expressway.Graph.Network import AboutNetwork
import networkx as nx
import matplotlib.pyplot as plt


path_road = 'E:/expressway project/Data/.chongqing/Graph/road/deal/'
path_point = 'E:/expressway project/Data/.chongqing/Graph/place/'
Host_file_path = 'E:/expressway project/Data/Host file/'
build_road_networkx = AboutNetwork( file_path = [path_road + '22GIS.shp', path_point + 'SFZP.shp'], Host_file_path = Host_file_path, Expressway = True)

import networkx as nx
import matplotlib.pyplot as plt

# 假设 G 和 pos 是从 SaveLoad().load_networkx() 中获取的

G, pos = SaveLoad().load_networkx('E:/expressway project/Data/Host file/', 'Simplify_road_22GIS_SFZP')

G.remove_edges_from(nx.selfloop_edges(G))

# 画出图像，设置 edgecolors 为 'none' 去掉节点的边框
nx.draw_networkx_nodes(G, pos, node_size=10)

nx.draw_networkx_edges(G,pos, edge_color='black', alpha=0.5)

plt.show()

