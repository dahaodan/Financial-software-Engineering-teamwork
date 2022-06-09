import json
import pymysql
from tornado.escape import json_encode
from .conn import Connection
from .base import BaseHandler


class ResearchHandler(BaseHandler):
    def get(self):
        conn = Connection().conn
        csl = conn.cursor()
        csl.execute(
            "select F1, title, orgSName, publishDate, URL from RESEARCH LIMIT 0,500")
        Research = csl.fetchall()
        self.write(json_encode(
            {'code': 200, "Research": Research}))
        csl.close()
        conn.close()
