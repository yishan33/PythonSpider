
#!/user/bin/evn python
#coding : utf-8

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
socket.setdefaulttimeout(30)

def go(image_Url):
    url = image_Url
    fileName = os.getcwd() + '\\' + 'mmpicture' + '\\'
    print fileName
    i = 0
   # shutil.rmtree('mmpicture')
    os.mkdir('mmpicture')
    print '正在从',url,'载入到',fileName
    
    while(1):
        
        try:
           
                    
            time.sleep(1)
            message = urllib2.urlopen(url).read()
            soup = BeautifulSoup(message, from_encoding = 'utf-8')
            if (message):   
                
                print 'i am in'    
                if (soup.findAll('a', attrs = {'target':'_blank'})):
                    imageWebsites = soup.findAll('a', attrs = {'target':'_blank'})
                    nextWebsiteTail = soup.findAll('a', attrs = {'class':'a1'})[2].get('href')
                    url = 'http://www.yjz9.com' + nextWebsiteTail 
                    print url
                    for eachImageWebsite in imageWebsites:
                        if eachImageWebsite:
                            i = i + 1
                            imageUrl = eachImageWebsite.get('href')
                            if (imageUrl == 'http://www.yjz9.com/weixin.html'):
                                continue
                            print imageUrl
                            messageTiny = urllib2.urlopen(imageUrl).read()                            
                            imageName = fileName + 'images%d'%i + '\\'
                            os.mkdir('mmpicture\\images%d'%i) 
                            j = 0
                            lastPage = 'abcd'
                            
                            
                            while (messageTiny):
                                j = j + 1
                                soupTiny = BeautifulSoup(messageTiny, from_encoding = 'utf-8')                                
                                imageTiny = soupTiny.findAll('img', attrs = {'onmouseover':'upNext(this)'})[0].get('src') 
                                imageTinyName = imageName + '%d.jpg'%j
                                print imageTinyName
                                urllib.urlretrieve(imageTiny, imageTinyName) 
                                print imageTiny
                                
                                if (soupTiny.findAll('a', attrs = {'class':'a1'})):
                                    imageNext = soupTiny.findAll('a', attrs = {'class':'a1'})[1].get('href')
                               #     print 'get the next room'
                               
                                    messageTiny = urllib2.urlopen(imageNext).read() 
                                    if (imageNext == lastPage):
                                        break
                                    lastPage = imageNext
                                    print imageNext
                               
                                    
                                    
                                    
                    #       addName = imageUrl[45:]
                      #     print addName
                       #    imageName = fileName + addName
                            time.sleep(1)
                            print '下载图片%d'%i
                            if (imageUrl == '/statics/images/yjz/qrcode_weixin120.png'):
                                continue
                    #        urllib.urlretrieve(imageUrl, imageName)
                        else:
                            continue
                            
            else:
                print 'i am out' 
                
        except IOError,e:
            if e.message == socket.timeout:
                print "timeout"
                continue     
                               
                            
image_Url = 'http://www.yjz9.com/tu/qcmn/'
print  image_Url

go(image_Url)

                         
  
                            
            







