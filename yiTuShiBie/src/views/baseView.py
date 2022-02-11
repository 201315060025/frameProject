# encoding: utf-8


def op_save_file(file_obj, file_type):
    write_mode, file_path, file_key = ('wb', Config.exePath, 'excelAddress') if file_type == '2' else ('w', Config.txtPath, 'txtAddress')
    filedata = file_obj.get(file_key)
    if filedata:
        # 格式化数据名
        name = "{0}_{1}.{2}".format('.'.join(filedata.name.split('.')[:-1]), str(int(time.time())), filedata.name.split('.')[-1])
        try:

            file_name = os.path.join(file_path, name)
            # 上传文件写入
            with open(file_name, write_mode) as ff:
                ff.write(filedata.body)
        except IOError:
            return 1, '上传文件 失败', ''
        return 0, '上传文件成功, 文件名: {}'.format(file_name), file_name
    else:
        return 1,  '上传文件失败', ''


def send_data(data):
    """"""
    url = Config.url
    data = Config.data
    res = requests.post(url, data=js.dumps(data), headers={})
    if res.status_code == 200:
        return js.loads(res.text)
    return {}


def read_file_data(file_name, file_type):
    """读取数据"""
    if file_name:
        if file_type == '2':
            # 读取exe数据
            pass
        else:
            # 读取txt数据
            pass
    return ''


def read_databse_data(db_config):
    """读取数据库数据"""
    if Config.TEST:
        ip = Config.ip
        user = Config.user
        pwd = Config.pwd
        db_name = Config.db_name
        table_name = Config.table_name
    else:
        ip = db_config.get('ip')
        user = db_config.get('name')
        pwd = db_config.get('pwd')
        db_name = db_config.get('db_name')
        table_name = db_config.get('table_name')

    con = pymysql.connect(host=ip,  # 此处必须是是127.0.0.1
                          port=3306,
                          user=user,  # mysql的登录账号admin
                          password=pwd,  # mysql的登录密码pwd
                          db=db_name,  # mysql中要访问的数据表
                          charset='utf8')  # 表的字符集
    sql = 'select * from {}'.format(table_name)
    rows = c.execute(sql)  # 返回执行成功的结果条数
    print(f'一共有 {rows} 张表')
    for d in c.fetchall():
        for k,v in d.items():
            print(v)
    return []