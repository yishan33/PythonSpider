#!usr/bin/env python

import pickle
import socket
import threading
import Queue
import urllib
import urllib2
from BeautifulSoup import  BeautifulSoup
from time import sleep, time
import logging
import requests
from selenium import webdriver
import cPickle as pickle

logging.basicConfig(level = logging.DEBUG,
                    format = '%(asctime)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename = 'image.log',
                    filemod = 'w'
                    )



def getImagesUrl():

    global imagesQueue
    global pagesQueue
    while True:
        try:
            start = time()
            url = pagesQueue.get()
            request = urllib2.Request(url)
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
            html = urllib2.urlopen(request, timeout = 20).read()
            soup = BeautifulSoup(html)
            end = time()
            seconds = end - start
            print 'useseconds:', seconds
            print 'now:', url
            images = soup.findAll('img')
            print '-' * 20
            for image in images:
                try:
                    src = image['src']
                    if src[-3:] == 'png':
                        continue
                    else:
                        print 'get',

                except KeyError, e:

                    src = image['data-original']

                imagesQueue.put(src)

            sleep(30)
           
        except Exception, e:
        
            print e
            pagesQueue.put(url)
            logging.error(e)
            setAgent()
   
def downLoadImage():

    global imagesQueue
    try:
        imageUrl = imagesQueue.get(False)
        imageName = '/Users/ljl/testPython/Spiders/newImages/' + imageUrl.split('/')[-1]
        print 'downLoad %s ...' % imageName
        try:
            urllib.urlretrieve(imageUrl, filename = imageName)
            sleep(1)
        except Exception, e:

            logging.error(e)
            pass
    except Exception, e:

        logging.error(e)
        pass

def setAgent():
    
    global agentQueue
    global pagesQueue
    try:
        newIp = agentQueue.get()
        ipType = newIp[0]
        host = newIp[1]
        print 'use ip:', newIp
        proxy_support = urllib2.ProxyHandler({
            ipType:host
        })
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        start = time()
        url = pagesQueue.get()
        try:
            request = urllib2.Request(url)
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
        except Exception, e:
            print e
            pagesQueue.put(url)
    except Exception, e:
        
        print e
        logging.error(e)
        pass
            
    

def getAgent():
    
    global agentQueue
    browser = webdriver.PhantomJS()
    fp = file('ipConfirm.txt', 'a+')
    try:
        
        browser.get('http://ip.zdaye.com/?ip=&port=8080&adr=&checktime=&sleep=&cunhuo=&nport=&nadr=&dengji=&https=&yys=&gb=4&px=')
        html_source = browser.page_source
        soup = BeautifulSoup(html_source)
        MainNode = soup.find(id = 'ipc')
        items_tr = MainNode.findAll('tr')
        
        del items_tr[0]
        
        for item in items_tr:
            item_td = item.findAll('td')
        
            ip = item_td[0].text + ':8080'
            is_https_tag = item_td[6].find('div')
            if is_https_tag:
                is_https = 'https'
                
            else :
                is_https = 'http'
            agentQueue.put((is_https, ip))
            print 'get new ip:', ip
            pickle.dump((is_https, ip), fp)

        print '-' * 10 + 'getAgent' + '-' * 10
        sleep(20)
        
        
    except Exception, e:
        
        print e
        pass
        
    finally:
        browser.quit()
        fp.close()

        
        
    
if __name__ == '__main__':

    imagesQueue = Queue.Queue()
    pagesQueue = Queue.LifoQueue()
    for i in range(1068):
        pageUrl = 'http://jandan.net/ooxx/page-%i' % i 
        pagesQueue.put(pageUrl)
    agentQueue = Queue.LifoQueue()
    getAgent()
   
    imageUrlThread = threading.Thread(target = getImagesUrl)
    imageUrlThread.start()
    
    while True:
  
        size = imagesQueue.qsize()
        if  size > 20:
            for i in range(20):
                thread = threading.Thread(target = downLoadImage)
                thread.start()
        else :
            for i in range(size):
                thread = threading.Thread(target = downLoadImage)
                thread.start()
        agentThread = threading.Thread(target = getAgent)
        agentThread.start()
        sleep(15)

















