"""
测试 Get_Data 类 是否可以读取所有 的 节点文件
"""

from src.Graph.Data import AboutData
import os

folder_path = 'E:/expressway project/Data/source_sichuang/Catsicgl_51_2022年报_2023022717背景/'

shp_files = [folder_path+f for f in os.listdir(folder_path) if f.endswith('.shp') and f not in ['Road_C.shp', 'Road_D.shp', 'Road_G.shp', 'Road_S.shp', 'Road_V.shp', 'Road_W.shp', 'Road_X.shp', 'Road_Y.shp', 'Road_Z.shp']]

print(shp_files)

GETDATA = AboutData(shp_files)

print(len(GETDATA.data))




