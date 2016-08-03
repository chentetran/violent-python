import zipfile
import optparse
from threading import Thread

def extractFile(zFile, pw):
	try:
		zFile.extractall(pwd=pw)
		print '[+] Password is ' + pw
		exit(0)
	except Exception, e:
		pass

parser = optparse.OptionParser('usage%prog -f <zipfile> -d <dictionary>')
parser.add_option('-f', dest='zname', type='string', help='specify zip file')
parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
(options, args) = parser.parse_args()

if (options.zname == None) | (options.dname == None):
	print parser.usage
	exit(0)
else:
	zname = options.zname
	dname = options.dname

	zFile = zipfile.ZipFile(zname)
	pwFile = open(dname)

	for line in pwFile.readlines():
		pw = line.strip('\n')
		t = Thread(target=extractFile, args=(zFile, pw))
		t.start()