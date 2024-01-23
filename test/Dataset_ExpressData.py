# -*- coding: utf-8 -*-

"""
File: Dataset_ExpressData.py
Author: Yunheng Wang
Begin Date: 2024/01/23
Description: This file is used to test the ExpressData class in the Dataset file
"""


from Expressway.Dataset.Filter_Data import ExpressData


path_road = 'E:/expressway project/Data/.sichuan/Graph/road/'
path_point = 'E:/expressway project/Data/.sichuan/Graph/place/'

class_data = ExpressData(file_path = [path_road + 'Road_G.shp', path_point + 'CBJZCP.shp'])

