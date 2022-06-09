import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, LSTM
from sklearn.preprocessing import MinMaxScaler
import time
import os
import datetime
import pymysql


class predict:
    def __init__(self, stknum, predict_time):
        # self.data = pd.read_csv("./data/{}.csv".format(stknum), encoding='gbk')
        conn = pymysql.connect(host='localhost', port=3306, database='trading', user='root', password='zhangyiyao020801',
                               charset='utf8')
        csl = conn.cursor()
        csl.execute("select name from stockinfo where symbol={}".format(stknum))
        name = csl.fetchall()
        name = name[0][0]
        if name[0] == '*':
            name = name[1:]
        csl.execute("select date,close from {}".format(name))
        idata = csl.fetchall()
        date = []
        close = []
        for each in idata:
            b = each[0][0:4]
            c = each[0][4:6]
            d = each[0][6:8]
            t = b+'-'+c+'-'+d
            date.append(t)
            close.append(each[1])
        data1 = {'日期': date,
                 '收盘价': close}
        self.data = pd.DataFrame(data1)
        csl.close()
        conn.close()
        self.dataframe = self.get_data()
        self.pred_time = predict_time
        self.dataset = self.dataframe["收盘价"].values
        self.train_size = min(len(self.dataset), 1000)
        if len(self.dataset) > 1000:
            self.dataset = self.dataset[0: 1000]
        self.model = Sequential()
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.dataset = self.scaler.fit_transform(self.dataset.reshape(-1, 1))
        self.trainX, self.trainY = [], []
        self.look_back = 1

    def get_data(self):
        # dataframe = pd.DataFrame(self.data, columns=['日期', '收盘价'])
        dataframe = self.data
        dataframe['日期'] = pd.to_datetime(dataframe['日期'])
        dataframe.drop(dataframe.index[(dataframe['收盘价'] == 0)], inplace=True)
        return dataframe

    def creat_dataset(self, data):
        """把前look_back天的数据作为后面的预测依据，所以依次把前look_back天作为x，后一天作为y"""
        dataX, dataY = [], []
        for i in range(len(data)-self.look_back):
            a = data[i: (i+self.look_back)]
            dataX.append(a)
            dataY.append(data[i+self.look_back])
        return np.array(dataX), np.array(dataY)

    def data_split(self):
        train = self.dataset[0: self.train_size]
        self.trainX, self.trainY = self.creat_dataset(train)

    def model_structure(self):
        pass

    def model_train(self):
        start = time.time()  # 记录一下模型训练时间
        self.model.compile(loss='mean_squared_error', optimizer='Adam')
        # 打印模型结构信息
        self.model.summary()

        history = self.model.fit(
            self.trainX, self.trainY, batch_size=64, epochs=50, validation_split=0.1, verbose=2)
        print('compilation time:', time.time()-start)

        trainPredict = self.model.predict(self.trainX)
        # testPredict = self.model.predict(self.testX)

        test_x = []
        test_x.append(self.trainY[-self.look_back:])
        test_x = np.array(test_x)
        testPredict = []
        for i in range(self.pred_time):
            new = self.model.predict(test_x)
            new = new.min()
            testPredict.append(new)
            new = np.array(new).reshape(-1, 1)
            test_x = []
            test_x.append(new)
            test_x = np.array(test_x)

        testPredict = np.array(testPredict).reshape(-1, 1)

        testPredict = self.scaler.inverse_transform(testPredict)
        # inverse_transform将数据变换回价格
        trainPredict = self.scaler.inverse_transform(trainPredict)

        dataset = self.scaler.inverse_transform(self.dataset)

        return dataset, trainPredict, testPredict

    def model_run(self):
        self.data_split()
        self.model_structure()
        dataset, trainPredict, testPredict = self.model_train()
        return dataset, trainPredict, testPredict
