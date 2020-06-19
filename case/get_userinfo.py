import requests
import sys
import time
import json
from case.get_fans import get_fans_list

get_fans_list = get_fans_list()
uid = get_fans_list
url = "http://localhost:4000/user/detail"
data = {
    "uid": uid
}
r = requests.post(url=url, json=data)
load_data = json.loads(json.dumps(r.json()))
userid = load_data["userPoint"]["userId"]
gender = load_data["profile"]["gender"]  # gender=0为女生，gender=2为男生
if (gender == 0):
    gender = "女"
else:
    gener = "男"
nickname = load_data["profile"]["nickname"]
info = [userid, nickname, gender]
print(info)
