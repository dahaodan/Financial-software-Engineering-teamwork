import json
import pymysql
from tornado.escape import json_encode
from handler.predict.lstm_predict import lstm_predict
from handler.predict.predict import predict
from .conn import Connection
from .base import BaseHandler
import efinance as ef
import pandas as pd
import numpy as np
from .predict.gru_predict import gru_predict
from .predict.lstm_predict import lstm_predict


class StocknewsHandler(BaseHandler):
    def get(self):
        conn = Connection().conn
        csl = conn.cursor()
        df = ef.stock.get_realtime_quotes()
        data = df.loc[:, ['股票代码', '股票名称', '最新价', '涨跌额', '涨跌幅']]
        a = ['000001', '000002', '000004', '000005', '000006', '000007',
             '000008', '000009', '000010', '000011', '000012', '000014']
        data2 = pd.DataFrame()
        for i in a:
            data1 = data.loc[data['股票代码'] == i]
            data2 = pd.concat((data2, data1))
        data2 = tuple(tuple(x) for x in data2.values)
        kchartdata = []
        for i in a:
            csl.execute("select name from stockinfo where symbol={}".format(i))
            name = csl.fetchall()
            name = name[0][0]
            if name[0] == '*':
                name = name[1:]
            csl.execute("select * from {}".format(name))
            basicdata = csl.fetchall()
            kchartdata.append(basicdata)
        kchartdata = tuple(kchartdata)
        self.write(json_encode(
            {'code': 200, "latestdata": data2, "kchartdata": kchartdata}))

    def post(self):
        try:
            data = json.loads(self.request.body)
            type = data['type']
            if type == 'search':
                info = data['data']
                conn = Connection().conn
                csl = conn.cursor()
                csl.execute(
                    "select name from stockinfo where name like '%{}%' or symbol like '%{}%'".format(info, info))
                dt = csl.fetchall()
                if dt:
                    df = ef.stock.get_realtime_quotes()
                    data1 = df.loc[:, ['股票代码', '股票名称', '最新价', '涨跌额', '涨跌幅']]
                    data3 = pd.DataFrame()
                    kchartdata = []
                    for each in dt:
                        data2 = data1.loc[data1['股票名称'] == each[0]]
                        data3 = pd.concat((data3, data2))
                        if each[0][0] == '*':
                            each[0] = each[0][1:]
                        csl.execute("select * from {}".format(each[0]))
                        basicdata = csl.fetchall()
                        kchartdata.append(basicdata)
                    kchartdata = tuple(kchartdata)
                    data3 = tuple(tuple(x) for x in data3.values)
                    print(data3)

                    self.write(json_encode(
                        {'code': 200, 'auth': 0, "latestdata": data3, "kchartdata": kchartdata}))
                else:
                    self.write(json_encode(
                        {'code': 1000, 'auth': 1, "message": "查无此股票"}))
                csl.close()
                conn.close()
            elif type == 'add':
                symbol = data['symbol']
                username = data['username']
                conn = Connection().conn
                csl = conn.cursor()
                csl.execute(
                    "select * from userstock where username='{}' and symbol='{}'".format(username, symbol))
                dt = csl.fetchall()
                if not dt:
                    csl.execute("insert into userstock(username,symbol,quant) values('{}','{}',0)".format(
                        username, symbol))
                    conn.commit()
                    self.write(json_encode(
                        {'code': 200, 'auth': 0, 'message': "收藏成功"}))
                else:
                    self.write(json_encode(
                        {'code': 1000, 'auth': 1, 'message': "已收藏"}))
                csl.close()
                conn.close()
            elif type == 'predict':
                ways = data['ways']
                days = data['days']
                code = data['code']
                days = int(days)
                if ways == '1':
                    p = gru_predict(code, days)
                    dataset, trainPredict, testPredict = p.model_run()
                    # for each in dataset:
                    #     each[0]=float(each[0])
                    # for each in trainPredict:
                    #     each[0]=float(each[0])
                    # for each in testPredict:
                    #     each[0]=float(each[0])
                    l1 = []
                    l2 = []
                    l3 = []
                    for i in range(len(dataset)):
                        temp = float(dataset[i][0])
                        l1.append(temp)
                    for i in range(len(trainPredict)):
                        temp = float(trainPredict[i][0])
                        l2.append(temp)
                    for i in range(len(testPredict)):
                        temp = float(testPredict[i][0])
                        l3.append(temp)
                    dataset = tuple(l1)
                    trainPredict = tuple(l2)
                    testPredict = tuple(l3)
                    print(dataset)
                    Predict=trainPredict+testPredict
                    predictdata = []
                    predictdata.append(dataset)
                    predictdata.append(Predict)
                    predictdata = tuple(predictdata)
                    self.write(json_encode(
                        {'code': 200, 'auth': 0, 'predictdata': predictdata}))
                else:
                    p = lstm_predict(code, days)
                    dataset, trainPredict, testPredict = p.model_run()
                    l1 = []
                    l2 = []
                    l3 = []
                    for i in range(len(dataset)):
                        temp = float(dataset[i][0])
                        l1.append(temp)
                    for i in range(len(trainPredict)):
                        temp = float(trainPredict[i][0])
                        l2.append(temp)
                    for i in range(len(testPredict)):
                        temp = float(testPredict[i][0])
                        l3.append(temp)
                    dataset = tuple(l1)
                    trainPredict = tuple(l2)
                    testPredict = tuple(l3)
                    print(dataset)
                    Predict=trainPredict+testPredict
                    predictdata = []
                    predictdata.append(dataset)
                    predictdata.append(Predict)
                    predictdata = tuple(predictdata)
                    self.write(json_encode(
                        {'code': 200, 'auth': 0, 'predictdata': predictdata}))

        except Exception as e:
            print("无法解析数据", e)
            self.write(json_encode(
                {'code': 1000, "result": "failure", "message": "无法解析数据"}))
