
import json
from utils.HttpUtils import HttpRequest

url = "http://dong/adminapi/login"
data1 = {"account": "admin", "pwd": "19931022ld", "key": "6538b2988c955", "captchaType": "blockPuzzle"}
res = HttpRequest.doPost(url, data1)
res1 = res.json()
print(res1["data"]["token"])
# print(res1[])

# url1 = "http://dong/adminapi/user/user?label_id=&user_type=0&status=&sex=&is_promoter=&country=&isMember=&pay_count=&user_time_type=&user_time=&nickname=&province=&city=&page=1&limit=15&level=&group_id=&field_key="
# res3 = HttpRequest.doGet(url1)
# res4 = res3.json()
# print(res4)
