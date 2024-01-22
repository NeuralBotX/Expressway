from Expressway.Tool.Buffer import SaveLoad
import networkx as nx
import matplotlib.pyplot as plt

class_SaveLoad = SaveLoad()
G , pos = class_SaveLoad.load_networkx('E:/expressway project/Data/Host file/', 'Composite_JTLJDP_Road_G')

point_colors = list(nx.get_node_attributes(G, 'color').values())
nx.draw(G, node_size=0.1, pos=pos, node_color=point_colors)
plt.show()