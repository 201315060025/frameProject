# encoding: utf-8
"""
初始化 数据库信息
"""


from monitorServer.db_execute import DbExecute
cursor = DbExecute()

# 创建数据库
sql = """CREATE DATABASE IF NOT EXISTS student"""
cursor.cursor.execute(sql)
cursor.db.commit()


# 修改数据库
cursor.restart_inint_obj('student')

# 创建数据库表
sql="""CREATE TABLE IF NOT EXISTS system_info(
     ID int(8) not null auto_increment COMMENT '序号',
     TIME datetime not null COMMENT '记录时间',
     mem_free VARCHAR (100) NOT NULL COMMENT '可用内存',
     mem_total VARCHAR (100) NOT NULL COMMENT '总内存',
     mem_percent VARCHAR (100) NOT NULL COMMENT '内存百分比',
     mem_used VARCHAR (100) NOT NULL COMMENT '占用内存',
     cpu VARCHAR (100)  COMMENT 'CPU占比',
     disk1 VARCHAR (100)  COMMENT 'C盘使用占比',
     disk2 VARCHAR (100)  COMMENT 'D盘使用占比',
     disk3 VARCHAR (100)  COMMENT 'E盘使用占比',
     disk4 VARCHAR (100)  COMMENT 'F盘使用占比',
     disk5 VARCHAR (100)  COMMENT 'G盘使用占比',
     primary key(ID)
) ENGINE = INNODB DEFAULT CHARSET = utf8 COMMENT = '系统信息监控';
"""
cursor.cursor.execute(sql)
cursor.db.commit()
