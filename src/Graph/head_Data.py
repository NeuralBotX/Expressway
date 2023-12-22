import geopandas as gpd
from tqdm import tqdm


def extract_filename(file_path):
    """
    :param file_path: 文件绝对路径

    :return: 文件名称的列表

    % function -> 根据文件的绝对路径 提取 文件名称
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


def read_shp(file_path):
    """
    :param file_path: 文件绝对路径

    :return: 文件数据列表

    % function -> 该函数是用来获取指定路径下的所有数据
    """
    # 仅有一个路径字符串
    if isinstance(file_path,str):
        data = gpd.read_file(filename = file_path, encoding='UTF-8')
        # data.crs = "EPSG:4490"
        return [data]

    # 有一组路径字符串列表
    elif isinstance(file_path,list):
        data = []
        for i in tqdm(file_path, desc="Reading files", unit="file"):
            data.append(gpd.read_file(filename = i, encoding='UTF-8'))
        return data


def get_data_type(number, data):
    """
    :param number: 输入文件路径数量

    :param data: 加载的数据

    :return: 文件类型列表

    % function -> 获取路径下的文件类型
    """
    data_type = []
    for i in range(number):
        type = data[i].geom_type.unique()
        if 'LineString' in type:
            data_type.append('LineString')
        elif 'Point' in type:
            data_type.append('Point')
    return data_type