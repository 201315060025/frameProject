import time
try:
    from logger import log
except:
    from monitorServer.logger import log

# 转换数据结果的格式
def format_data(func):
    def wrapper(*arg, **kwargs):
        cur_res = func(*arg, **kwargs)
        return [str(round(i, 2)) for i in cur_res]
    return wrapper


def use_time(func):
    def wrapper(*arg, **kwargs):
        _start_time = time.time()
        cur_res = func(*arg, **kwargs)
        log.info(f"{func.__name__} use time {str(time.time()-_start_time)} s")
        return cur_res

    return wrapper
