# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

from flask import render_template, flash, redirect, request, Flask, g, make_response, redirect
from app import app


import hashlib
import xml.etree.ElementTree as ET
import time

@app.route('/weixin',methods=['GET','POST'])
def wechat_auth():
    if request.method == 'GET':
        token='esportswechat'
        data = request.args
        signature = data.get('signature','')
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')
        s = [timestamp,nonce,token]
        s.sort()
        s = ''.join(s)
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)
    else:
        rec = request.stream.read()
        xml_rec = ET.fromstring(rec)
        tou = xml_rec.find('ToUserName').text
        fromu = xml_rec.find('FromUserName').text


        if  xml_rec.find('EventKey') is None:
            contents = u'谢谢关注'


        return render_template('reply_text.xml',
        toUser = fromu,
        fromUser = tou,
        createtime = str(int(time.time())),
        content = contents
        )
