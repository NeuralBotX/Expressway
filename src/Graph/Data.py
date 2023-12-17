import geopandas as gpd
from tqdm import tqdm

class AboutData():
    def __init__(self, file_path, get_pos = False):

        # 保存 输入的路径信息
        self.file_path = file_path

        # 保存 所有读取到的文件名
        self.file_name = self.__private_extract_filename()

        # 保存 共有多少条数据集合
        self.number = len(file_path)

        # 保存 路径下的所有数据集合 ---- %费时%
        self.data = self.__private_read_shp()

        # 保存每个数据对应的 地理信息类型 (分为点 和 边)
        self.data_type = self.__private_get_data_type()

        # 保存所有数据集合节点的经纬度信息
        if get_pos:
            self.pos = self.__private_get_pos()


    def __private_extract_filename(self):
        """
        :return:

        % function -> 该函数是用来获取指定路径下的所有数据
        """
        file_name = []
        for path in self.file_path:
            # 获取最后一个斜杠的索引
            last_slash_index = path.rfind('/')
            # 获取最后一个点号的索引
            last_dot_index = path.rfind('.')
            # 提取文件名
            file_name.append(path[last_slash_index + 1: last_dot_index])

        return file_name


    def __private_read_shp(self):
        """
        :return: 返回数据列表

        % function -> 该函数是用来获取指定路径下的所有数据
        """

        # 仅有一个路径字符串
        if isinstance(self.file_path,str):
            data = gpd.read_file(filename = self.file_path, encoding='UTF-8')
            # data.crs = "EPSG:4490"
            return [data]

        # 有一组路径字符串列表
        elif isinstance(self.file_path,list):
            data = []
            for i in tqdm(self.file_path, desc="Reading files", unit="file"):
                data.append(gpd.read_file(filename = i, encoding='UTF-8'))
            return data


    def __private_get_data_type(self):
        """
        :return:

        % function -> 该函数是通过截取 所有数据的列表集合 从而得到的位置信息字典
        """

        data_type = [self.data[i].geom_type.unique() for i in range(self.number)]

        return data_type


    def __private_get_pos(self):
        """
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
                sig_pos = self.data[i].set_index('CROWID')['geometry'].apply(extract_coords).to_dict()
                pos.update(sig_pos)
                print(1)
            elif self.data_type[i] == 'LineString':
                raise "wait"

        return pos


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


if __name__ == "__main__":
    path = 'E:/expressway project/Data/source_sichuan/Catsicgl_51_2022年报_2023022717背景/'
    class_data = AboutData([path + 'Road_C.shp',
                            path + 'Road_D.shp',
                            path + 'Road_G.shp',
                            path + 'Road_S.shp',
                            path + 'Road_V.shp',
                            path + 'Road_W.shp',
                            path + 'Road_X.shp',
                            path + 'Road_Y.shp',
                            path + 'Road_Z.shp'
                            ],get_pos=False)

    class_data.data_to_csv('E:/expressway project/Data/dispose_sichuan',save_all_data=True)

