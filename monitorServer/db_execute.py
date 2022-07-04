# encoding: utf-8
"""
数据库操作
"""
import pymysql
from monitorServer.logger import log
from monitorServer.config import Config
from monitorServer.tools import cur_time

class SingleModel(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


class DbExecute(SingleModel):
    def __init__(self):
        super(DbExecute).__init__()
        self._ip = Config.ip
        self._name = Config.name
        self._pwd = Config.pwd
        self._database = Config.database
        self._table = Config.table
        self.cursor = None
        self.db = None
        self._init_obj()

    def _init_obj(self):
        """声明一个执行者"""
        if self.cursor is None:
            db = pymysql.connect(user=self._name, passwd=self._pwd, db=self._database, host=self._ip)
            cur = db.cursor()
            self.cursor = cur
            self.db = db

    def generate_table(self):
        """生成表"""

        pass

    def restart_inint_obj(self, database):
        db = pymysql.connect(user=self._name, passwd=self._pwd, db=database, host=self._ip)
        cur = db.cursor()
        self.cursor = cur
        self.db = db


    def insert(self, *args)->bool:
        sql = """insert into {}(TIME,mem_free,mem_total,mem_percent,mem_used,cpu,disk1,disk2,disk3,disk4,disk5) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""".format(
            self._table)
        try:
            val = (cur_time(),) + args[0]
            self.cursor.execute(sql, val)
            self.db.commit()
            return True
        except Exception as e:
            log.warning(f"insert data fail and source data = {sql}, {str(e)}")
            log.exception(e)
            self.cursor.close()
            self.db.close()
            return False

    def select(self, sql):
        """查询数据"""
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            log.warning(f"查询数据错误{sql}, {str(e)}")
            log.exception(e)
            self.cursor.close()
            return []



if __name__ == '__main__':
    from job.systemJob import SystemJob
    data = SystemJob().do()
    db_exe = DbExecute()
    res = db_exe.insert(data)
    print(res)