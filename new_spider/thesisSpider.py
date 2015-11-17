#-*- encoding:utf-8 -*-
#!/usr/bin/python

import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
import threading
import time
import Queue
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def downLoadPage():
	
	pageUrl = pageQueue.get()
	pageHtml = urllib2.urlopen(pageUrl).read()
	pageSoup = BeautifulSoup(pageHtml)
	items = pageSoup.findAll('div', attrs = {'class':'record-item'})
	for item in items:
		
		try:
			thesisName = item.find('a', attrs = {'class':'title'}).text + '.pdf'
			downLoadLink = item.find('a', attrs = {'class':'download'})['href']
			print 'DownLoad',thesisName, downLoadLink,'...'
			html = requests.get(downLoadLink)
			soup = BeautifulSoup(html.content)
			link = 'http://f.wanfangdata.com.cn/' + soup.find(id = 'doDownload')['href']
			urllib.urlretrieve(link, thesisName)
			
		except Exception, e:
			pass


if __name__ == '__main__':
		
	keyWords = sys.argv[1].split('/')
#	keyWords = ['docker']
	pageQueue = Queue.Queue()
	print keyWords
	for keyword in keyWords:
		
		houzui = '%s&f=top' % keyword
		print houzui
		url = 'http://s.wanfangdata.com.cn/Paper.aspx?q=关键词%3A' + houzui 
		html = urllib2.urlopen(url, timeout = 10).read()
		soup = BeautifulSoup(html)
		try:
			pageCount = soup.find('p', attrs = {'class':'pager'}).span.text.split('/')[1]
			for i in range(int(pageCount) + 1):
				pageQueue.put(url + '&p=%i' % i)
				
		except Exception, e:
			print e
			pageQueue.put(url)

	threadCount = 0
	while True:
		
		if pageQueue.empty():
			break
		if pageQueue.qsize() > 5:
			threadCount = 5
		else:
			threadCount = pageQueue.qsize()
		
		for i in range(threadCount):
			pageThread = threading.Thread(target = downLoadPage)
			pageThread.start()
				
		time.sleep(10)

	print 'all over'
	


	
		
	



