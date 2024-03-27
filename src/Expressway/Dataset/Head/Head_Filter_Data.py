# -*- coding: utf-8 -*-

"""
File: Head_Filter_Data.py
Author: Yunheng Wang
Begin Date: 2024/01/23
Description: This file is used for the ExpressData class implementation functions
"""


# 引入第三方库
from tqdm import tqdm


def Extract_Expressway(data, number, data_type):
    """
    :param data:

    :param number:

    :param data_type:

    :return:

    % function ->筛选出高速公路线路数据的信息
    """

    filter_data = []

    for i in tqdm(range(number), desc='Extract expressway road graph', unit="file"):

        if data_type[i] == 'LineString':
            middle = data[i].copy()                                                     # 使用copy是为了防止对传入的data进行修改

            # 多用于四川的数据
            if 'LXBH' in list(data[i].columns) and 'LDJSDJ' in list(data[i].columns) and 'LXMC' in list(data[i].columns):
                for index, row in data[i].iterrows():
                    if (row['LXBH'] is not None and len(row['LXBH']) != 4) or (row['LDJSDJ'] is not None and  row['LDJSDJ'] == 1) or (row['LXMC'] is not None and '高速' in row['LXMC']):
                        continue
                    else:
                        middle.drop(index, inplace=True)
                filter_data.append(middle)

            # 多用于处理过的数据 或 重庆数据
            else:
                for index, row in data[i].iterrows():
                    if (row['LXBH'] is not None and len(row['LXBH']) != 4) or (row['LXMC'] is not None and '高速' in row['LXMC']):
                        continue
                    else:
                        middle.drop(index, inplace=True)
                filter_data.append(middle)

        elif data_type[i] == 'Point':
            middle = data[i].copy()                                                     # 使用copy是为了防止对传入的data进行修改
            filter_data.append(middle)

    return filter_data
