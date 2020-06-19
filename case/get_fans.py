import requests
import sys
import time
import json

time = round(time.time() * 1000)
limit = 12
lasttime = -1
print(time)


def get_fans_list():
    uid = 341496792
    url = "http://localhost:4000/user/followeds"
    data = {
        "uid": uid,
        "time": time,
        "limit": limit,
        # "lasttime":lasttime
    }
    r = requests.post(url=url, json=data)
    load_data = json.loads(json.dumps(r.json()))
    i = 0
    while (i < limit):
        userid = load_data['followeds'][i]["userId"]
        print(userid)
        i = i + 1
    return userid
