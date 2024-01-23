# -*- coding: utf-8 -*-

"""
File: Head_Extract_Data.py
Author: Yunheng Wang
Begin Date: 2024/01/23
Description:
"""


# 引入第三方库
import geopandas as gpd
from tqdm import tqdm


def get_pos(data, number, data_type):
    """
    :param data: 路径下的所有数据集合

    :param number: 输入文件路径数量

    :param data_type: 每个数据对应的地理信息类型

    :return: 路网图 + 离散点图的所有位置信息 、 离散点图的位置信息 、 路网图的位置信息 、 路网图的位置信息翻转映射格式

    % function -> 从基础数据中提取位置信息
    """

    node_pos = {}                           # 离散点图的位置信息 {离散点图中点的ID：(经度，维度),...}
    road_pos = {}                           # 路网图的位置信息  {(经度，维度)：路网图中点的ID,...}
    road_pos_overturn = {}                  # 路网图的位置信息翻转映射格式  {路网图中点的ID：(经度，维度),...} 。
    all_pos = {}                            # 路网图 + 离散点图的所有位置信息 {离散点图中点的ID：(经度，维度),路网图中点的ID：(经度，维度),...}

    for i in tqdm(range(number), desc='Getting location information', unit="file"):

        # ============================== 离散点图的位置信息提取 ==============================
        if data_type[i] == 'Point':
            for index, row in data[i].iterrows():
                crow_id = row['CROWID']
                geometry = row['geometry']
                jd_wd = (geometry.x,geometry.y)             # 保存的经纬度格式为： (经度，纬度)
                node_pos[crow_id] = jd_wd                   # 离散点图的经纬度信息保存至 node_pos
                all_pos[crow_id] = jd_wd                    # 离散点图的经纬度信息保存至 all_pos

        # ============================== 路网图的位置信息提取 ==============================
        elif data_type[i] == 'LineString':
            for index, row in data[i].iterrows():
                """
                注意：在构建路网图的基础数据中存在两种数据类型格式，分别为：MultiLineString(线段)，LineString(直线)
                思路：基本思路是将 MultiLineString 转化为 LineString 也就是说线段 到 直线的转化
                """

                # geometry
                if row['geometry'] is not None:
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

                    # 保存至数据类型
                    id_row = row['CROWID']
                    for sig_idx, sig_jd_wd in enumerate(geo_row):
                        if sig_jd_wd in road_pos:
                            continue
                        else:
                            name = str(id_row) + '@' + str(sig_idx)      # 为线路节点分配 唯一的id 形式为：线路的唯一id(也称行的唯一表标识) + @ + 递增数值字符串
                            jd_wd = (sig_jd_wd[0],sig_jd_wd[1])     # 保存的经纬度格式为： (经度，纬度)
                            road_pos[jd_wd] = name                  # 路网图的经纬度信息保存至 road_pos
                            road_pos_overturn[name] = jd_wd         # 路网图的经纬度信息保存至 road_pos_overturn
                            all_pos[name] = jd_wd                   # 路网图的经纬度信息保存至 all_pos

    # 路网图 + 离散点图的所有位置信息 、 离散点图的位置信息 、 路网图的位置信息 、 路网图的位置信息翻转映射格式
    return all_pos,node_pos,road_pos,road_pos_overturn