
#!user/bin/env python

import os
import time
from bs4 import BeautifulSoup
import sys
import urllib
import urllib2
import shutil
import socket

reload(sys)
sys.setdefaultencoding('utf-8')
socket.setdefaulttimeout(30)


def go(imageUrl):
    
    url = imageUrl
    fileName = os.getcwd() + '\\' + 'ehentaipicture' + '\\'
    print fileName
    i = 0
   # shutil.rmtree('mmpicture')
   # os.mkdir('ehentaipicture')
    print '正在从',url,'载入到'
    print fileName 
    
    while(1):
        try:
      
        
            time.sleep(1)
            print 'i want in 1'
            message = urllib2.urlopen(url).read()
            soup = BeautifulSoup(message, from_encoding = 'utf-8')
            print 'i want in'
            if (message):
                if (soup.findAll('a', href = True, onmouseover = True)):
                    print 'message is ok'
                    imagesWebsites = soup.findAll('a', href = True, onmouseover = True);
                    for imagesWebsite in imagesWebsites:
                        print 'imagesWebsite is ok'
                        imagesUrl = imagesWebsite.get('href')
                        print imagesUrl
                        messageTiny = urllib2.urlopen(imagesUrl).read()
                        soupTiny = BeautifulSoup(messageTiny, from_encoding = 'utf-8')
                        if (messageTiny):
                            print 'messageTiny is ok'
                            if (soupTiny.findAll(style = lambda(value): value and len(value) > 45)):
                                print 'images_Url is ok'
                                images_Url = soupTiny.findAll('div', style = True)                                
                                print images_Url
                            
                    
            
            
        
    
    
    


        except IOError,e:
            
            if e.message == socket.timeout:
                print 'timeout'
                continue
        
        
        
imageUrl = 'http://g.e-hentai.org/?f_doujinshi=0&f_manga=1&f_artistcg=0&f_gamecg=0&f_western=0&f_non-h=0&f_imageset=0&f_cosplay=0&f_asianporn=0&f_misc=0&f_search=chinese&f_apply=Apply+Filter'
go(imageUrl)





