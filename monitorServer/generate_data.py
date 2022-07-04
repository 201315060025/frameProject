# encoding: utf-8
"""
使用一个京城单独去产生数据
"""


from job.systemJob import SystemJob


def generate_data():
    """专程是产生数据"""
    cur_data = SystemJob.do()
    pass






class schedulerExe(object):
    def __init__(self):
        pass

    def executor(self):
        """"""
        cur_data = SystemJob.do()






if __name__ == '__main__':
    res = SystemJob().do()
    print(res)

