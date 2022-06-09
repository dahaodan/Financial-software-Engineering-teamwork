import json
import pymysql
from tornado.escape import json_encode
from .conn import Connection
from .base import BaseHandler


class LoginHandler(BaseHandler):
    """
    登录接口
    """

    def post(self):
        # 获取用户登录的用户名和密码
        try:
            # axios方法
            data = json.loads(self.request.body)
            username = data['username']
            password = data['password']
            print(username, password)

            # // 连接数据库 改变相应返回的auth
            # // 登录成功 auth返回值为0
            # // 登录失败 auth返回值为1

            conn = Connection().conn
            # conn = pymysql.connect(host='localhost', port=3306, database='trading', user='root', password='zhangyiyao020801',
            #                        charset='utf8')
            csl = conn.cursor(cursor=pymysql.cursors.DictCursor)

            csl.execute(
                "select * from users where username='{}' and password='{}'".format(username, password))
            dt = csl.fetchall()

            if dt:
                self.write(json_encode({'code': 200, "auth": 0, "result": "success", "message": "登录成功",
                           "username": dt[0]['username'], "email": dt[0]['email'], "money": dt[0]['money'], "profile": dt[0]['profile']}))
            else:
                self.write(json_encode(
                    {'code': 200, "auth": 1, "result": "failure", "message": "用户名和密码不一致"}))
            csl.close()
            conn.close()
        except Exception as e:
            print("无法解析数据", e)
            self.write(json_encode(
                {'code': 1000, "result": "failure", "message": "无法解析数据"}))
