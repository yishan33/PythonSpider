
#!user/bin/env python 
#coding:utf-8

import requests

r = requests.get('http://www.baidu.com/link?url=QeTRFOS7TuUQRppa0wlTJJr6FfIYI1DJprJukx4Qy0XnsDO_s9baoO8u1wvjxgqN', allow_redirects = False)
print r
print r.status_code