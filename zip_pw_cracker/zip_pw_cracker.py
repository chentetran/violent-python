import zipfile
from threading import Thread

def extractFile(zFile, pw):
	try:
		zFile.extractall(pwd=pw)
		print '[+] Password is ' + pw
		exit(0)
	except Exception, e:
			pass
			
zFile = zipfile.ZipFile('evil.zip')
pwFile = open('dictionary.txt')

for line in pwFile.readlines():
	pw = line.strip('\n')
	t = Thread(target=extractFile, args=(zFile, pw))
	t.start()