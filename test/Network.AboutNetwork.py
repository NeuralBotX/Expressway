# -*- coding: utf-8 -*-

"""
File: Network.AboutNetwork.py
Author: Yunheng Wang
Begin Date: 2024/01/21
Description: This file is used to test the AboutNetwork class in the Network file
"""


from Expressway.Graph.Network import AboutNetwork


path = 'E:/expressway project/Data/source_sichuan/基础数据/'
Host_file_path = 'E:/expressway project/Data/Host file/'

build_road_networkx = AboutNetwork( file_path = [path + 'Road_G.shp', path + 'GYJGP.shp'], Host_file_path = Host_file_path)
G_Point,G_Road,G_Simplify,G_Plus = build_road_networkx(combined_network = True, draw = True, save=True)
