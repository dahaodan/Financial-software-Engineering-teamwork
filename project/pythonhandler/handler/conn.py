import pymysql

class Connection:
    def __init__(self, name='zyy'):
        if name == 'zyy':
            self.conn = pymysql.connect(host='localhost', port=3306, database='trading', user='root', password='zhangyiyao020801',
                                   charset='utf8')
        if name == 'gcqw':
            self.conn = pymysql.connect(host='localhost', port=3306, database='trading', user='root', password='111111',
                                   charset='utf8')
        