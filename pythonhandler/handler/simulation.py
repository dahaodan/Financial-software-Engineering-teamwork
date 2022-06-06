import json
import pandas as pd
import pymysql
from tornado.escape import json_encode
from .conn import Connection
from .base import BaseHandler


class SimulationHandler(BaseHandler):
    def post(self):
        try:
            data = json.loads(self.request.body)
            type = data['type']
            if type == 'sample':
                path = './model/{}'.format(data['strategy'])
                df1 = pd.read_excel(path + '/report_info.xlsx')
                data1 = tuple(tuple(x) for x in df1.values)
                df2 = pd.read_excel(path + '/all_risk_analysis.xlsx')
                data2 = tuple(tuple(x) for x in df2.values)
                df3 = pd.read_excel(path + '/scoreic_info.xlsx')
                data3 = tuple(tuple(x) for x in df3.values)
                df4 = pd.read_excel(path + '/group_return.xlsx')
                data4 = tuple(tuple(x) for x in df4.values)
                df5 = pd.read_excel(path + '/pred_autocorr.xlsx')[1:]
                data5 = tuple(tuple(x) for x in df5.values)
                df6 = pd.read_excel(path + '/monthly_ic.xlsx')
                l = []
                j = 0
                for i in range(1, 43):
                    if i % 12 == 0:
                        l.append([j, 11, round(df6.iloc[i, 2], 3)])
                        j += 1
                    else:
                        l.append([j, i%12-1, round(df6.iloc[i, 2], 3)])
                data6 = tuple(tuple(x) for x in l)
                self.write(json_encode(
                    {'code': 200, 'report_info': data1, 'risk_info': data2, 'scoreic_info': data3, 'group_return': data4, 'pred_autocorr': data5, "monthly_ic": data6}))
        except Exception as e:
            print("无法解析数据", e)
            self.write(json_encode(
                {'code': 1000, "result": "failure", "message": "无法解析数据"}))
