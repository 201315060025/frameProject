# encoding: utf-8

from datetime import datetime


def cur_time(is_format: bool = False, fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.now().strftime(format=fmt) if is_format else datetime.now()


def strftime(dt: datetime, fmt="%Y-%m-%d %H:%M:%S"):
    return dt.strftime(fmt)


if __name__ == '__main__':
    print(cur_time())