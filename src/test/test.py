import networkx as nx
import random
import matplotlib.pyplot as plt
from src.Tool.Buffer import SaveLoad

G = nx.Graph()
random.seed(100)
color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
pos = {'1':(10,10.1111111),'2':(10,11),'5':(14,15),'6':(20,20)}
G.add_nodes_from(['1','2','5','6'], pos = pos,color=color)
G.add_weighted_edges_from([('1','2',3),('5','6',7)], pos = pos,color=color)



point_colors = list(nx.get_node_attributes(G, 'color').values())
nx.draw(G, node_size=0.1, pos=pos, node_color=point_colors)
plt.show()

class_SaveLoad = SaveLoad()
class_SaveLoad.save_networkx(G,'C:/Users/86155/Desktop/' , '1', pos)

g,pos = class_SaveLoad.load_networkx('C:/Users/86155/Desktop/' , '1')

point_colors = list(nx.get_node_attributes(g, 'color').values())
nx.draw(g, node_size=0.1, pos=pos, node_color=point_colors)
plt.show()