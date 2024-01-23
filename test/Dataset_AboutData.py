# -*- coding: utf-8 -*-

"""
File: Dataset.AboutData.py
Author: Yunheng Wang
Begin Date: 2024/01/21
Description: This file is used to test the AboutData class in the Dataset file
"""


from Expressway.Dataset.Basic_Data import AboutData


# ============ test AboutData ============
path = 'E:/expressway project/Data/.chongqing/Graph/road/deal/'

class_data = AboutData(file_path = [path + '22GIS.shp'])

print("数据路径 : {}".format(class_data.file_path))                                     # 打印 所有的数据路径
print("数据文件名 : {}".format(class_data.file_name))                                   # 打印 所有的数据文件名
print("数据数量 : {}".format(class_data.number))                                        # 打印 所有的数据数量
print("数据集合 : {}".format(class_data.data))                                          # 打印所 有的数据集合
print("数据的类型 : {}".format(class_data.data_type))                                    # 打印 所有数据的类型
# print(class_data.data[0].iloc[0])

# ============ test data_to_csv ============
class_data.data_to_csv(save_path='C:/Users/86155/Desktop/新建文件夹')
