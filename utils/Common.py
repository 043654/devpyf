import os

import yaml


class Commons:

    def __init__(self):
        pass

    # 获取项目路径
    @staticmethod
    def getFilePath():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 读取yaml文件
    @staticmethod
    def readYaml(fileName):
        with open(fileName, 'r', encoding='utf-8') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)


if __name__ == '__main__':
    filepath = Commons.getFilePath()
    print(Commons.readYaml(filepath + "\\config\\config.yaml"))
