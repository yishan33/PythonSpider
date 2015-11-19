#-*- coding:utf-8 -*-
#!usr/bin/env python

from fabric.api import local, cd, run, lcd, env, put
from time import sleep

def gitPython(commitContent):
	print 'now to git PythonSpider...'
	with lcd('/Users/ljl/Python_Git/PythonSpider/'):
		local('git add .')
		local('git commit -m %s' % commitContent)
		local('git push origin master')
	print '*' * 30	
	print 'git over!'





env.hosts = ['root@139.129.30.127']
env.password = 'lfs1129'
	
def trans():
		
	print 'You connect remote server Successs!'
	remoteDir = toDir 
	remoteTar = remoteDir + fromDir.split('/')[-1]
	put(fromDir, remoteDir)
	with cd(remoteDir):
		run('tar -xvf %s' % remoteTar)
			
	print 'all over....'


	
	

	