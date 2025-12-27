# coding=utf-8

import requests
from lxml import etree

url = 'http://www.spiderbuf.cn/playground/s02'

myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

html = requests.get(url, headers=myheaders).text
print(html)

# 来源：https://spiderbuf.cn/crawler-tutorial/scraper-http-header

# 爬虫练习网站：Spiderbuf