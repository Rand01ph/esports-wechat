# -*- coding: utf-8 -*-
__author__ = 'Rand01ph'

import requests
import bs4

class LOL():

    def __init__(self):
        pass


    def team_rankings(self):
        response = requests.get('http://www.gosugamers.net/lol/rankings#team')
        soup = bs4.BeautifulSoup(response.text)
        ranks = []
        for i in soup.find_all('tr', limit=15):
            ranks.append("No.%s %s MMR %s\n"%(i.get_text().strip().split('\n\n')[0],i.get_text().strip().split('\n\n')[1].strip(),i.get_text().strip().split('\n\n')[2]))
        return ranks

    def live_matches(self):
        response = requests.get('http://www.gosugamers.net/lol/gosubet')
        soup = bs4.BeautifulSoup(response.text)
        lives = []
        if len(soup.find('h1').parent.find_all('a')) > 0:
            for i in soup.find('h1').parent.find_all('a'):
                if len(i.get_text().strip().split('\n\n')) > 1:
                    lives.append("%s VS %s\n"%(i.get_text().strip().split('\n\n')[0].split('\n')[0], i.get_text().strip().split('\n\n')[1]))
                else:
                    continue
        else:
            lives.append(u"暂时没有正在进行的比赛")
        return lives

    def upcoming_matches(self):
        response = requests.get('http://www.gosugamers.net/lol/gosubet')
        soup = bs4.BeautifulSoup(response.text)
        upcomings = []
        for i in soup.find('h2').parent.find_all('a'):
            if len(i.get_text().strip().split('\n\n')) > 1:
                upcomings.append("%s VS %s\n"%(i.get_text().strip().split('\n\n')[0].split('\n')[0], i.get_text().strip().split('\n\n')[1]))
            else:
                continue
        return upcomings