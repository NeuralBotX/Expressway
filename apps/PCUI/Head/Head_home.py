# -*- coding: utf-8 -*-

"""
File: apps/home.py
Author: Yunheng Wang
Begin Date: 2024/01/25
Description: This file is the header file of the main page
"""


import networkx as nx
import matplotlib.pyplot as plt
import os
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk


def home_centre_pos(root,width, height):
    """
    :param root:

    :param width:

    :param height:

    :return:

    % function ->
    """

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # 计算窗口左上角坐标使其居中
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    return x,y


def extract_filename(file_path):
    """
    :param

    :return:

    % function ->
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


def cache(G, pos, save_name):
    """
    :param G:

    :param pos:

    :param save_name:

    :return:

    % function ->
    """

    point_colors = list(nx.get_node_attributes(G, 'color').values())
    image = nx.draw(G, node_size = 0.1, pos=pos, node_color=point_colors)
    plt.savefig(save_name)
    plt.show()


def show_pic(root, image_name):
    """
    :param root:

    :param image_name:

    :return:

    % function ->  生成图像至界面
    """

    # 生成图像至界面
    image = Image.open(image_name)
    image = image.resize((470, 330))
    # 将图像转换为Tkinter PhotoImage
    tk_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, bg="#1E1E1E")
    image_label.place(x=300, y=130)
    # 更新Label中的图像
    image_label.config(image=tk_image)
    # 保留对图像对象的引用，以避免垃圾回收
    image_label.image = tk_image


