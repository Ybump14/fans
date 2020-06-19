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
nickname = load_data["profile"]["nickname"]
birthday = load_data["profile"]["birthday"]
city = load_data["profile"]["city"]
province = load_data["profile"]["province"]
info = [userid, nickname, gender,birthday,city,province]
print(info)
