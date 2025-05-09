# -*- coding: utf-8 -*-

"""
File: Sichuan_Gantry.py
Author: Yunheng Wang
Begin Date: 2024/01/23
Description:
            1. 将四川省门架excel数据格式 变成 shp文件格式
            2. 删除 空值 （删除经纬度为空或经纬度为0的）
            3. 将属性值修改为适配于代码的
"""


# 引入第三方库
import pandas as pd
import geopandas as gpd
from fiona.crs import CRS
from shapely.geometry import Point


def read_xlsx(file_path):
    data = pd.read_excel(file_path)

    return data


def adjust_data(file_path):
    data = read_xlsx(file_path)
    # 将 'gantryid' 列名改为 'CROWID'
    data.rename(columns={'gantryid': 'CROWID'}, inplace=True)
    # 因为 .shp 文件不能保存超过10个字符的 因此修改为十个字符以内
    data.rename(columns={'etcgantryhex': 'etcgantry'}, inplace=True)
    return data


def data_to_geopandas(file_path):
    data = adjust_data(file_path)

    # 过滤经纬度不为0.00的数据
    filtered_data = data[(data['lng'] != 0.0) & (data['lat'] != 0.0)]

    geometry = [Point(xy) for xy in zip(filtered_data['lng'], filtered_data['lat'])]
    crs = 'epsg:4490'
    geo_data = gpd.GeoDataFrame(filtered_data, geometry=geometry, crs=crs)

    for index, row in geo_data.iterrows():
        if row['geometry'].is_empty:
            print(1)
            geo_data.drop(index, inplace=True)

    return geo_data


def save_shp(file_path,save_path):
    data = data_to_geopandas(file_path)
    # print(data.crs)  # 打印空间参考信息
    data.to_file(save_path, driver='ESRI Shapefile', encoding='utf-8')



if __name__ == "__main__":
    file_path = 'E:/expressway project/Data/.sichuan/flow/门架基础数据/1门架基础信息数据gantry.xlsx'
    save_path = 'E:/expressway project/Data/.sichuan/flow/门架基础数据/GANTRY.shp'
    save_shp(file_path, save_path)

