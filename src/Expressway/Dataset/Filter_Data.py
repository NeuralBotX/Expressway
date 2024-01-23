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
