# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from app import app

app.run(host = '127.0.0.1:9999', debug=True)