#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#爬贴吧原图
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os
#帖子地址
url = 'http://tieba.baidu.com/p/4448954758'
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'lxml')
#匹配原图标签
pic_list = bs.findAll('img', {'class':'BDE_Image'})
cnt = 1
head_url = 'http://imgsrc.baidu.com/forum/pic/item/'
try:
	os.mkdir(r'./python_download')
except FileExistsError as e:
	pass
for pic in pic_list:
	pic_url = head_url + pic['src'].split('/')[-1]
	with open(os.path.join(r'./python_download', str(cnt)+'.jpg'), 'wb') as fout:
		fout.write(urlopen(pic_url).read())
	cnt += 1
	print(pic_url + ' OK...')
