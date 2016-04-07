# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import re

address = "http://www.wired.com/2015/10/how-to-switch-android-ios/"

response = urllib2.urlopen(address)
soup = BeautifulSoup(response,"lxml")
paragraphs = soup.find('article').find_all('p')

for paragraph in paragraphs:
	print paragraph.text

# with open('article.txt', 'w') as article:
#  	for line in text:
#  		article.write(str(line))
