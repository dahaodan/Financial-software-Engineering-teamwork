import json
from tornado.escape import json_encode
from .conn import Connection
from .base import BaseHandler
import re


class UserinfoHandler(BaseHandler):
    def post(self):
        try:
            dt1 = json.loads(self.request.body)
            type = dt1['type']
            if type == 'username':
                oldusername = dt1['oldusername']
                newusername = dt1['newusername']
                conn = Connection().conn
                csl = conn.cursor()
                csl.execute(
                    "select * from users where username='{}'".format(newusername))
                getfromdb = csl.fetchall()
                if len(newusername) < 3 or len(newusername) > 8:
                    self.write(json_encode(
                        {'code': 1000, "auth": 1, "result": "failure", "message": "用户名格式错误"}))
                elif not getfromdb:
                    csl.execute("update users set username='{}' where username='{}'".format(
                        newusername, oldusername))
                    conn.commit()
                    csl.execute("update userstock set username='{}' where username='{}'".format(newusername,oldusername))
                    conn.commit()
                    csl.execute("update record set username='{}' where username='{}'".format(newusername,oldusername))
                    conn.commit()
                    csl.execute(
                        "select * from users where username='{}'".format(newusername))
                    dt = csl.fetchall()
                    self.write(json_encode(
                        {'code': 200, "auth": 0, "result": "success", "message": "修改成功", "username": dt[0][0], "email": dt[0][2], "money": dt[0][3], "profile": dt[0][4]}))
                else:
                    self.write(json_encode(
                        {'code': 1000, "auth": 2, "result": "failure", "message": "用户名已被使用"}))
                csl.close()
                conn.close()
            elif type == 'email':
                username = dt1['username']
                email = dt1['email']
                conn = Connection().conn
                csl = conn.cursor()
                csl.execute(
                    "select * from users where email='{}'".format(email))
                getfromdb = csl.fetchall()
                str = r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$'
                if not re.match(str, email):
                    self.write(json_encode(
                        {'code': 1000, "auth": 1, "result": "failure", "message": "邮箱格式错误"}))
                elif not getfromdb:
                    csl.execute("update users set email='{}' where username='{}'".format(
                        email, username))
                    conn.commit()
                    csl.execute(
                        "select * from users where username='{}'".format(username))
                    dt = csl.fetchall()
                    print(dt)
                    self.write(json_encode(
                        {'code': 200, "auth": 0, "result": "success", "message": "修改成功", "username": dt[0][0], "email": dt[0][2], "money": dt[0][3], "profile": dt[0][4]}))
                else:
                    self.write(json_encode(
                        {'code': 1000, "auth": 2, "result": "failure", "message": "邮箱已被使用"}))
                csl.close()
                conn.close()
            elif type == 'profile':
                username = dt1['username']
                profile = dt1['profile']
                conn = Connection().conn
                csl = conn.cursor()
                csl.execute("update users set profile='{}' where username='{}'".format(
                    profile, username))
                conn.commit()
                csl.execute(
                    "select * from users where username='{}'".format(username))
                dt = csl.fetchall()
                self.write(json_encode(
                    {'code': 200, "auth": 0, "result": "success", "message": "修改成功", "username": dt[0][0], "email": dt[0][2], "money": dt[0][3], "profile": dt[0][4]}))
                csl.close()
                conn.close()
            elif type == 'money':
                username = dt1['username']
                money = dt1['money']
                conn = Connection().conn
                csl = conn.cursor()
                if money.isdigit():
                    money = int(money)
                    csl.execute(
                        "update users set money=money+{} where username='{}'".format(money, username))
                    conn.commit()
                    csl.execute(
                        "select * from users where username='{}'".format(username))
                    dt = csl.fetchall()
                    self.write(json_encode(
                        {'code': 200, "auth": 0, "result": "success", "message": "充值成功", "username": dt[0][0], "email": dt[0][2], "money": dt[0][3], "profile": dt[0][4]}))

                else:
                    self.write(json_encode(
                        {'code': 1000, "auth": 1, "result": "failure", "message": "充值失败"}))
                csl.close()
                conn.close()
            elif type == 'password':
                username = dt1['username']
                password = dt1['password']
                conn = Connection().conn
                csl = conn.cursor()
                csl.execute("update users set password='{}' where username='{}'".format(
                    password, username))
                conn.commit()
                csl.execute(
                    "select * from users where username='{}'".format(username))
                dt = csl.fetchall()
                self.write(json_encode(
                    {'code': 200, "auth": 0, "result": "success", "message": "修改成功", "username": dt[0][0], "email": dt[0][2], "money": dt[0][3], "profile": dt[0][4]}))
                csl.close()
                conn.close()
        except Exception as e:
            print("无法解析数据", e)
            self.write(json_encode(
                {'code': 1000, "result": "failure", "message": "无法解析数据"}))
