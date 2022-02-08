#!/usr/bin/env python
import json as js,os, requests, time

from sanic import Sanic,request
from sanic.response import json, text, html
from feedparser import parse
from jinja2 import Environment, PackageLoader, select_autoescape
import sys
from src.config.config import Config

# 开启异步特性  要求3.6+
enable_async = sys.version_info >= (3, 6)
# app = Sanic("ytsbCode")
app = Sanic(name='_src-views')


@app.route('/test')
def test_api(request):
    return json({'status': 200, 'message': "success", 'data': None})


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







@app.route("/")
async def index(request):
    url = "http://blog.howie6879.cn/atom.xml"
    feed = parse(url)
    articles = feed['entries']
    data = []
    for article in articles:
        data.append({"title": article["title_detail"]["value"], "link": article["link"]})
    return json(data)


@app.route("/html")
async def rss_html(request):
    url = "http://blog.howie6879.cn/atom.xml"
    feed = parse(url)
    articles = feed['entries']
    data = []
    for article in articles:
        data.append({
            "title": article["title_detail"]["value"],
            "link": article["link"],
            "published": article["published"]
        })
    return await template('rss.html', articles=data)


@app.route('/intention-recognition-result', methods=['POST'])
async def intention_recognition_result(request):
    pars = dict(request.form)
    # <editor-fold des="数据校验">
    if 'modelType' not in pars:
    # if 'modelType' not in pars or pars['modelType'][0] != 3:
        return {'status':401, 'message': "参数错误", 'data': None}
    if 'modelWeight' not in pars or 'ruleWeight' not in pars or 'dataSourceType' not in pars:
        return {'status': 401, 'message': "参数错误", 'data': None}
    if pars.get('dataSourceType') and pars['dataSourceType'][0] == '3' and 'ip' not in pars and 'name' not in pars and 'pwd' not in pars:
        # 校验数据库
        return {'status': 401, 'message': "参数错误", 'data': None}



    modelWeight, ruleWeight = pars['modelWeight'][0], pars['ruleWeight'][0]
    modelType, modelWeight, ruleWeight = pars['modelType'][0], pars['modelWeight'][0], pars['ruleWeight'][0]
    dataSourceType = pars['dataSourceType'][0]

    # print(request.files)
    if dataSourceType == '2':
        # 保存excel
        save_flag, save_result, file_name = op_save_file(request.files,dataSourceType)
        # 读取excel
        new_data = read_file_data(file_name, '2')
    elif dataSourceType == '1':
        # 保存txt
        save_flag, save_result, file_name = op_save_file(request.files,dataSourceType)
        # 读取txt
        new_data = read_file_data(file_name, '1')
    else:
        # 读取数据库
        new_data = read_databse_data({})
        pass
    # 发送给模型
    message = send_data({})
    data={'status':200, 'message': 'OK', 'data': message}
    return json(data)
