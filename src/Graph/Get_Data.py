import geopandas as gpd


class Get_Data():
    def __init__(self, path, get_pos = False):
        self.path = path
        # 获取路径下的所有数据集合
        data = self.__private_read_shp(path = path)
        self.data = data

        if get_pos:
            self.pos = self.get_pos(self.data)


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


    def get_pos(self,data):
        """
        :param data: 路径下的所有数据的列表集合

        :return: 返回数据位置信息列表

        % function -> 该函数是通过截取 所有数据的列表集合 从而得到的位置信息字典
        """

        # 用来返回 geopandas数据集合内的经纬度信息
        def extract_coords(geom):
            return (geom.x, geom.y)  # 返回经度和纬度的元组

        pos = {}
        for i in data:
            # 将 CROWID 与 geometry内的经纬度信息提取出来 整合成字典
            sig_pos = i.set_index('CROWID')['geometry'].apply(extract_coords).to_dict()
            pos.update(sig_pos)
        return pos


if __name__ == "__main__":
    re = Get_Data(['E:/expressway project/Data/source_sichuang/Catsicgl_51_2022年报_2023022717背景/CBJZCP.shp','E:/expressway project/Data/source_sichuang/Catsicgl_51_2022年报_2023022717背景/SDP.shp'],get_pos=True)






