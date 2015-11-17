#-*- encoding:utf-8 -*-
#!/usr/bin/python

import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
import json
import Queue
import threading
import os
from time import sleep, time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class tbSpider(object):
	
	def __init__(self, baseUrl = 'http://tieba.baidu.com/p/4129831294'):
		self.baseUrl = baseUrl 
		self.hostBaseUrl = baseUrl + '?see_lz=1'

	def getBasicMessage(self, url):
		
		html = urllib2.urlopen(url, timeout = 10).read()
		soup = BeautifulSoup(html)
		hostIdSign = soup.find(id = 'j_p_postlist').div
		self.className = hostIdSign['class']
		self.hostId = self.getId(str(hostIdSign['data-field']))
		pageBar = soup.find('li', attrs = {'class':'l_reply_num'})
		self.pageCount = int(pageBar.findAll('span')[1].text)
		self.title = soup.find(id = 'j_core_title_wrap').text[:-8]
		
	def getId(self, sign):
		
		Id = json.loads(sign)['author']['user_id']
		return Id
		
	def getHostMessages(self, sign):
		message = sign.find('cc').text
		return message
	
	def getHostItems(self):
		start = time()
		pageUrlQueue = Queue.Queue()
		successQueue = Queue.Queue()	
		self.getBasicMessage(self.hostBaseUrl)
		print self.title
		for i in range(self.pageCount):
			url = self.hostBaseUrl + '&pn=%i' % (i + 1)
			pageUrlQueue.put(url)
		def downLoadPage():
			pageUrl = pageUrlQueue.get()
			filename = 'tbFiles/' + pageUrl.split('=')[-1] + '.txt'
			fp = file(filename, 'w+')
			while True:
				try:
					
					start = time()
					html = urllib2.urlopen(pageUrl, timeout = 30).read()
					soup = BeautifulSoup(html)
					items = soup.findAll('cc')
					for item in items:
						fp.write(item.text)
						fp.write('\n')
					fp.close()
					end = time()
					print pageUrl, 'use %i seconds' % (end - start)
					successQueue.put(pageUrl)
					break
				except Exception, e:
					print e, pageUrl
					pass
		
		while True:
			
			if not pageUrlQueue.empty():
				for i in range(60):
					thread = threading.Thread(target = downLoadPage)
					thread.start()
				sleep(15)
			else:
				sleep(2)
			if successQueue.qsize() == self.pageCount:
				mainFileName = 'tbFiles/' + self.title + '.txt'
				fp_main = file(mainFileName, 'w+')
				for i in range(self.pageCount):
					filename = 'tbFiles/%i.txt' % (i + 1) 
					fp_read = file(filename, 'r+')
					for line in fp_read:
						fp_main.write(line)
					fp_main.write('------------------------------------\n')
					os.remove(filename)	
				fp_main.close()
				break
			
		end = time()
		print self.title, 'is ok!', 'use %i seconds' % (end - start)
		sys.exit(0)
		
		
			
	def getAllItems(self):
		
		start = time()
		pageUrlQueue = Queue.Queue()
		successQueue = Queue.Queue()
		self.getBasicMessage(self.baseUrl)
		print self.title
		for i in range(self.pageCount):
			url = self.baseUrl + '?pn=%i' % (i + 1)
			pageUrlQueue.put(url)
			
		def downLoadPage():
			
			pageUrl = pageUrlQueue.get()
			filename = 'tbFiles/' + pageUrl.split('=')[-1] + '.txt'
			fp = file(filename, 'w+')
			while True:
				try:
					
					start = time()
					html = urllib2.urlopen(pageUrl, timeout = 30).read()
					soup = BeautifulSoup(html)
					items = soup.findAll('div', attrs = {'class':self.className})
					for item in items:
						if self.getId(str(item['data-field'])) == self.hostId:
							fp.write(self.getHostMessages(item))
					fp.close()
					end = time()
					print pageUrl, 'use %i seconds' % (end - start)
					successQueue.put(pageUrl)
					break
				except Exception, e:
					print e, pageUrl
					pass
			
		while True:
			
			if not pageUrlQueue.empty():
				for i in range(60):
					thread = threading.Thread(target = downLoadPage)
					thread.start()
				sleep(15)
			else:
				sleep(2)
			if successQueue.qsize() == self.pageCount:
				mainFileName = 'tbFiles/' + self.title + '.txt'
				fp_main = file(mainFileName, 'w+')
				for i in range(self.pageCount):
					filename = 'tbFiles/%i.txt' % (i + 1) 
					fp_read = file(filename, 'r+')
					for line in fp_read:
						fp_main.write(line)
						fp_main.write('------------------------------------\n')
					os.remove(filename)	
				fp_main.close()
				break
			
		end = time()
		print self.title, 'is ok!', 'use %i seconds' % (end - start)
		sys.exit(0)

	def run(self):
		self.getHostItems()
			
if __name__ == '__main__':
	
	targetUrl = sys.argv[1]
	spider_1 = tbSpider(targetUrl)
	spider_1.run()	


