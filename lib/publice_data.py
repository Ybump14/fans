import datetime
import json
import random
import string
import requests
import time


class Login(object):

    def get_follweds_url(self):
        self.url = "http://localhost:4000/user/followeds"
        return self.url

    def get_user_detail_url(self):
        self.url = "http://localhost:4000/user/detail"
        return self.url

    def get_follweds_data(self):
        self.uid = 341496792
        self.time = round(time.time() * 1000)
        self.limit = 10
        self.lasttime = -1
        self.data = {
            "uid": self.uid,
            "time": self.time,
            "limit": self.limit,
            "lasttime":self.lasttime
        }
        return self.data

    def ranstr(self,num):
        salt = ''.join(random.sample(string.ascii_uppercase + string.digits, num))
        return salt

    def ranlong(self,num):
        salt = ''.join(random.sample(string.digits, num))
        return salt

    def phoneNORandomGenerator(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

    def toJson(self):
        return json.dumps(self,default=lambda o:o.__dict__,sort_keys=True,indent=4)


