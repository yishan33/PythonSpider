# -*- coding: UTF-8 -*-
#!/usr/bin/python

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def loginBD():
	
	browser = webdriver.PhantomJS() #success
	browser.set_page_load_timeout(20)   # 防止页面加载个没完
	browser.get('https://passport.baidu.com/v2/?login')
	html_source = browser.page_source
	#print html_source 
	#browser.find_element_by_class_name("js-signin").click()   # 点击登录按钮，一般网站该步可省略
	 
	email = browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__userName"]')
	email.clear()
	email.send_keys("1147925734@qq.com")
	password = browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__password"]')
	password.clear()
	password.send_keys("lfs1129")

	browser.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__submit"]').click()
	#form = browser.find_element_by_xpath("//form[@class='zu-side-login-box']")
	#form.submit()
	 
	somedom = WebDriverWait(browser, 60).until(lambda brow: brow.find_elements_by_class_name("mod-personal-edit"))
	html = browser.page_source
	print html
	browser.quit()
	
def loginSina():
	browser = webdriver.Firefox()
	browser.set_page_load_timeout(20)   # 防止页面加载个没完
	browser.get('http://weibo.com/login.php')
#	html_source = browser.page_source
#	print html_source

	email = browser.find_element_by_name('username')
	email.clear()
	email.send_keys("1147925734@qq.com")
	password = browser.find_element_by_name('password')
	password.clear()
	password.send_keys("lfs1129")

	browser.find_element_by_xpath('//*[@id="pl_login_form"]/div[3]/div[2]/div[6]/a').click()
	somedom = WebDriverWait(browser, 60).until(lambda brow: brow.find_element_by_xpath('//*[@id="plc_top"]'))
	print 'ready to find'
	print browser.find_element_by_xpath('//*[@id="v6_pl_content_homefeed"]/div/div[3]/div[3]').text
	element = browser.find_element_by_xpath('//*[@id="v6_pl_content_homefeed"]/div/div[3]/div[3]').find_element_by_tag_name('img')
	print 'find already'
	print element.get_attribute('src')
#	for img in element:
#		print img.get_attribute('src')
#	elementLink = browser.find_element_by_class_name('bigcursor').get_attribute('src')
#	
#	
#	print elementLink
#	print element.text
	sleep(20)
	browser.quit()
		
def loginRenRen():
	browser = webdriver.PhantomJS() #success
	browser.set_page_load_timeout(20)   # 防止页面加载个没完
	browser.get('http://www.renren.com/')
	somedom = WebDriverWait(browser, 60).until(lambda brow: brow.find_element_by_xpath('//*[@id="pl_login_form"]/div[3]/div[2]/div[6]/a'))
	html_source = browser.page_source
	#print html_source 
	#browser.find_element_by_class_name("js-signin").click()   # 点击登录按钮，一般网站该步可省略
	 
	email = browser.find_element_by_xpath('//*[@id="email"]')
	email.clear()
	email.send_keys("1147925734@qq.com")
	password = browser.find_element_by_xpath('//*[@id="password"]')
	password.clear()
	password.send_keys("liufushan653")

	browser.find_element_by_xpath('//*[@id="login"]').click()
	#form = browser.find_element_by_xpath("//form[@class='zu-side-login-box']")
	#form.submit()
	 
	somedom = WebDriverWait(browser, 60).until(lambda brow: brow.find_elements_by_class_name("mod-personal-edit"))
	html = browser.page_source
	print html
	browser.quit()
	
def loginQQZone():
	
	browser = webdriver.Firefox()
	browser.set_page_load_timeout(30)   # 防止页面加载个没完
	browser.get('http://qzone.qq.com/')
#	browser.switch_to_default_content()
	browser.switch_to_frame(browser.find_element_by_name('login_frame'))
#	html_source = browser.page_source
#	print html_source 
	#browser.find_element_by_class_name("js-signin").click()   # 点击登录按钮，一般网站该步可省略
	
	browser.find_element_by_id('switcher_plogin').click()

	browser.find_element_by_name('u').clear()
	browser.find_element_by_name('u').send_keys("2450824814")
	browser.find_element_by_name('p').clear()
	browser.find_element_by_name('p').send_keys("liufushan653")

	browser.find_element_by_id('login_button').click()
	print 'before', browser.page_source
#	browser.get('http://user.qzone.qq.com/1147925734')
	sleep(1)
	
	browser.get('http://user.qzone.qq.com/2450824814')
	browser.set_page_load_timeout(30)
	print 'get page'
	print browser.page_source
