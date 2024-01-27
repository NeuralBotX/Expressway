# -*- coding: utf-8 -*-

"""
File: Network_AboutNetwork.py
Author: Yunheng Wang
Begin Date: 2024/01/21
Description: This file is used to test the AboutNetwork class in the Network file
"""


from Expressway.Graph.Network import AboutNetwork


path_road = 'E:/expressway project/Data/.sichuan/Graph/road/'
path_point = 'E:/expressway project/Data/.sichuan/Graph/place/'
Host_file_path = 'E:/expressway project/Data/Host file/'

# build_road_networkx = AboutNetwork( file_path = [path_road + 'Road_G.shp' , path_point + 'SFZP.shp', ], Host_file_path = Host_file_path, PCUI = True)
# G_Point,G_Road,G_Simplify,G_Plus = build_road_networkx(combined_network = True, draw = True, save=True)


path_road = 'E:/expressway project/Data/.chongqing/Graph/road/deal/'
path_point = 'E:/expressway project/Data/.chongqing/Graph/place/'
Host_file_path = 'E:/expressway project/Data/Host file/'
build_road_networkx = AboutNetwork( file_path = [path_road + '22GIS.shp', path_point + 'GANTRY.shp', path_point + 'SFZP.shp'], Host_file_path = Host_file_path, Expressway = True)
# build_road_networkx = AboutNetwork( file_path = [path_road + '22GIS.shp', path_point + 'SFZP.shp'], Host_file_path = Host_file_path, PCUI = True)
G_Point,G_Road,G_Simplify,G_Plus = build_road_networkx(combined_network = True, draw = True, save=True)