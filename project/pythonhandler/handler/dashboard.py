import json
import pymysql
from tornado.escape import json_encode
from .conn import Connection
from .base import BaseHandler
from .getstock import stock
import efinance as ef

class DashboardHandler(BaseHandler):
    def get(self):
        conn = Connection().conn
        csl = conn.cursor()
        csl.execute("select * from SSEC")
        SSEC = csl.fetchall()
        csl.execute("select * from GEI")
        GEI = csl.fetchall()
        csl.execute("select * from SZI")
        SZI = csl.fetchall()
        csl.execute("select * from CSI300")
        CSI300 = csl.fetchall()
        csl.execute("select title,URL from RESEARCH where f1>=1 and f1<=15")
        RESEARCH = csl.fetchall()
        self.write(json_encode(
            {'code': 200, "SSEC": SSEC, "SZI": SZI, "GEI": GEI, "CSI300": CSI300, "Research": RESEARCH}))
        csl.close()
        conn.close()
