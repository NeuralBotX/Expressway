# -*- coding: utf-8 -*-

"""
File: Log.py
Author: Yunheng Wang
Begin Date: 2024/01/22
Description: This file is used to define the log decorator.
"""


# 引入第三方库
import time
import platform
import os
from datetime import timedelta


class BasicLog:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print("\033[91mWorking:", os.getcwd())                                               # 当前执行的文件路径
        print("\033[91mName：{}".format(self.function.__name__ ))                            # 当前执行的类名

        start_time = time.time()
        result = self.function(*args, **kwargs)

        print("\033[91mTime: {}\033[0m".format(str(timedelta(seconds=time.time() - start_time)).split(".")[0])) # 该类执行完所损失的时间

        return result
