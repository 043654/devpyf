import requests
import json

from utils.Common import Commons


class HttpRequest:
    client = requests.session()
    Jsonheaders = {"Content-Type": "application/json", "charset": "UTF-8"}

    def __init__(self):
        HttpRequest.getToken()

    # 获取token
    @classmethod
    def getToken(cls):
        filepath = Commons.getFilePath()
        configinfo = Commons.readYaml(filepath + "\\config\\config.yaml")
        url = configinfo["token"]
        data1 = configinfo["login"]
        resToken = cls.client.post(url, data1)
        resTokenJson = resToken.json()
        sessiontoken = resTokenJson["data"]["token"]
        cls.Jsonheaders = {"Content-Type": "application/json",
                           "charset": "UTF-8",
                           "Authori-Zation": "Bearer" + " " + sessiontoken
                           }
        return cls.Jsonheaders

    @classmethod
    def doGet(cls, url1):
        return cls.client.get(url=url1, headers=HttpRequest.getToken())

    @classmethod
    def doPost(cls, url, postBody):
        return cls.client.post(url=url, headers=HttpRequest.getToken(), data=json.dumps(postBody))
