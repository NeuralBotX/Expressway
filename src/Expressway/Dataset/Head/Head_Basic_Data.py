# -*- coding: utf-8 -*-

"""
File: Basic_Data.py
Author: Yunheng Wang
Begin Date: 2023/12/22
Description: This file is used for the AboutData class implementation functions
"""


# 引入第三方库
import geopandas as gpd
from tqdm import tqdm


def extract_filename(file_path):
    """
    :param file_path: 数据文件的路径，输入可以是两种形式，如下：
                      1. 字符串型 str 。这通常用于构建单个网络，离散点图 或 路网图
                      2. 列表形式 list 。这通常用于构建最终的组合式路网图

    :return: 文件名称的列表

    % function -> 获取文件的名称列表
    """

    file_name = []
    if isinstance(file_path ,list):
        for path in file_path:
            # 获取最后一个斜杠的索引
            last_slash_index = path.rfind('/')
            # 获取最后一个点号的索引
            last_dot_index = path.rfind('.')
            # 提取文件名
            file_name.append(path[last_slash_index + 1: last_dot_index])

    elif isinstance(file_path, str):
        # 获取最后一个斜杠的索引
        last_slash_index = file_path.rfind('/')
        # 获取最后一个点号的索引
        last_dot_index = file_path.rfind('.')
        # 提取文件名
        file_name.append(file_path[last_slash_index + 1: last_dot_index])

    return file_name
#print(extract_filename('E:/expressway project/Data/.sichuan/flow/门架基础数据/GANTRY.shp'))

def read_shp(file_path):
    """
    :param file_path: 数据文件的路径，输入可以是两种形式，如下：
                      1. 字符串型 str 。这通常用于构建单个网络，离散点图 或 路网图
                      2. 列表形式 list 。这通常用于构建最终的组合式路网图

    :return: 读取数据集合的列表

    % function -> 读取指定路径下的所有数据
    """

    # file_path：str
    if isinstance(file_path,str):
        data = gpd.read_file(filename = file_path, encoding='UTF-8')
        # data.crs = "EPSG:4490"
        # 文件内数据过少 或 为空的不可被执行
        if not data.empty:
            return [data]
        else:
            raise ValueError(f"Error: GeoDataFrame from file {file_path} is empty.")

    # file_path：list
    elif isinstance(file_path,list):
        data = []
        for i in tqdm(file_path, desc="Reading files", unit="file"):
            gdf = gpd.read_file(filename=i, encoding='UTF-8')
            # 文件内数据过少 或 为空的不可被执行
            if not gdf.empty and len(gdf) > 10:
                data.append(gdf)
            else:
                raise ValueError(f"Error: GeoDataFrame from file {i} is empty or too few.")

        return data

#print(read_shp('E:/Expressway/.sichuan\/Graph/place/处理后数据集/GANTRY.shp'))
def get_data_type(number, data):
    """
    :param number: 输入文件路径数量

    :param data: 预加载的数据

    :return: 文件类型列表

    % function -> 获取路径下的文件类型
    """

    data_type = []
    for i in range(number):
        type = data[i].geom_type.unique()
        if 'LineString' in type:
            data_type.append('LineString')
        elif 'Point' in type:
            data_type.append('Point')

    return data_type
#print(get_data_type(1, read_shp('E:/Expressway/.sichuan\/Graph/place/处理后数据集/GANTRY.shp')))
