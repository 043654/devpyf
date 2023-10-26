import os

import yaml


class Commons:

    def __init__(self):
        pass

    # 获取项目路径
    @classmethod
    def getFilePath(cls):
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 读取yaml文件
    @classmethod
    def readYaml(cls, fileName):
        with open(fileName, 'r', encoding='utf-8') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)


if __name__ == '__main__':
    # path = Commons.getFilePath()
    # print(path)
    # file = path + "\\data\\config.yaml"
    # print(Commons.readYaml(file))
    pass
