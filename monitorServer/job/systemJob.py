# encoding: utf-8
import psutil
try:
    from decorator import format_data, use_time
    from logger import log
except:
    from monitorServer.decorator import format_data,use_time
    from monitorServer.logger import log


class SystemInfo(object):
    def __init__(self):
        pass

    @use_time
    @format_data
    def get_cpu_info(self)-> list:
        """
        获取cpu 信息
        @return:
        """
        return [psutil.cpu_percent(interval=1)]

    @use_time
    @format_data
    def get_memory(self)->list:
        """
        获取内存信息
        @return:
        """
        mem = psutil.virtual_memory()
        mem_total = round(mem.total / 1024 / 1024 / 1024, 0)
        mem_free = round(mem.free / 1024 / 1024 / 1024)
        mem_percent = mem.percent
        mem_used = round(mem.used / 1024 / 1024 / 1024)
        return [mem_total, mem_free, mem_percent, mem_used]

    @use_time
    @format_data
    def get_disk_used(self)-> list:
        """
        磁盘使用率
        @return:
        """
        disk1 = 0
        disk2 = 0
        disk3 = 0
        disk4 = 0
        disk5 = 0

        # disk1 = str(psutil.disk_usage('C:/').percent) + '%'
        # disk2 = str(psutil.disk_usage('D:/').percent) + '%'
        # disk3 = str(psutil.disk_usage('E:/').percent) + '%'
        # disk4 = str(psutil.disk_usage('F:/').percent) + '%'
        return [disk1, disk2, disk3, disk4, disk5]


class SystemJob(object):
    def __init__(self):
        self.system_obj = SystemInfo()
        pass

    def do(self)-> tuple:
        """"""
        try:
            # cpu信息
            cpu = self.system_obj.get_cpu_info()[0]
            # cpu = psutil.cpu_percent(interval=1, percpu=True)

            # 内存信息
            # mem = psutil.virtual_memory()
            # mem_total = round(mem.total / 1024 / 1024 / 1024, 0)
            # mem_free = round(mem.free / 1024 / 1024 / 1024)
            # mem_percent = str(mem.percent) + '%'
            # mem_used = round(mem.used / 1024 / 1024 / 1024)
            mem_total, mem_free, mem_percent, mem_used = self.system_obj.get_memory()

            # 磁盘信息(磁盘空间使用占比)
            disk1 = str(0) + '%'
            disk2 = str(0) + '%'
            disk3 = str(0) + '%'
            disk4 = str(0) + '%'
            disk5 = str(0) + '%'
            disk1,disk2, disk3, disk4, disk5 = self.system_obj.get_disk_used()

            # disk1 = str(psutil.disk_usage('C:/').percent) + '%'
            # disk2 = str(psutil.disk_usage('D:/').percent) + '%'
            # disk3 = str(psutil.disk_usage('E:/').percent) + '%'
            # disk4 = str(psutil.disk_usage('F:/').percent) + '%'
            # disk5 = str(psutil.disk_usage('G:/').percent) + '%'

            return mem_free, mem_total, mem_percent, mem_used, cpu, disk1, disk2, disk3, disk4, disk5
        except Exception as e:
            log.error("获取服务器数据有问题")
            log.exception(e)

if __name__ == '__main__':
    print('test systemJob file')
    # test system info
    system_info = SystemInfo()
    print('cup info: ', system_info.get_cpu_info())

    # test system job
    system_job = SystemJob()
    res = system_job.do()
    print('do job res', res)
