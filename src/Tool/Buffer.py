import networkx as nx
import random
import json


class SaveLoad():
    def save_networkx(self, G, save_path, save_name, pos_data):
        """
        :param G:

        :param save_path:

        :param save_name:

        :return:

        % function ->
        """
        position_file = save_name + '_positions.txt'
        graph_file = save_name + '_graph.txt'

        # 有边的网络 如 路网图 简化图 组合图
        if len(G.edges()) > 0:
            # 保存 边的连接关系 边的权重 边的颜色
            with open(save_path + graph_file, 'w') as wf:
                for edge in G.edges(data=True):
                    # 有权重信息
                    if 'weight' in edge[2]:
                        wf.write(f"{edge[0]} {edge[1]} {edge[2]['weight']}\n")
                    # 无权重信息
                    else:
                        wf.write(f"{edge[0]} {edge[1]}\n")

        # 无边网络 如 特殊点图
        else:
            with open(save_path + graph_file, 'w') as wf:
                for node in G.nodes():
                    wf.write(f"{node}\n")

        # 保存 点的位置信息
        with open(save_path + position_file, 'w') as file:
            json.dump(pos_data, file)


    def load_networkx(self, load_path, load_name):
        """
        :param load_path:

        :param load_name:

        :param draw:

        :return:

        % function ->
        """

        position_file = load_name + '_positions.txt'
        graph_file = load_name + '_graph.txt'

        with open(load_path + position_file, 'r') as file:
            pos = json.load(file)

        with open(load_path + graph_file, 'r') as file:
            edges_weights = []
            nodes = set()
            weight = 0 # 1 - 有权重信息，有连边属性 // 0 - 无权重信息，有连边属性 // -1 - 无权重信息，无连边属性，仅有点

            for line in file:
                data = line.strip().split()  # 将每行数据分割

                # 有权重信息，有连边属性
                if len(data) == 3:  # 如果数据长度为 3，则包含权重信息
                    edges_weights.append([data[0], data[1], float(data[2])])
                    nodes.update(data[:2])  # 将节点添加到集合中
                    weight = 1

                # 无权重信息，有连边属性
                elif len(data) == 2:  # 否则只有节点信息，没有权重信息
                    edges_weights.append([data[0], data[1]])
                    nodes.update(data[:2])  # 将节点添加到集合中

                # 无权重信息，无连边属性，仅有点
                elif len(data) == 1:
                    nodes.add(data[0])
                    weight = -1

        G = nx.Graph()

        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        if weight == 1:
            G.add_nodes_from(list(nodes), pos=pos, color = color)
            G.add_weighted_edges_from(edges_weights, pos = pos, color = color)
        elif weight == 0:
            G.add_nodes_from(nodes, pos=pos, color=color)
            G.add_edges_from(edges_weights, pos=pos, color=color)
        elif weight == -1:
            G.add_nodes_from(nodes, pos=pos, color=color)

        return G, pos













