import geopandas as gpd


class Get_Data():
    def __init__(self, path, get_pos = False):

        # 保存 输入的路径信息
        self.path = path

        # 保存 共有多少条数据集合
        self.number = len(path)

        # 保存 路径下的所有数据集合
        self.data = self.__private_read_shp(path = path)

        # 保存每个数据对应的 地理信息类型 (分为点 和 边)
        self.data_type = self.__private_get_data_type(data = self.data)

        # 保存所有数据集合节点的经纬度信息
        if get_pos:
            self.pos = self.__private_get_pos(data = self.data)


    def __private_read_shp(self, path):
        """
        :param path: 可以是一个路径字符串 或 一组路径列表

        :return: 返回数据列表

        % function -> 该函数是用来获取指定路径下的所有数据
        """

        # 仅有一个路径字符串
        if isinstance(path,str):
            data = gpd.read_file(filename = path)
            data.crs = "EPSG:4490"
            return [data]

        # 有一组路径字符串列表
        elif isinstance(path,list):
            data = []
            for i in path:
                data.append(gpd.read_file(filename = i))
            return data


    def __private_get_pos(self, data):
        """
        :param data: 路径下的所有数据的列表集合

        :return: 返回数据位置信息列表

        % function -> 该函数是通过截取 所有数据的列表集合 从而得到的位置信息字典
        """

        # 用来返回 geopandas数据集合内的经纬度信息
        def extract_coords(geom):
            return (geom.x, geom.y)  # 返回经度和纬度的元组

        pos = {}
        for i in range(self.number):
            if self.data_type[i] == 'Point':
                # 将 CROWID 与 geometry内的经纬度信息提取出来 整合成字典
                sig_pos = data[i].set_index('CROWID')['geometry'].apply(extract_coords).to_dict()
                pos.update(sig_pos)
                print(1)
            elif self.data_type[i] == 'LineString':
                raise "wait"

        return pos


    def __private_get_data_type(self, data):
        """
        :param data:
        :return:

        % function -> 该函数是通过截取 所有数据的列表集合 从而得到的位置信息字典
        """

        data_type = [self.data[i].geom_type.unique() for i in range(self.number)]
        return data_type


if __name__ == "__main__":
    re = Get_Data(['E:/expressway project/Data/source_sichuang/Catsicgl_51_2022年报_2023022717背景/Road_S.shp',
                   'E:/expressway project/Data/source_sichuang/Catsicgl_51_2022年报_2023022717背景/JTLGCP.shp'],get_pos=False)






