import head_Data

import numpy as np
from tqdm import tqdm
from shapely.geometry import MultiLineString, LineString
from shapely.ops import unary_union

class AboutData:
    def __init__(self, file_path, get_pos = False):

        # 保存 输入的路径信息 - str / list
        self.file_path = file_path

        # 保存 所有读取到的文件名 - list
        self.file_name = head_Data.extract_filename(self.file_path)

        # 保存 共有多少条数据集合 - int
        self.number = len(file_path) if isinstance(file_path,list) else 1

        # 保存 路径下的所有数据集合 ---- %费时% - list
        self.data = head_Data.read_shp(self.file_path)

        # 保存每个数据对应的 地理信息类型 (分为点 和 边) - list
        self.data_type = head_Data.get_data_type(self.number, self.data)

        # 保存 path 路径下 路网 和 关键点的经纬度集合 - dict
        if get_pos:
            self.all_pos, self.node_pos, self.road_pos, self.road_pos_overturn = self.__private_get_pos()


    def __private_get_pos(self):
        """
        :return: 返回数据位置信息列表

        % function -> 该函数是通过截取 所有数据的列表集合 从而得到的位置信息字典
        """

        # 用来返回 geopandas数据集合内的经纬度信息

        node_pos = {} # 点的位置信息
        road_pos = {} # 路网点的位置信息
        road_pos_overturn = {} # road_pos 的键值对翻转形式
        all_pos = {} # 用来存储 点和边 的所有位置信息
        for i in tqdm(range(self.number), desc='Getting location information', unit="file"):

            if self.data_type[i] == 'Point':
                # 将 CROWID 与 geometry内的经纬度信息提取出来 整合成字典
                # sig_pos = self.data[i].set_index('CROWID')['geometry'].apply(extract_coords).to_dict()
                # node_pos.update(sig_pos)
                for index, row in self.data[i].iterrows():
                    crow_id = row['CROWID']
                    geometry = row['geometry']
                    node_pos[crow_id] = (geometry.x,geometry.y)
                    all_pos[crow_id] = (geometry.x,geometry.y)

            elif self.data_type[i] == 'LineString':
                for index, row in self.data[i].iterrows():
                    # 在路网中 存在两中 数据类型的格数 MultiLineString(线段) 与 LineString(直线)
                    # 我们的基本思路是将 MultiLineString 转化为 LineString 也就是说线段 到 直线的转化

                    # MultiLineString 类型的处理方式
                    if row['geometry'].geom_type == 'MultiLineString':
                        geo_row = []
                        geoms = list(row['geometry'].geoms)
                        for geo in geoms:
                            for lin in list(geo.coords):
                                geo_row.append(lin)
                    # LineString 类型的处理方式
                    elif row['geometry'].geom_type == 'LineString':
                        geo_row = list(row['geometry'].coords)

                    id_row = row['CROWID']
                    for sig_idx, sig_jd_wd in enumerate(geo_row):
                        if sig_jd_wd in road_pos:
                            continue
                        else:
                            name = id_row + '@' + str(sig_idx)
                            jd_wd = (sig_jd_wd[0],sig_jd_wd[1])
                            road_pos[jd_wd] = name
                            road_pos_overturn[name] = jd_wd
                            all_pos[name] = jd_wd

        return all_pos,node_pos,road_pos,road_pos_overturn


    def __getitem__(self, index):
        """
        :param index:

        :return:

        % function -> 获取 self.data 的某个数据集
        """

        return self.data[index]


    def data_to_csv(self, save_path, save_all_data = True):
        """

        :param save_path:

        :param save_all_data:

        :return:

        % function -> 用于将 self.data 数据集合保存成csv文件
        """
        if save_all_data:
            total_files = self.number
            for idx,sig in tqdm(enumerate(self.data), desc="Saving files", unit="file", total=total_files):
                sig.to_csv( save_path + '/' + self.file_name[idx] + '.csv', index=False, encoding='utf-8-sig')
        else:
            pass

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
    path = 'E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/'
    class_data = AboutData([# path + 'Road_C.shp',
                            # path + 'Road_D.shp',
                            # path + 'Road_G.shp',
                            # path + 'Road_S.shp',
                            # path + 'Road_V.shp',
                            # path + 'Road_W.shp',
                            # path + 'Road_X.shp',
                            path + 'Road_Y.shp',
                            # path + 'Road_Z.shp'
                            ],get_pos=True)
