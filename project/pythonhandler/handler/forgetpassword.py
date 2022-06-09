import json
import pymysql
from tornado.escape import json_encode
from .conn import Connection
from .base import BaseHandler

class ForgetpasswordHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            username = data['username']
            email = data['email']
            password = data['password']
            conn = Connection().conn
            csl = conn.cursor()
            csl.execute("select * from users where username='{}' and email='{}'".format(username,email))
            dt=csl.fetchall()
            if dt:
                csl.execute("update users set password='{}' where username='{}'".format(
                        password, username))
                conn.commit()
                self.write(json_encode(
                        {'code': 200, "auth": 0, "message": "修改成功"}))
            else:
                self.write(json_encode(
                        {'code': 200, "auth": 1, "message": "用户名或邮箱错误"}))
            csl.close()
            conn.close()

        except Exception as e:
            print("无法解析数据", e)
            self.write(json_encode(
                {'code': 1000, "result": "failure", "message": "无法解析数据"}))