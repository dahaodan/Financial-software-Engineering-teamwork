# 导入tushare
import pandas as pd
import tushare as ts
import talib
# 初始化pro接口
pro = ts.pro_api('b0f9b7ffb94292b20a87bcfc758e2659ae06aa9202a27d8d094e1985')

class stock:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def get(self, code):
        df = pro.query('daily', ts_code=code, start_date=self.start, end_date=self.end)
        df = df.reindex(index=df.index[::-1])
        [diff, dea, macd] = talib.MACD(df['close'])
        df = pd.concat([df, diff, dea, macd], axis=1)
        df.rename(columns={0:'diff', 1:'dea', 2:'macd'}, inplace=True)
        ret = pd.concat([df['trade_date'], df['open'], df['close'],
                df['high'], df['low'], df['vol'], df['macd'], df['diff'], df['dea']], axis=1)
        ret.reset_index(drop=True, inplace=True)
        return ret
        