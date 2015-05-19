
#!/usr/bin/env python
import string, urllib2 
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


#定义爬虫引擎

def spider(eachKey, eachUrl):
        
        
        url = eachUrl
        fileName = eachKey + '.txt'
        f = open(fileName, 'w+')  
        print '正在写入' + fileName
        
        while (1):       
               
                html = urllib2.urlopen(url).read()
                soup = BeautifulSoup(html, from_encoding = 'utf-8')
                message = soup.findAll('div', attrs = {'class' : 'info'})
                if (message):
                        if (soup.findAll('link', attrs = {'rel':'next'})):
                                website = soup.findAll('link', attrs = {'rel':'next'})[0].get('href')
                                url = 'http://book.douban.com' + website
                                print url
                        
                        for eachItem in message:
                                if (eachItem.findAll('span', attrs = {'class':'rating_nums'})):
                                        point = eachItem.findAll('span', attrs = {'class':'rating_nums'})[0].string.strip() + ' '
                                bookName = eachItem.findAll('a' )[0].get('title').decode('UTF-8').encode('GB18030') + '---'       
                                publish = eachItem.findAll('div', attrs = {'class':'pub'})[0].string.strip() + '\n'
                                publisher = publish.decode('UTF-8').encode('GB18030')
                        
                            #    print point
                            #    print bookName
                            #    print publisher
                                f.write(point)
                                f.write(bookName)
                                f.write(publisher)
                break                                                      
                                  
        f.close()
                                       
def go(target_list):
        for eachKey in target_list.keys():
                eachUrl = target_list[eachKey]
                spider(eachKey, eachUrl)

def spiderList(url):
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html, from_encoding = 'utf-8')
        tagAll = soup.findAll('ul', attrs = {'class':'clearfix'})
        diction = {}
        for eachItem in tagAll:
                tag = eachItem.findAll('a')
                i = 0
                for eachTag in tag:
                        tag_title = tag[i].string
                        tag_title = tag_title.decode('UTF-8').encode('GB18030')
                        tag_url = 'http://book.douban.com' + tag[i].get('href')
                        tag_url = tag_url.decode('UTF-8').encode('GB18030')
                        print tag_title
                        print tag_url
                        i = i + 1
                        diction[tag_title] = tag_url
        return diction
                        
                 
url = 'http://book.douban.com/'
target_list = spiderList(url)
go(target_list)

