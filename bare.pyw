
#!/user/bin/env python
#coding:utf-8


import os
import spiderEnerge

url = 'http://tieba.baidu.com/p/3086520715?see_lz=1'

box = spiderEnerge.spiderGroup_attr(url, 'div', {'id':'post_content_51691314318'}, 'text')
                                                 
print box