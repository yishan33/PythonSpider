
#!user/bin/env python
#encoding = utf8

import spiderEnerge
import socket
import os
socket.setdefaulttimeout(20)

os.mkdir('bigImage')
imagePath = os.getcwd() + '\\' + 'bigImage' + '\\'
url = spiderEnerge.init()
print url
while(1):
    
    try:
        i = 0
        targets = spiderEnerge.spiderGroup_numOfattr_1(url, 'img', 'src', 'src')
        print targets
        for target in targets:
            if (target == '/statics/images/yjz/qrcode_weixin120.png'):
                continue
            i = i + 1
            imagePlace = imagePath + '%d.jpg'%i
            print 'обть%d.jpg'%i
            spiderEnerge.downLoad(target, imagePlace)
        
    except IOError,e:
        if e.message == socket.timeout:            
            print 'timeout'
            continue


