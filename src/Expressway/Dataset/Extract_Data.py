# -*- coding: utf-8 -*-

"""
File: Extract_Data.py
Author: Yunheng Wang
Begin Date: 202/01/23
Description: This file is used to extract location information.
"""


# 引入头文件
from Expressway.Dataset.Head import Head_Extract_Data
from Expressway.Dataset.Head import Head_Crawl_Data

# 引入内部文件
from Expressway.Dataset.Basic_Data import AboutData


class Position(AboutData):
    def __init__(self, file_path):

        # 继承 AboutData 父类
        super(Position, self).__init__(file_path = file_path)

        # 保存 路网图 + 离散点图的所有位置信息 -> all_pos
        # 保存 离散点图的位置信息 -> node_pos
        # 保存 路网图的位置信息 -> road_pos
        # 保存 路网图的位置信息翻转映射格式 -> road_pos_overturn
        self.all_pos, self.node_pos, self.road_pos, self.road_pos_overturn,self.node_name_pos = Head_Extract_Data.get_pos(self.data, self.number, self.data_type)
        #self.road_pos_cleand = Head_Crawl_Data.clean_data(self.road_pos,3000)






