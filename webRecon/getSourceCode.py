'''
Uses Mechanize library to get a website's source code
'''

import mechanize

def viewPage(url):
	browser = mechanize.Browser()
	page = browser.open(url)
	source_code = page.read()
	print source_code

viewPage('https://www.iplocation.net/find-ip-address')