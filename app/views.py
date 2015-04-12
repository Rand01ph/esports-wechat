# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

from flask import render_template, flash, redirect, request, Flask, g, make_response, redirect
from app import app
from dota2 import Dota2
from lol import LOL

from wechat_sdk import WechatBasic

import hashlib
import xml.etree.ElementTree as ET
import time


@app.route('/')
def index():
	return "Hello World!"


@app.route('/dota2')
def dotasome():
	dota2 = Dota2()
	ranks = dota2.team_rankings()
	lives = dota2.live_matches()
	upcomings = dota2.upcoming_matches()
	return render_template('dota2.html', ranks=ranks, lives=lives, upcomings=upcomings)


@app.route('/lol')
def lolsome():
	lol = LOL()
	ranks = lol.team_rankings()
	lives = lol.live_matches()
	upcomings = lol.upcoming_matches()
	return render_template('lol.html', ranks=ranks, lives=lives, upcomings=upcomings)



@app.route('/weixin', methods=['GET', 'POST'])
def wechat_auth():

	token = 'esportswechat' # your token

	if request.method == 'GET':
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

	wechat = WechatBasic(token=token)
	wechat.parse_data(request.data)
	message = wechat.get_message()

	response = None

	if message.type == 'subscribe':  # 关注事件(包括普通关注事件和扫描二维码造成的关注事件)
		if message.key and message.ticket:  # 如果 key 和 ticket 均不为空，则是扫描二维码造成的关注事件
			response = wechat.response_text(u'感谢您的关注,输入h查看功能指令')
		else:
			response = wechat.response_text(u'感谢您的关注,输入h查看功能指令')

	elif message.type == 'text':
		if message.content == 'h':
			response = wechat.response_text(u'电竞助手测试版，请输入如下指令：\n'
			                                u'd2tr  返回dota2职业战队排名\n'
			                                u'd2lm 查询正在进行的Dota2比赛\n'
			                                u'd2um 查询即将进行的Dota2比赛\n'
			                                u'loltr  返回LOL职业战队排名\n'
			                                u'lollm 查询正在进行的LOL比赛\n'
			                                u'lolum 查询即将进行的LOL比赛\n')
		elif message.content == 'd2tr':
			dota2 = Dota2()
			ranks = dota2.team_rankings()
			content = ""
			for rank in ranks:
				content += rank
			response = wechat.response_text(content)

		elif message.content == 'd1lm':
			dota2 = Dota2()
			lives = dota2.live_matches()
			content = ""
			for live in lives:
				content += live
			response = wechat.response_text(content)

		elif message.content == 'd1um':
			dota2 = Dota2()
			upcomings = dota2.upcoming_matches()
			content = ""
			for upcoming in upcomings:
				content += upcoming
			response = wechat.response_text(content)

		elif message.content == 'loltr':
			lol = LOL()
			ranks = lol.team_rankings()
			content = ""
			for rank in ranks:
				content += rank
			response = wechat.response_text(content)

		elif message.content == 'lollm':
			lol = LOL()
			lives = lol.live_matches()
			content = ""
			for live in lives:
				content += live
			response = wechat.response_text(content)

		elif message.content == 'lolum':
			lol = LOL()
			upcomings = lol.upcoming_matches()
			content = ""
			for upcoming in upcomings:
				content += upcoming
			response = wechat.response_text(content)


		else:
			response = wechat.response_text(u'您发送的是文字消息')
	elif message.type == 'image':
		response = wechat.response_text(u'您发送的是图片消息')
	else:
		response = wechat.response_text(u'未知消息')

	return response
