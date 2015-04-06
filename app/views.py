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
		body_text = request.data
		# 加密过程
		#1. 将token、timestamp、nonce三个参数进行字典序排序
		#2. 将三个参数字符串拼接成一个字符串进行sha1加密
		#3. 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
		#s = [timestamp, nonce, token]
		#s.sort()
		#s = ''.join(s)
		#if (hashlib.sha1(s).hexdigest() == signature):
		#	return make_response(echostr)  #返回echostr参数内容，则接入生效

	#post方法:
	#Get the infomations from the recv_xml.
	# 实例化 wechat
	wechat = WechatBasic(token=token)
	# 对签名进行校验
	if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
		# 对 XML 数据进行解析 (必要, 否则不可执行 response_text, response_image 等操作)
		return 'hello'
		wechat.parse_data(body_text)
		# 获得解析结果, message 为 WechatMessage 对象 (wechat_sdk.messages中定义)
		message = wechat.get_message()

		response = None
		if message.type == 'text':
			if message.content == 'wechat':
				response = wechat.response_text(u'^_^')
			else:
				response = wechat.response_text(u'文字')
		elif message.type == 'image':
			response = wechat.response_text(u'图片')
		else:
			response = wechat.response_text(u'未知')

		# 现在直接将 response 变量内容直接作为 HTTP Response 响应微信服务器即可，此处为了演示返回内容，直接将响应进行输出
		return response