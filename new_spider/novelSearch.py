#-*- encoding:utf-8 -*-
#!/usr/bin/python

import urllib
import urllib2
import Queue
import sys
from BeautifulSoup import BeautifulSoup
from novelSpider import *


class novelGet(object):
	
	searchBaseUrl = 'http://so.23wx.com/cse/search?s=15772447660171623812&entry=1&q='
	def __init__(self, book):
		self.books = book.split('/')
		self.bookUrls = Queue.Queue()
		
	def searchTop(self, bookName):
		bookSearchUrl = self.searchBaseUrl + bookName
		html = urllib2.urlopen(bookSearchUrl).read()
		soup = BeautifulSoup(html)
		bookUrl = soup.find('div', attrs = {'class':'result-game-item-pic'}).a['href']
		return bookUrl
		
		
	def run(self):
		for book in self.books:
			bookUrl = self.searchTop(book)	
			spider_one = novelSpider(book, bookUrl)
			spider_one.run()
		


if __name__ == '__main__':
	
	book = sys.argv[1]
	myNovel = novelGet(book)
	myNovel.run()
	
	
	
	
	
	