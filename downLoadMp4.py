

#!/usr/bin/env python
#coding=utf8
 
import httplib
import urllib
import urllib2
import ssl
 
httpClient = None
 
try:
    httpClient = httplib.HTTPConnection('112.124.120.22', 8080, timeout=30)
    httpClient.request('HEAD', '/welfare/common/company/types.service')
 
    #response «HTTPResponse∂‘œÛ
    response = httpClient.getresponse()
    print response
    print response.status
    print response.reason
    print '1'
     
    backData = response.read()
    if (backData):
        print 'full'
    else:
        print 'empty'
    print backData
    print '2'
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()

