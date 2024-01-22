# -*- coding: utf-8 -*-

"""
File: Basic_Data.py
Author: Yunheng Wang
Begin Date: 2023/12/22
Description: This file is used for the AboutNetwork class implementation functions
"""


# 引入第三方库
from tqdm import tqdm
from scipy.spatial import KDTree
import random
from geopy.distance import geodesic


def generate_nodes_and_edges(data, pos):
    """
    :param data: 预提取图信息的数据

    :param pos: 位置信息的字典

    :return: 点的集合， 连边的集合

    % function -> 提取输入数据中的 图信息（点及连边关系）
    """

    edges = []                  # 连边集合的数据结构
    nodes = []                  # 点的集合的数据结构

    for index, row in data.iterrows():
        """
        注意：在构建路网图的基础数据中存在两种数据类型格式，分别为：MultiLineString(线段)，LineString(直线)
        思路：基本思路是将 MultiLineString 转化为 LineString 也就是说线段 到 直线的转化
        """

        # MultiLineString 类型的处理方式
        if row['geometry'].geom_type == 'MultiLineString':
            geo_row = []
            geoms = list(row['geometry'].geoms)
            for geo in geoms:
                for lin in list(geo.coords):
                    geo_row.append(lin)

        # LineString 类型的处理方式
        elif row['geometry'].geom_type == 'LineString':
            geo_row = list(row['geometry'].coords)

        # 添加数据
        for i in range(len(geo_row)):
            node = pos[(geo_row[i][0], geo_row[i][1])]
            front_node = pos[(geo_row[i - 1][0], geo_row[i - 1][1])]
            nodes.append(node)
            if i > 0:
                edges.append([node, front_node])

    # 点的集合， 连边的集合
    return nodes, edges


def build_network(G, seed, nodes, edges, pos, weight = False):
    """
    :param G: 输入一个图G  (一般为空)

    :param seed: 随机种子数字

    :param nodes: 构造网络所需要的 节点列表

    :param edges: 构造网络所需要的 连边关系

    :param pos: 点的位置信息 ,位置信息格式  {路网图中点的ID：(经度，维度),...} 。

    :param weight: 是否有权重信息

    :return: 构建好的networkx图

    % function -> 根据给定数据构建 网络图
    """

    # 构造无权加权网络
    if weight == False:
        random.seed(seed)
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        G.add_nodes_from(nodes, pos=pos, color=color)
        G.add_edges_from(edges, pos=pos, color=color)

    # 构造无向无权网络
    else:
        random.seed(seed)
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        G.add_nodes_from(nodes, pos=pos, color=color)
        G.add_weighted_edges_from(edges, pos=pos, color=color)

    return G


def mapping(base_network, target_network, base_network_pos, target_network_pos):
    """
    :param base_network: 路网的networkx图

    :param target_network: 特殊点的networkx图

    :param base_network_pos:  路网图中点的位置信息 {点id：(经度,维度), ...}

    :param target_network_pos: 特殊点的位置信息 {点id：(经度,维度), ...}

    :return: point_to_road_node - 特殊点与路网点之间的关联关系 {point_id：road_node_id}

    % function -> 为了建立组合网络，我们将特殊点根据其在路网上的就近原则来进行特殊点至路网的归一化处理。
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

    # 机器学习方法 ： 使用 KD树 的算法来快速查找 每个每个节点对应最近的道路网络点
    base_network_pos_list = [base_network_pos[k] for k in base_network.nodes()]
    base_network_nodes = list(base_network.nodes())

    KDtree = KDTree(base_network_pos_list)  # 创建了 KD 树

    mapping_dict = {}
    mapping_dict_overturn = {}

    for i in tqdm(target_network.nodes(), desc='Mapping', unit=" node"):
        i_JD, i_WD = target_network_pos[i]
        _, nearest_networkx_index = KDtree.query([i_JD, i_WD], k=1)  # [i_JD, i_WD] - 目标节点的经纬度 ,k 表示要返回的最近邻点的数量
        mapping_dict[i] = base_network_nodes[nearest_networkx_index]
        mapping_dict_overturn[base_network_nodes[nearest_networkx_index]] = i

    return mapping_dict,mapping_dict_overturn


def find_node_degree_e1_b2(G):
    """
    :param G: 输入的networkx网络

    :return: 返回 一个元组 元组内第一个为 度为1的点的集合 元组内第二个为 度大于2的点的集合 -> (度为1的点的集合, 度大于2的点的集合)

    % function -> 找到网络 G 所有 degree > 2 和 degree = 1 的点
    """

    degree_greater2_nodelist = []
    degree_equal1_nodelist = []

    for node, degree_value in G.degree():
        if degree_value > 2:
            degree_greater2_nodelist.append(node)
        elif degree_value == 1:
            degree_equal1_nodelist.append(node)

    return (degree_equal1_nodelist,degree_greater2_nodelist)


def count_distance(path, pos):
    """
    :param path: 一条 路径 列表

    :param pos: 路径列表对应的 位置信息 字典

    :return: 返回 路径 两端点之间的距离

    % function -> 计算一条路径中两个端点的距离
    """

    distance = 0
    for i in range(len(path)):
        if i > 0:
            point1 = pos[path[i]]
            point2 = pos[path[i-1]]
            # geodesic 输入 需要为 (纬度,经度)
            distance += geodesic( (point1[1],point1[0]), (point2[1],point2[0])).meters

    return distance

