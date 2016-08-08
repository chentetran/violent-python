'''
Uses mechanize library to get website's source code.
Utilizes http proxy (selected from http://rmmcurdy.com/scripts/proxy/good.txt) for anonymous browsing
'''

import mechanize

def testProxy(url, proxy):
	browser = mechanize.Browser()
	browser.set_proxies(proxy)
	page = browser.open(url)
	source_code = page.read()
	print source_code

url = 'https://www.iplocation.net/find-ip-address'
hideMeProxy = {'http':'110.117.200.206:8118'}
testProxy(url, hideMeProxy)