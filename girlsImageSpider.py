
#!user/bin/env python
#encoding = utf8 
import os
import time
from bs4 import BeautifulSoup
import urllib
import urllib2
import socket
import shutil
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
socket.setdefaulttimeout(20)




def go(MMUrl):
    
    #shutil.rmtree('girlsImage')
    os.mkdir('girlsImage')
    fileName = os.getcwd() + '\\' + 'girlsImage' + '\\'
    i = 0
    print fileName
    url = MMUrl
    while(1): 
        try:
            
        
    
            message = urllib2.urlopen(url).read()
            soup = BeautifulSoup(message, from_encoding = 'utf-8')
            print url
            if (message):     
                 
                time.sleep(1)          
                imagesUrlTags = soup.findAll('img')
                title = soup.find('h1', attrs = {'class':'title'})
                print title
                print imagesUrlTags
                for imageUrlTag in imagesUrlTags:
                    i = i + 1
                    imageUrl = imageUrlTag.get('src')
                    imageName = fileName + '%d.jpg'%i
                    if (imageUrl == 'http://s.jandan.com/static/img/weixin3.png'):
                        continue
                    print 'обть%d.jpg'%i
                    urllib.urlretrieve(imageUrl, imageName)
                print soup.findAll('a', attrs =  {'class':'previous-comment-page'})
                url = soup.find('a', attrs = {'class':'previous-comment-page'}).get('href')
                url = url[:-9]
                print url
                
        except IOError,e:
            if e.message == socket.timeout:
                print timeout
                continue            
            
MMUrl = 'http://jandan.net/ooxx/page-1366'
go(MMUrl)



