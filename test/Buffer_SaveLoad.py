from Expressway.Tool.Buffer import SaveLoad
from Expressway.Graph.Network import AboutNetwork
import networkx as nx
import matplotlib.pyplot as plt

'''
path_road = 'E:/expressway project/Data/.chongqing/Graph/road/deal/'
path_point = 'E:/expressway project/Data/.chongqing/Graph/place/'
Host_file_path = 'E:/expressway project/Data/Host file/'
build_road_networkx = AboutNetwork( file_path = [path_road + '22GIS.shp', path_point + 'SFZP.shp'], Host_file_path = Host_file_path, Expressway = True)
'''
import networkx as nx
import matplotlib.pyplot as plt

# 假设 G 和 pos 是从 SaveLoad().load_networkx() 中获取的

G, pos = SaveLoad().load_networkx('E:/DataSet/Expressway DataSet/.Host file/', 'Road_22GIS_GANTRY_SFZP')


nx.draw(G, node_size=0.1, pos=pos, node_color='black', edge_color='black', alpha=0.5, with_labels=False)

# 显示图形
plt.show()