#	browser.set_page_load_timeout(20) 
#	somedom = WebDriverWait(browser, 60).until(lambda brow: brow.find_element_by_xpath('//*[@id="QZ_Toolbar_Container"]/div/div[1]/a[1]/span'))
	print 'now to get target'
	try:
		browser.find_element_by_xpath('//*[@id="QZ_Toolbar_Container"]/div[1]/div[1]/a[1]/span').text
	except Exception, e:
		print e
#	elements = browser.find_elements_by_class_name('item qz_like_btn_v3')
#	print 'elements is ready'
#	for element in elements:
#		element.click()
#		print 'click'
	browser.quit()

def login163():
	browser = webdriver.PhantomJS()  #success
	browser.set_page_load_timeout(20)   # 防止页面加载个没完
	browser.get('http://mail.163.com/')
	html_source = browser.page_source
	print html_source 
	#browser.find_element_by_class_name("js-signin").click()   # 点击登录按钮，一般网站该步可省略
	
	email = browser.find_element_by_xpath('//*[@id="idInput"]')
	email.clear()
	email.send_keys("fsliu33")
	password = browser.find_element_by_xpath('//*[@id="pwdInput"]')
	password.clear()
	password.send_keys("liufushan1129653")

	browser.find_element_by_xpath('//*[@id="loginBtn"]').click()
	#form = browser.find_element_by_xpath("//form[@class='zu-side-login-box']")
	#form.submit()
#	somedom = WebDriverWait(browser, 60).until(lambda brow: brow.find_elements_by_class_name("user-avatar"))
	html = browser.page_source
	print html
	browser.quit()

def loginYuan():
	browser = webdriver.Firefox()  #success
	browser.set_page_load_timeout(40)   # 防止页面加载个没完
	browser.get('http://www.spring4u.info/forumdisplay.php?fid=9')
#	html_source = browser.page_source
#	print html_source 
	#browser.find_element_by_class_name("js-signin").click()   # 点击登录按钮，一般网站该步可省略
	
	email = browser.find_element_by_xpath('/html/body/center/div[1]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/input')
	email.clear()
	email.send_keys("spider33")
	password = browser.find_element_by_xpath('/html/body/center/div[1]/table[2]/tbody/tr[2]/td/form/table/tbody/tr[3]/td[2]/input')
	password.clear()
	password.send_keys("lfs653")
	
	browser.find_element_by_xpath('/html/body/center/div[1]/table[2]/tbody/tr[2]/td/form/center/input').click()
	browser.get('http://www.spring4u.info/index.php')
	#form = browser.find_element_by_xpath("//form[@class='zu-side-login-box']")
	#form.submit()
#	somedom = WebDriverWait(browser, 60).until(lambda brow: brow.find_elements_by_xpath('/html/body/center/div[4]/table/tbody[1]/tr[1]/td/table/tbody/tr/td[1]/a'))
	html = browser.page_source
	print html
	browser.quit()

def loginHepan():
	
	#login
	browser = webdriver.Firefox()  #success
	browser.set_page_load_timeout(40)   # 防止页面加载个没完
	browser.get('http://bbs.uestc.edu.cn/member.php?mod=logging&action=login')
	
	email = browser.find_element_by_name('username')
	email.clear()
	email.send_keys("spider33")
	password = browser.find_element_by_name('password')
	password.clear()
	password.send_keys("lfs653")
	browser.find_element_by_name('loginsubmit').click()
	somedom = WebDriverWait(browser, 60).until(lambda brow: brow.find_elements_by_class_name("vwmy"))
	targetUrl = 'http://bbs.uestc.edu.cn/forum.php?mod=viewthread&tid=1571839&extra=page%3D1'
	browser.get(targetUrl)
	
	#jump to last page
	lastpage = browser.find_element_by_xpath('//*[@id="pgt"]/div/div/a').text
	lastPageUrl = targetUrl + '&page=%s' % lastpage
	
	print '-' * 20
#	browser.find_element_by_tag_name(name)
	#find last reply//*[@id="postnum28059437"]/em
	while True:
		browser.get(lastPageUrl)
		lastReply = browser.find_element_by_xpath('//*[@id="postlistreply"]/preceding-sibling::div[1]/table/tbody/tr/td[2]/div/strong/a/em').text
		print 'now : %s' % lastReply
		if int(lastReply) == 37:
		#write message
			messageBox = browser.find_element_by_name('message')
			messageBox.send_keys('jiu qiang 38~!')
			
			browser.find_element_by_name('replysubmit').click()
			break
		sleep(0.5)
	print 'i get 38!'	
	browser.quit()


#def loginQQCookie():
#	
#	browser = webdriver.Firefox()  #success
#	browser.get
	


#loginRenRen()
#login163()
#loginYuan()
#loginHepan()
loginSina()
#loginQQZone()
