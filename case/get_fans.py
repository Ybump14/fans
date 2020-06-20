import requests
import sys
import time
import json
from lib.publice_data import Login


class Get_Fan_UserId(object):

    def get_fans(self):
        login = Login()
        url = login.get_follweds_url()
        data = login.get_follweds_data()
        limit = login.limit
        r = requests.post(url=url, json=data)
        load_data = json.loads(json.dumps(r.json()))
        useridData = []
        i = 0
        while (i < limit):
            userid = load_data['followeds'][i]["userId"]
            useridData.append(userid)
            i = i + 1
        return useridData


