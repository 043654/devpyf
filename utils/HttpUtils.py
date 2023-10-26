import requests
import json


class HttpRequest:
    client = requests.session()
    headers = {"Content-Type": "application/json",
               "charset": "UTF-8",
               "Authori-Zation": "Bearer"
               }

    def __init__(self):
        HttpRequest.getToken()

    # 获取token
    @classmethod
    def getToken(cls):
        url = "http://dong/adminapi/login"
        data1 = {"account": "admin", "pwd": "19931022ld", "key": "6538b2988c955", "captchaType": "blockPuzzle"}
        resToken = HttpRequest.doPost(url, data1)
        resTokenJson = resToken.json()
        sessiontoken = resTokenJson["data"]["token"]
        global Token
        return sessiontoken

    @classmethod
    def doGet(cls, url1):
        return cls.client.get(url=url1, headers=cls.headers)

    @classmethod
    def doPost(cls, url, postBody):
        return cls.client.post(url=url, headers=cls.headers, data=json.dumps(postBody))


if __name__ == '__main__':
    HttpRequest()
