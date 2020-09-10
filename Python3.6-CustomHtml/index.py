#!/usr/bin/env python
# -*- coding:utf-8 -*-

#####----------------------------------------------------------------#####
#####                                                                #####
#####   使用教程/readme:                                              #####
#####   https://cloud.taifucloud.com/document/product/583/32996         #####
#####                                                                #####
#####----------------------------------------------------------------#####

def render_template(html, keys={}):
    for k, v in keys.items():
        html = html.replace("${" + k + "}", v)
    return html

def main_handler(event, context):
    f = open("./demo.html")
    html = f.read()
    keys = {
        "master": "Tencent Serverless Cloud Function Team Top Cloud 雲函數團隊", # Your name. 您的名稱
        "centralCouplet": "年年有餘", # centralCouplet 橫批
        "upCouplet": "千年迎新春", # upCouplet 上聯
        "downCouplet": "瑞雪兆豐年" # downCouplet 下聯
    }
    html = render_template(html, keys)
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'},
        "body": html
    }