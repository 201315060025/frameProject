#!/usr/bin/env python
from sanic import Sanic
from sanic.response import json, text, html
from feedparser import parse
from jinja2 import Environment, PackageLoader, select_autoescape

import sys

# https://github.com/channelcat/sanic/blob/5bb640ca1706a42a012109dc3d811925d7453217/examples/jinja_example/jinja_example.py
# 开启异步特性  要求3.6+
enable_async = sys.version_info >= (3, 6)
# app = Sanic("ytsbCode")
app = Sanic(name='_src-views')

# jinjia2 config
# env = Environment(
#     loader=PackageLoader('views.rss', '../templates'),
#     autoescape=select_autoescape(['html', 'xml', 'tpl']),
#     enable_async=enable_async)


# async def template(tpl, **kwargs):
#     template = env.get_template(tpl)
#     rendered_template = await template.render_async(**kwargs)
#     return html(rendered_template)


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


@app.route('/intention-recognition-result')
async def intention_recognition_result(request):
    data={'status':200, 'message': 'OK', 'data': {'yi': "正常"}}
    return json(data)
