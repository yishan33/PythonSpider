#!user/bin/env python
#encoding = utf8

import os
import urllib
import urllib2
import socket
from bs4 import BeautifulSoup
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
socket.setdefaulttimeout(20)

def init():    
    
    if (os.path.exists(attachedFileName) == False):          
        
        f = open(fileName + '.txt', 'w')
        print 'i am work'
        url = raw_input('Enter the website:')
        f.write(url)
        f.close()
    else:
        f = open(fileName + '.txt', 'r')
        url = f.readline()
        f.close()
    return url
def signalSpider(url, tag, attribute, thing):
    message = urllib2.urlopen(url).read()
    soup = BeautifulSoup(message, from_encoding = 'utf-8')
    print 'in the spider'
    if (message):
        print 'in the message'
        target = soup.find(tag, attrs = attribute).get(thing)
        return target
    
def spiderGroup_attr(url, tag, attribute, thing):
    message = urllib2.urlopen(url).read()
    soup = BeautifulSoup(message, from_encoding = 'utf-8')
    print 'in the spiderGroup'
    if (message):
        box = []
        targets = soup.findAll(tag, attrs = attribute)
        print targets
        time.sleep(1)
        for target in targets:
            print 'in the loop'
            targetTiny = target.get(thing)
            print targetTiny
            box.add(targetTiny)
        return box   
            
def spiderGroup_numOfattr_1(url, tag, attr1, thing):
    
    message = urllib2.urlopen(url).read()
    soup = BeautifulSoup(message, from_encoding = 'utf-8')
    print 'in the spiderGroup'
    if (message):
        
        box = set()
        targets = soup.findAll(tag, attrs = {attr1:True})
        print targets
        for target in targets:   
            time.sleep(1)
            targetTiny = target.get(thing)
            print 'get ' + targetTiny
            box.add(targetTiny)
        return box    





def spiderGroup_numOfattr_1_test(url, tag):
    
    message = urllib2.urlopen(url).read()
    soup = BeautifulSoup(message, from_encoding = 'utf-8')
    print 'in the spiderGroup'
    if (message):
        
        box = set()
        targets = soup.findAll(tag)
        print targets
        for target in targets:   
            time.sleep(1)
            targetTiny = target
            print 'get ',targetTiny
            box.add(targetTiny)
        return box    




    
def spiderGroup_numOfattr_2(url, tag, attr1, attr2, thing):
    
    message = urllib2.urlopen(url).read()
    soup = BeautifulSoup(message, from_encoding = 'utf-8')
    print 'in the spiderGroup'
    if (message):
        
        box = set()
        targets = soup.findAll(tag, attrs = {attr1:True,attr2:True})
        print targets
        time.sleep(1)
        for target in targets:   
            print 'in the loop'
            targetTiny = target.get(thing)
            box.add(targetTiny)
        return box      
        
def downLoad(elementUrl, strogePlace):
    
    urllib.urlretrieve(elementUrl, strogePlace)
    
    

fileName = sys.argv[0][sys.argv[0].rfind(os.sep) + 1:-3]
attachedFileName = sys.argv[0][:-3] + '.txt'

