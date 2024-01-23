# -*- coding: utf-8 -*-

"""
File: Dataset_Position.py
Author: Yunheng Wang
Begin Date: 2024/01/23
Description:
"""

from Expressway.Dataset.Extract_Data import Position

path_road = 'E:/expressway project/Data/.sichuan/Graph/road/'
path_point = 'E:/expressway project/Data/.sichuan/Graph/place/'

class_data = Position(file_path = [path_road + 'Road_G.shp', path_point + 'CBJZCP.shp'])

# print("路网图 + 离散点图的所有位置信息 : {}".format(class_data.all_pos))                  # 打印 路网图 + 离散点图的所有位置信息
# print("离散点图的位置信息 : {}".format(class_data.node_pos))                             # 打印 离散点图的位置信息
# print("路网图的位置信息 : {}".format(class_data.road_pos))                              # 打印 路网图的位置信息
# print("路网图的位置信息翻转映射格式 : {}".format(class_data.road_pos_overturn))           # 打印 路网图的位置信息翻转映射格式