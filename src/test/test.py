

import networkx as nx

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 2), (2, 3), (3, 3)])

# 查找自环边
self_loops = list(nx.selfloop_edges(G))

# 移除自环边
G.remove_edges_from(self_loops)

# 输出删除自环边后的边列表
print(G.edges())