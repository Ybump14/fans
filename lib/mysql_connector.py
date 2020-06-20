# -*- coding: UTF-8 -*-
import mysql.connector
import traceback


class MySql(object):

    def mysql_connect(self):
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="fans",
            auth_plugin='mysql_native_password'
        )
        return db

    def mysql_select(self, sql):
        get_connect = MySql()
        db = get_connect.mysql_connect()
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as e:
            traceback.print_exc()
        finally:
            cursor.close()
            db.close()
            return data

    def mysql_update(self, sql, var):
        get_connect = MySql()
        db = get_connect.mysql_connect()
        try:
            cursor = db.cursor()
            cursor.execute(sql, var)
            db.commit()
            print("更新成功")
        except Exception as e:
            traceback.print_exc()
            db.rollback()
        finally:
            cursor.close()
            db.close()



