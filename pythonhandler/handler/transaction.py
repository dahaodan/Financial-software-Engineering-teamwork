import json
import pymysql
from tornado.escape import json_encode
from .conn import Connection
from .base import BaseHandler
import efinance as ef
import pandas as pd


class TransactionHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            print(data)
            type = data['type']
            if type == 'init':
                username = data['username']
                conn = Connection().conn
                csl = conn.cursor()
                csl.execute(
                    "select symbol,quant from userstock where username ='{}'".format(username))
                symboldata = csl.fetchall()
                symbollist = []
                quantlist = []
                for i in symboldata:
                    symbollist.append(i[0])
                    quantlist.append(i[1])
                df = ef.stock.get_realtime_quotes()
                totaldata = df.loc[:, ['股票代码', '股票名称', '最新价', '涨跌额', '涨跌幅']]
                data2 = pd.DataFrame()
                for i in symbollist:
                    data1 = totaldata.loc[totaldata['股票代码'] == i]
                    data2 = pd.concat((data2, data1))
                data2 = tuple(tuple(x) for x in data2.values)
                quantlist = tuple(quantlist)

                kchartdata = []
                for i in symbollist:
                    csl.execute(
                        "select name from stockinfo where symbol={}".format(i))
                    name = csl.fetchall()
                    name = name[0][0]
                    if name[0] == '*':
                        name = name[1:]
                    csl.execute("select * from {}".format(name))
                    basicdata = csl.fetchall()
                    kchartdata.append(basicdata)
                kchartdata = tuple(kchartdata)
                self.write(json_encode(
                    {'code': 200, "latestdata": data2, "kchartdata": kchartdata, "quantlist": quantlist}))
            elif type == 'delete':
                username = data['username']
                symbol = data['symbol']
                conn = Connection().conn
                csl = conn.cursor()
                csl.execute("select quant from userstock where username='{}' and symbol={}".format(
                    username, symbol))
                quant = csl.fetchall()
                if quant[0][0] == 0:
                    csl.execute("delete from userstock where username='{}' and symbol='{}'".format(
                        username, symbol))
                    conn.commit()
                    self.write(json_encode(
                        {'code': 200, 'auth': 0, 'message': "取消收藏成功"}))
                else:
                    self.write(json_encode(
                        {'code': 200, 'auth': 1, 'message': "有交易存在无法取消收藏"}))
            elif type == 'transact':
                username = data['username']
                symbol = data['symbol']
                signal = data['transtype']
                vol = data['transvol']
                money = data['money']
                money = float(money)
                if not vol.isdigit():
                    self.write(json_encode(
                        {'code': 200, 'auth': 1, 'message': "交易量格式错误"}))
                else:
                    vol = int(vol)
                    if vol % 100 != 0 or vol >= 100000000:
                        self.write(json_encode(
                            {'code': 200, 'auth': 1, 'message': "交易量格式错误"}))
                    else:
                        df = ef.stock.get_realtime_quotes()
                        totaldata = df.loc[:, ['股票代码', '最新价']]
                        data1 = totaldata.loc[totaldata['股票代码'] == symbol]
                        totalprice = float(data1['最新价'].values) * vol
                        if signal == '1':
                            if money < totalprice:
                                self.write(json_encode(
                                    {'code': 200, 'auth': 3, 'message': "本金不足以购买"}))
                            else:
                                conn = Connection().conn
                                csl = conn.cursor()
                                csl.execute(
                                    "update userstock set quant=quant + {} where username='{}' and symbol='{}'".format(vol, username, symbol))
                                conn.commit()
                                csl.execute("insert into record(username,symbol,vol,type) values('{}','{}',{},'买入')".format(
                                    username, symbol, vol))
                                conn.commit()
                                csl.execute(
                                    "update users set money=money-{} where username='{}'".format(totalprice, username))
                                conn.commit()
                                self.write(json_encode(
                                    {'code': 200, 'auth': 0, 'message': "购买成功", 'money': money-totalprice}))
                                csl.close()
                                conn.close()
                        elif signal == '2':
                            conn = Connection().conn
                            csl = conn.cursor()
                            csl.execute("select quant from userstock where username='{}' and symbol='{}'".format(
                                username, symbol))
                            dtt = csl.fetchall()
                            quant = dtt[0][0]
                            if quant < vol:
                                self.write(json_encode(
                                    {'code': 200, 'auth': 2, 'message': "持有量少于要求卖出量"}))
                            else:
                                csl.execute(
                                    "update userstock set quant=quant - {} where username='{}' and symbol='{}'".format(vol, username, symbol))
                                conn.commit()
                                csl.execute("insert into record(username,symbol,vol,type) values('{}','{}',{},'卖出')".format(
                                    username, symbol, vol))
                                conn.commit()
                                csl.execute(
                                    "update users set money=money+{} where username='{}'".format(totalprice, username))
                                conn.commit()
                                self.write(json_encode(
                                    {'code': 200, 'auth': 0, 'message': "卖出成功", 'money': money+totalprice}))
                                csl.close()
                                conn.close()
            elif type == 'record':
                username=data['username']
                conn = Connection().conn
                csl = conn.cursor()
                csl.execute("select * from record where username = '{}'".format(username))
                dtt=csl.fetchall()
                namelist=[]
                codelist=[]
                for each in dtt:
                    csl.execute("select ts_code,name from stockinfo where symbol = '{}'".format(each[1]))
                    dttt=csl.fetchall()
                    name=dttt[0][1]
                    code=dttt[0][0]
                    namelist.append(name)
                    codelist.append(code)
                namelist=tuple(namelist)
                codelist=tuple(codelist)
                self.write(json_encode(
                                    {'code': 200, 'auth': 0, 'data':dtt,'name':namelist,'code':codelist}))
                csl.close()
                conn.close()
        except Exception as e:
            print("无法解析数据", e)
            self.write(json_encode(
                {'code': 1000, "result": "failure", "message": "无法解析数据"}))
