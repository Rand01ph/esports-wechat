# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

from flask import render_template, flash, redirect, request, Flask, g, make_response, redirect
from app import app


from wechat_sdk import WechatBasic

import hashlib
import xml.etree.ElementTree as ET
import time


@app.route('/')
def index():
	return "Hello World!"


@app.route('/weixin', methods=['GET', 'POST'])
def wechat_auth():
	if request.method == 'GET':
		token = 'esportswechat'  # your token
		data = request.args  # GET 方法附上的参数
		signature = data.get('signature', '')
		timestamp = data.get('timestamp', '')
		nonce = data.get('nonce', '')
		echostr = data.get('echostr', '')
		# 加密过程
		#1. 将token、timestamp、nonce三个参数进行字典序排序
		#2. 将三个参数字符串拼接成一个字符串进行sha1加密
		#3. 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
		s = [timestamp, nonce, token]
		s.sort()
		s = ''.join(s)
		if (hashlib.sha1(s).hexdigest() == signature):
			return make_response(echostr)  #返回echostr参数内容，则接入生效

	#post方法:
	#Get the infomations from the recv_xml.
	xml_recv = ET.fromstring(request.data)
	return request.data
