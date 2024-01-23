# -*- coding: utf-8 -*-

"""
File: Chongqing_road.py
Author: Yunheng Wang
Begin Date: 2024/01/23
Description:
"""


import geopandas as gpd


def read_data(file_path):
    gdf = gpd.read_file(file_path)
    return gdf



def adjust_data(file_path):
    data = read_data(file_path)
    data = data.rename(columns={'OBJECTID': 'CROWID', 'lxdm': 'LXBH', 'ldjsdj': 'LXMC' })
    return data


def save_shp(file_path,save_path):
    data = adjust_data(file_path)
    data.to_file(save_path, driver='ESRI Shapefile', encoding='utf-8')


if __name__ == "__main__":
    path = 'E:/expressway project/Data/.chongqing/Graph/road/'
    save_path = 'E:/expressway project/Data/.chongqing/Graph/road/deal/22GIS.shp'
    file_path = path + '22GIS.shp'

    save_shp(file_path, save_path)