from src.Graph.Get_Data import Get_Data
import os
import networkx as nx
import matplotlib.pyplot as plt

data = Get_Data(['E:/expressway project/Data/source_sichuang/Catsicgl_51_2022年报_2023022717背景/Road_S.shp'])

id = data.data[0].iloc[0]['CROWID']
gre = list(data.data[0].iloc[0]['geometry'].coords)

q_x = data.data[0].iloc[0]['QDWZ_JD']
q_y = data.data[0].iloc[0]['QDWZ_WD']
print((q_x,q_y))
z_x = data.data[0].iloc[0]['ZDWZ_JD']
z_y = data.data[0].iloc[0]['ZDWZ_WD']
print((z_x,z_y))

allpos = {}

all_edge = []
for i in range(len(gre)):
    if i == 0:
        pass
    else:
        all_edge.append([id+str(i),id+str(i-1)])
    allpos[id+str(i)] = (gre[i][0],gre[i][1])

print(list(allpos.values()))

G = nx.Graph()

G.add_edges_from(all_edge,pos = allpos)

nx.draw(G, node_size=1, pos=allpos)
plt.show()
