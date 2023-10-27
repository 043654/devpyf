import pytest
import pandas as pd
from utils.Common import Commons
from utils.HttpUtils import HttpRequest


class TestDemo:

    @pytest.fixture()
    def file(self):
        filepath = Commons.getFilePath()
        configinfo = Commons.readYaml(filepath + "\\mapper\\demoapi.yaml")
        strurl = configinfo["api"]
        return strurl

    @pytest.fixture()
    def getcsv(self):
        filepath = Commons.getFilePath()
        data = pd.read_csv(filepath + "\\data\\excel\\demo.csv")
        return data.to_string()

    def setup_class(self):
        pass

    # 获取用户管理列表
    def testdemo(self, file, getcsv):
        strn = file
        res = HttpRequest.doGet(strn)
        dd = [getcsv]
        print(dd)

    def teardown_class(self):
        pass
