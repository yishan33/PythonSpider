#!/usr/bin/python

from fabric.api import local, cd, run, lcd, env, put
from time import sleep


def git(f):
	def dec(commit):
		with lcd(f()):
			local('git add .')
			local('git commit -m %s' % commit)
			local('git push origin master')
		print '*' * 30
		print 'git over'
	
	return dec	

@git		
def gitPython(commitContent = None):
		print 'now to git PythonSpider...'
		return '/Users/ljl/Python_Git/PythonSpider'


@git
def gitTinyTreasure(commitConnect = None):
	print 'now to git tinyTreasure...'
	return '/Users/ljl/Python_Git/tinyTreasure/'
		





