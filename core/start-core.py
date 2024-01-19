import os
import sys

import requests
import yaml
from loguru import logger


class core:
    """
    --------------------------------------------------------------------------------------------------------------------
    基础常量区域

    """
    client = requests.session()
    Jsonheaders = {"Content-Type": "application/json", "charset": "UTF-8"}

    # def __init__(self):
    #     self.logger = logger
    #     self.logformt(self)

    def __init__(self):
        pass

    """
    --------------------------------------------------------------------------------------------------------------------
    OS/File工具类区域
    """

    # 获取项目路径
    @staticmethod
    def getFilePath():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 读取yaml文件
    @staticmethod
    def readYaml(fileName):
        with open(fileName, 'r', encoding='utf-8') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    """
    --------------------------------------------------------------------------------------------------------------------
    http请求工具类区域
        请求类型：get,post，文件上传，文件下载
    """

    @classmethod
    def doGet(cls, url1):
        return cls.client.get(url=url1, headers=None)

    @classmethod
    def doPost(cls, url):
        return cls.client.post(url=url, headers=None, data=None)

    """
    --------------------------------------------------------------------------------------------------------------------
        log区域
    """

    @staticmethod
    def log():
        loging = logger
        loging.remove()
        # 添加控制台输出的格式,sys.stdout为输出到屏幕;关于这些配置还需要自定义请移步官网查看相关参数说明
        loging.add(sys.stdout,
                   format="<green>{time:YYYYMMDD HH:mm:ss}</green> | "  # 颜色>时间
                          "{process.name} | "  # 进程名
                          "{thread.name} | "  # 进程名
                          "<cyan>{module}</cyan>.<cyan>{function}</cyan>"  # 模块名.方法名
                          ":<cyan>{line}</cyan> | "  # 行号
                          "<level>{level}</level>: "  # 等级
                          "<level>{message}</level>",  # 日志内容
                   )
        # 输出到文件的格式,注释下面的add',则关闭日志写入
        # self.logger.add(log_file_path, level='DEBUG',
        #                 format='{time:YYYYMMDD HH:mm:ss} - '  # 时间
        #                        "{process.name} | "  # 进程名
        #                        "{thread.name} | "  # 进程名
        #                        '{module}.{function}:{line} - {level} -{message}',  # 模块名.方法名:行号
        #                 rotation="10 MB")
        return loging


if __name__ == '__main__':
    core.log().error("33333333333333333333333333333")
