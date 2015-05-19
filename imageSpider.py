
#!/usr/bin/python

import os
import time
import urllib
import urllib2
import shutil

from bs4 import BeautifulSoup
import sys

import socket
reload(sys)
sys.setdefaultencoding("utf-8")
socket.setdefaulttimeout(20)



def imageSpider(eachKey, eachUrl):
    url = eachUrl
    print url
    i = 0
    fileName = os.getcwd() + '\\'+ eachKey +'image\\'
    print fileName 
 #   shutil.rmtree(eachKey + 'image')
    os.mkdir(eachKey + 'image')
    print '正在下载',eachKey,'到',fileName
    url = douban + '/tag/' + eachKey + '?start=980&type=T'
    
   

    while(1):
        
        try:   
            
            if (url == 'http://book.douban.com' + '/tag/' + eachKey + '?start=1000&type=T'):
                break            
            time.sleep(1)
            message = urllib2.urlopen(url).read()
            soup = BeautifulSoup(message, from_encoding = 'utf-8')
            if (message):
            
                if (soup.findAll('link', attrs = {'rel':'next'})):
                    website = soup.findAll('link', attrs = {'rel':'next'})[0].get('href')
                    url = 'http://book.douban.com' + website  
                    

                if (soup.findAll('img',attrs = {'class':''})):                

                    images = soup.findAll('img',attrs = {'class':''})        
                    for eachImage in images:
                        if eachImage:               
                            socket.setdefaulttimeout(20)
                            i = i + 1
                            imageUrl = eachImage.get('src')
                            imageName = fileName + '%d.jpg'%i
                            time.sleep(1)                            
                            print '下载%d.jpg'%i
                            urllib.urlretrieve(imageUrl, imageName)  
                        else:
                            continue                                                                

        except IOError,e:
            if e.message == socket.timeout:                
                print "timeout"
                continue         

def go(target_list):

        for eachKey in target_list.keys():
                eachUrl = target_list[eachKey]
                imageSpider(eachKey, eachUrl)



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
                        tag_title = tag_title
                        tag_url = 'http://book.douban.com' + tag[i].get('href')
                        tag_url = tag_url
                        print tag_title
                        print tag_url
                        i = i + 1
                        diction[tag_title] = tag_url

        return diction    





url = 'http://book.douban.com/'
douban = url
target_list = spiderList(url)
go(target_list)











