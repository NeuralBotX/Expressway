# -*- coding: utf-8 -*-

"""
File: Network_AboutNetwork.py
Author: Yunheng Wang
Begin Date: 2024/01/21
Description:
            1. 将重庆省龙门架excel数据格式 变成 shp文件格式
            2. 删除 空值 （删除经纬度为空或经纬度为0的）
            3. 将属性值修改为适配于代码的
"""


import pandas as pd
import geopandas as gpd
from fiona.crs import CRS
from shapely.geometry import Point


def read_xlsx(file_path):
    data = pd.read_excel(file_path, sheet_name = '门架基础信息数据')
    return data


def adjust_data(file_path):
    data = read_xlsx(file_path)
    # 将 'gantryid' 列名改为 'CROWID'
    data.rename(columns={'国标ID': 'CROWID'}, inplace=True)
    data.rename(columns={'门架ID': 'ID'}, inplace=True)
    data.rename(columns={'门架HEX编号': 'HEX'}, inplace=True)
    data.rename(columns={'名称': 'NAME'}, inplace=True)
    data.rename(columns={'桩号': 'NUMBER'}, inplace=True)
    data.rename(columns={'经度': 'LNG'}, inplace=True)
    data.rename(columns={'纬度': 'LAT'}, inplace=True)
    data.rename(columns={'方向': 'Dir'}, inplace=True)
    return data


def data_to_geopandas(file_path):
    data = adjust_data(file_path)

    # 过滤经纬度不为0.00的数据
    filtered_data = data[(data['LNG'] != 0.0) & (data['LAT'] != 0.0)]

    geometry = [Point(xy) for xy in zip(filtered_data['LNG'], filtered_data['LAT'])]
    crs = 'epsg:4490'
    geo_data = gpd.GeoDataFrame(filtered_data, geometry=geometry, crs=crs)
    for index, row in geo_data.iterrows():
        if row['geometry'].is_empty:
            print(1)
            geo_data.drop(index, inplace=True)
    return geo_data


def save_shp(file_path,save_path):
    data = data_to_geopandas(file_path)
    data.to_file(save_path, driver='ESRI Shapefile', encoding='utf-8')


if __name__ == "__main__":
    file_path = 'E:/expressway project/Data/.chongqing/flow/门架.xlsx'
    save_path = 'E:/expressway project/Data/.chongqing/Graph/place/GANTRY.shp'
    save_shp(file_path, save_path)