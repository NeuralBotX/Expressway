# encoding:utf-8
'''
@author: Yawen Tan
@project: Expressway
@file: Crawl_Data.py
@time: 2024/3/13 15:49
@desc:
'''

from Expressway.Dataset.Head import Head_Crawl_Data


# 引入内部文件
from Expressway.Dataset.Basic_Data import AboutData
from Expressway.Dataset.Extract_Data import Position

from tqdm import tqdm

class Clean(Position,AboutData):
    def __init__(self, file_path):

        # 继承 AboutData 父类
        super(Clean, self).__init__(file_path = file_path)




        self.clean_node_pos = Head_Crawl_Data.clean_data(self.node_pos,3000)


        self.clean_road_pos_overturn = Head_Crawl_Data.clean_data(self.road_pos,3000)
        self.clean_road_pos = {value: key for key, value in self.clean_road_pos_overturn.items()}
        self.clean_all_pos = dict(**self.clean_node_pos, **self.clean_road_pos)
        #self.clean_node_name_pos = Head_Crawl_Data.clean_data(self.node_name_pos)




#Clean_1 = Clean('E:/Expressway/.chongqing/Graph/place/处理后数据集/SFZP.shp')
#print(Clean_1.clean_node_pos)
#print(Clean_1.clean_road_pos_overturn)
#print(Clean_1.clean_road_pos_overturn)
#print(Clean_1.clean_road_pos)
#print(len(Clean_1.clean_road_pos))





















