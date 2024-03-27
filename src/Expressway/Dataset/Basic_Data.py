# -*- coding: utf-8 -*-

"""
File: Basic_Data.py
Author: Yunheng Wang
Begin Date: 2023/12/17
Description: This file is used to read and extract the underlying data.
"""


# 引入类的头文件
from Expressway.Dataset.Head import Head_Basic_Data


# 引入第三方库
from tqdm import tqdm


class AboutData:
    def __init__(self, file_path):
        """
        :param file_path: 数据文件的路径，输入可以是两种形式，如下：
                          1. 字符串型 str 。这通常用于构建单个网络，离散点图 或 路网图
                          2. 列表形式 list 。这通常用于构建最终的组合式路网图

        % function -> 初始化 AboutData 类
        """

        # 保存 输入的路径信息 - str / list
        self.file_path = file_path

        # 保存 所有读取到的文件名 - list
        self.file_name = Head_Basic_Data.extract_filename(self.file_path)

        # 保存 共有多少条数据集合 - int
        self.number = len(file_path) if isinstance(file_path,list) else 1

        # 保存 路径下的所有数据集合 %费时% - list
        self.data = Head_Basic_Data.read_shp(self.file_path)

        # 保存 每个数据对应的地理信息类型 (分为点 和 边) - list
        self.data_type = Head_Basic_Data.get_data_type(self.number, self.data)


    def __getitem__(self, index):
        """
        :param index: 索引的下标

        :return: 返回索引值对应的数据集

        % function -> 利用索引获取 self.data 的某个数据集
        """

        return self.data[index]


    def data_to_csv(self, save_path):
        """
        :param save_path: 预保存的文件夹路径

        :return: 空

        % function -> 用于将 self.data 数据集合保存成csv文件

        % authority -> 可被外部调用
        """

        total_files = self.number
        for idx,sig in tqdm(enumerate(self.data), desc="Saving files", unit="file", total=total_files):
            sig.to_csv( save_path + '/' + self.file_name[idx] + '.csv', index=False, encoding='utf-8-sig')

        return


    def __build__(self, *args, **kwargs):
        '''

        % function -> 用于子类的多态
        '''

        pass


    def __call__(self, *args, **kwargs):
        """
        % function -> 当子类对其进行重写时，该方法的主要功能是定义在执行 __call__ 成员函数之前，默认执行 __build__ 成员函数
        """

        self.__build__()
        pass


if __name__ == "__main__":

    pass
