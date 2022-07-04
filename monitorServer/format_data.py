# encoding: utf-8
from db_execute import DbExecute
from tools import strftime


def cpu_info_data():
    """cup Info data"""
    obj = DbExecute()
    print(id(obj))
    cpu_data = obj.select("SELECT TIME,cpu,mem_percent FROM system_info WHERE TIME > DATE_SUB(NOW(), INTERVAL 60 MINUTE)")
    all_time = []
    all_cpu = []
    all_mem_percent = []
    for time_cpu in cpu_data:
        TIME = strftime(time_cpu[0])
        cpu0 = time_cpu[1].split('%')
        cpu_num = eval(cpu0[0])
        mem0 = time_cpu[2].split('%')
        mem_percent = eval(mem0[0])
        all_cpu.append(cpu_num)
        all_time.append(TIME)
        all_mem_percent.append(mem_percent)

    return all_time, all_cpu, all_mem_percent


def memory_used_data():
    """内存使用情况"""
    all_time, all_cpu, all_mem_percent = cpu_info_data()
    return all_time, all_cpu, all_mem_percent


def memory_rank_data():
    """内存使用占比"""
    obj = DbExecute()
    print(id(obj))
    res = obj.select('select mem_free,mem_total,mem_percent,mem_used from system_info order by TIME desc limit 1')
    return [['mem_free', res[0][0]], ['mem_used', res[0][3]]]


if __name__ == '__main__':
    cpu_info_data()

    memory_rank_data()
    print('end')
