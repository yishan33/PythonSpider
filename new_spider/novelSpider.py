#-*- coding:utf-8 -*-
#!/usr/bin/python

import urllib
import urllib2
from time import sleep, time
import Queue
import os
from BeautifulSoup import BeautifulSoup
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class novelSpider(object):
	'''Get the novels from 顶点小说...'''
	def __init__(self, bookName, bookBaseUrl):
		self.bookName = bookName
		self.bookBaseUrl = bookBaseUrl
		self.pageQueue = Queue.Queue()
		self.pageSequence = []
		self.pageSolidList = []
		self.pageIndex = 1
		self.leave = 0
		self.checkSquence = []
		
	def getPages(self):
		
		html = urllib2.urlopen(self.bookBaseUrl).read()
		soup = BeautifulSoup(html)
		chapterTable = soup.find('table', attrs = {'id':'at'})
		chapters = chapterTable.findAll('tr')
		for chapterCombine in chapters:
			for chapter in chapterCombine.findAll('td'):
				a = chapter.find('a')
				try:
					pageUrl = a['href']
					title = a.text
					self.pageQueue.put((title, pageUrl))
					self.pageSequence.append(pageUrl)
					self.pageSolidList.append(pageUrl)
		#			print title, pageUrl	
				except Exception, e:
					print e
					pass
			
		self.checkSequence = (['index.html'] + self.pageSequence)[::100]
		del self.checkSequence[0]
		self.leave = len(self.pageSequence) % 100
		if self.leave == 0:
			pass
		else:
			self.checkSequence.append(self.pageSequence[-1])
	
	def write_to_main(self):
		
		def remove():
			
			if len(self.checkSequence) > 1:
				count = 100
			else:
				count = self.leave
			for i in range(count):
				chaptername = str(self.pageIndex) + '.txt'
				fp_from = file(chaptername, 'r+')
				for line in fp_from:
					self.fp_main.write(line)
				fp_from.close()
				os.remove(chaptername)		
				self.pageIndex += 1
			del self.checkSequence[0]
		
		try:
			if self.pageSolidList.index(self.checkSequence[0]) >= self.pageSolidList.index(self.pageSequence[0]):
				pass
			else:
				remove()
		except Exception, e:
			print e
			remove()
			
		
		
	def run(self):
		
		start = time()
		self.getPages()
		self.fp_main = file(self.bookName, 'a+')
		while self.pageIndex - 1 < len(self.pageSolidList):
			
			self.write_to_main()
			if not self.pageQueue.empty():
				for i in range(120):
					chapterThread = threading.Thread(target = self.downLoadChapter)
					chapterThread.start()
				sleep(15)
			
		self.fp_main.close()
		end = time()
		seconds = end - start
		print 'DownLoad %s Use: %i seconds' % (self.bookName, seconds)
				
			
	def downLoadChapter(self):
		
		title, pageUrl = self.pageQueue.get()
		chapterName = str(self.pageSolidList.index(pageUrl) + 1) + '.txt'
		while True:
			
			fp = file(chapterName, 'w+')
			try:
				
				pageGetUrl = self.bookBaseUrl + pageUrl
				html = urllib2.urlopen(pageGetUrl, timeout = 30).read()
				soup = BeautifulSoup(html)
				content = soup.find(id = 'contents').text
				content = content.split('&nbsp;' * 4)
				if len(content) > 1:
					del content[0]
					content[0] = '    ' + content[0]
				newContent = []
				for item in content:
					item = item + '\n'
					newContent.append(item)
				content = '    '.join(newContent)
				fp.write(content)
				print 'download chapter %s ...' % chapterName	
				self.pageSequence.remove(pageUrl)
				break
			
			except Exception, e:
				
				print e
				print '-' * 30
				print 'bad %s %s' % (title, pageUrl) 
				pass
			
			finally:
				fp.close()
			sleep(1)


		

	
				
if __name__ == '__main__':
	bookName = sys.argv[1]
	bookBaseUrl = sys.argv[2]
#	bookName = '吞噬星空'
#	bookBaseUrl = 'http://www.23wx.com/html/0/304/'
	loader = novelSpider(bookName, bookBaseUrl)
	loader.run()
		
		