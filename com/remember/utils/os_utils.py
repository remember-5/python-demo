import os

CONFIG_PATH = '\\config'


class OSUtils:

    @staticmethod
    def get_file(file):
        """
        获取配置文件
        :param file:
        :return:
        """
        print(file)
        print(CONFIG_PATH)

    @staticmethod
    def get_path_filename(path):
        """
        获取地址下的所有文件名字
        :param path:
        :return:
        """
        return os.listdir(path)

    @staticmethod
    def get_path_file(path):
        for root, dirs, files in os.walk(path):
            print('root_dir:', root)  # 当前目录路径
            print('sub_dirs:', dirs)  # 当前路径下所有子目录
            print('files:', files)  # 当前路径下所有非目录子文件


if __name__ == '__main__':
    OSUtils.get_file("1")
