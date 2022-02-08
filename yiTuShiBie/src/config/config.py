#!/usr/bin/env python
import os


class Config():
    """
    Basic config
    """
    # Application config
    TIMEZONE = 'Asia/Shanghai'
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # 文件路径
    txtPath = r"/Users/4paradigm/code/person/fram_project/yiTuShiBie/src/data"
    exePath = r"/Users/4paradigm/code/person/fram_project/yiTuShiBie/src/data"

    # 测试数据
    url = "t"
    data = {
    "requestId": "72f15ad1-19f8-430d-9826-e202ff01212b",
    "accessToken": "mib",
    "requestTime": 0,
    "resultLimit": 1,
    "commonFeatures": {},
    "rawInstances": [
        {
            "id": "1",
            "rawFeatures": {
                "sepal_length": 5,
                "sepal_width": 3,
                "petal_length": 1.6,
                "petal_width": 0.2
            }
        }
    ],
    "isDebug": False,
    "isWarmupRequest": False
    }

    TEST = True
    ip = ""
    user = ''
    pwd = ""
    db_name = 'student'
    table_name = ''
