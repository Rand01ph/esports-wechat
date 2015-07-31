# -*- coding: utf-8 -*-  

import werobot

robot = werobot.WeRoBot(token='esportswechat')

@robot.text
def hello_world():
    return 'Hello World!'

robot.run()
