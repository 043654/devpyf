import requests


class HttpRequest:
    client = requests.session()

    def __init__(self):
        pass

    def doGet(self, headers, url):
        res = self.client.get(url=url, headers=headers)
        print(res.status_code)

    def doPost(self):
        url = "http://dong/adminapi/login"
        headers = {"Content-Type": "application/json"}
        data1 = {"account": "admin", "pwd": "19931022ld", "key": "6538b2988c955", "captchaType": "blockPuzzle",
                 "captchaVerification": ""}
        res = self.client.post(url=url, headers=headers, data=data1)


if __name__ == '__main__':
    HttpRequest()


