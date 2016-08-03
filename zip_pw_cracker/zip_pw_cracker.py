import zipfile

zFile = zipfile.ZipFile('evil.zip')
pwFile = open('dictionary.txt')

for line in pwFile.readlines():
	pw = line.strip('\n')
	try:
		zFile.extractall(pwd=pw)
		print '[+] Password is ' + pw
		exit(0)
	except Exception, e:
		pass