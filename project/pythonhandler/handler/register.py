import json
from tornado.escape import json_encode
from .conn import Connection
from .base import BaseHandler


class RegisterHandler(BaseHandler):
    """
    注册接口
    """

    def post(self):
        # 获取用户注册的用户名，密码和邮箱
        try:
            # axios方法
            data = json.loads(self.request.body)
            username = data['username']
            password = data['password']
            email = data['email']
            print(username, password, email)

            # // 连接数据库 改变相应返回的auth
            # // 注册成功 auth返回值为0
            # // 用户名已被使用 auth返回值为1
            # // 注册邮箱已被使用 auth返回值为2

            conn = Connection().conn
            # conn = pymysql.connect(host='localhost', port=3306, database='trading', user='root', password='zhangyiyao020801',
            #                        charset='utf8')

            csl = conn.cursor()
            csl.execute(
                "select * from users where username='{}' or email='{}'".format(username, email))
            dt = csl.fetchall()
            if not dt:
                csl.execute("INSERT INTO users(username, password, email, money) VALUES ('{}', '{}', '{}', 0);".format(
                    username, password, email))
                conn.commit()
                self.write(json_encode(
                    {'code': 200, "auth": 0, "result": "success", "message": "注册成功"}))
            else:
                csl.execute(
                    "select * from users where username='{}'".format(username))
                dt2 = csl.fetchall()
                if dt2:
                    self.write(json_encode(
                        {'code': 200, "auth": 1, "result": "failure", "message": "用户名已被使用"}))
                else:
                    self.write(json_encode(
                        {'code': 200, "auth": 2, "result": "failure", "message": "注册邮箱已被使用"}))
            csl.close()
            conn.close()

        except Exception as e:
            print("无法解析数据", e)
            self.write(json_encode(
                {'code': 1000, "result": "failure", "message": "无法解析数据"}))
