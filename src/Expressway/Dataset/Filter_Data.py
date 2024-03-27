# -*- coding: utf-8 -*-

"""
File: Filter_Data.py
Author: Yunheng Wang
Begin Date: 202/01/23
Description:
"""


# 引入头文件
from Expressway.Dataset.Head import Head_Filter_Data

# 引入内部文件
from Expressway.Dataset.Basic_Data import AboutData


class ExpressData(AboutData):
    def __init__(self, file_path):

        # 继承 AboutData 父类
        super(ExpressData, self).__init__(file_path = file_path)

        self.Express_Data = Head_Filter_Data.Extract_Expressway(self.data, self.number, self.data_type)

#ExpressData_1 = ExpressData('E:/Expressway/.chongqing/Graph/road/处理后数据集/22GIS.shp')
#print(ExpressData_1.Express_Data[0])
#for index,column in ExpressData_1.Express_Data[0].iterrows():
    #if column['geometry'].geom_type == 'LineString':
        #geo_row = list(column['geometry'].coords)
#for column in ExpressData_1.Express_Data[0].columns:
        #print(geo_row[:2])