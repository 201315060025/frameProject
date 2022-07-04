# encoding: utf-8
"""
使用一个京城单独去产生数据
"""

import setproctitle
import os, schedule, time, psutil, errno
from multiprocessing import Process
from job.systemJob import SystemJob
from db_execute import DbExecute
try:
    from logger import log
except:
    from monitorServer.logger import log


class ProcessOpt(object):
    def __init__(self):
        pass

    @classmethod
    def judgeprocess(cls, processname):
        pl = psutil.pids()
        name_list = []
        for pid in pl:
            try:
                name = psutil.Process(pid).name()
            except:
                name = None
            name_list.append(name)
            if name == processname:
                return pid
        return None

    @classmethod
    def pid_exists(cls, pid):
        """Check whether pid exists in the current process table.
        UNIX only.
        """
        if pid < 0:
            return False
        if pid == 0:
            # According to "man 2 kill" PID 0 refers to every process
            # in the process group of the calling process.
            # On certain systems 0 is a valid PID but we have no way
            # to know that in a portable fashion.
            raise ValueError('invalid PID 0')
        try:
            os.kill(pid, 0)
        except OSError as err:
            if err.errno == errno.ESRCH:
                # ESRCH == No such process
                return False
            elif err.errno == errno.EPERM:
                # EPERM clearly means there's a process to deny access to
                return True
            else:
                # According to "man 2 kill" possible error values are
                # (EINVAL, EPERM, ESRCH)
                raise
        else:
            return True



def generate_data():
    """专程是产生数据"""
    cur_data = SystemJob().do()
    if cur_data is False:
        log.error("获取数据有问题")

    insert_res = DbExecute().insert(cur_data)
    if insert_res is False:
        log.error("插入数据错误")


def main():
    schedule.every(0.1).minutes.do(generate_data)
    schedule.run_pending()
    while True:
        schedule.run_pending()
        time.sleep(0.05)


# todo: 进程监控重启

generate_data_pro = Process(target=main, args=(), name='generate_data_process')
generate_data_pro.start()
# 重命名京城名称
setproctitle.setproctitle('proData')





if __name__ == '__main__':
    res = SystemJob().do()
    print(res)

