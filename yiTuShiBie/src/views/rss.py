#!/usr/bin/env python
import json as js,os, requests, time

from sanic import Sanic,request
from sanic.response import json, text, html
from feedparser import parse
from jinja2 import Environment, PackageLoader, select_autoescape
import sys
from src.config.config import Config
from .baseView import *

# 开启异步特性  要求3.6+
enable_async = sys.version_info >= (3, 6)
# app = Sanic("ytsbCode")
app = Sanic(name='_src-views')


@app.route('/test')
def test_api(request):
    return json({'status': 200, 'message': "success", 'data': None})


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
