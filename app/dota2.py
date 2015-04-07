# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

import requests
import bs4

class dota2():

	def __init__(self):
		pass

	@staticmethod
	def team_rankings():
		response = requests.get('http://www.gosugamers.net/dota2/rankings#team')
		soup = bs4.BeautifulSoup(response.text)
		ranks = []
		for i in soup.find_all('tr'):
			if int(i.get_text().strip().split('\n\n')[0]) > 15:
				break
			ranks.append("No.%s %s MMR %s"%(i.get_text().strip().split('\n\n')[0],i.get_text().strip().split('\n\n')[1].strip(),i.get_text().strip().split('\n\n')[2]))
		return ranks

