import requests
import time
import json
from case.get_fans import Get_Fan_UserId
from lib.publice_data import Login
from lib.mysql_connector import MySql


class Get_fan_info(object):

    def get_fan_info(self):
        login = Login()
        url = login.get_user_detail_url()
        get_uid = Get_Fan_UserId()
        uidData = get_uid.get_fans()
        i = 0
        limit = 10
        for uid in uidData:
            uid = str(uid)
            r=requests.get(url=url+"?uid="+uid)
            load_data = json.loads(json.dumps(r.json()))
            userid = (load_data["userPoint"]["userId"])
            gender = load_data["profile"]["gender"]
            nickname = load_data["profile"]["nickname"]
            birthday = load_data["profile"]["birthday"]
            city = load_data["profile"]["city"]
            province = load_data["profile"]["province"]
            db = MySql()
            sql = "INSERT INTO `fans`.`fans_info` (`uid`, `nickname`, `birthday`, `province`, `city`, `gender`) VALUES ( %s, %s, %s, %s, %s, %s)"
            var = (userid, nickname, birthday, province, city, gender)
            save = db.mysql_update(sql, var)
            i = i + 1
            print("已插入第%s条数据" % i)
            print("userid=%s" % userid)
            info = [userid, nickname, gender, birthday, city, province]
        return info


run = Get_fan_info()
run.get_fan_info()
