'''
TCP Port Scanner

Steps:

1. Input hostname and list of ports to scan
2. Translate hostname into IPv4 internet address
3. Connect to each target address and port
4. Send garbage data and read banner results to determine what service is running on port
'''

import optparse
from socket import *
from threading import *

# Takes target host and (int) port as arguments
# Attempts to create a connection to the target host and port
# If success, prints open port message
def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send('fsociety\r\n')	# Send garbage data
		results = connSkt.recv(100) 	# Response might indicate the application running
		screenLock.acquire()
		print '[+] %d/tcp open' % tgtPort
		print '[+] ' + str(results)
	except:
		screenLock.acquire()
		print '[-] %d/tcp closed' & tgtPort
	finally:
		screenLock.release()
		connSkt.close()

# Takes hostname and target ports as arguments
# First attempts to resolve an IP address 
# Then prints the hostname or IP addr and checks every port using connScan()
def portScan(tgtPort, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve '%s': Unknown host" % tgtHost
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print '[+] Scan results for ' + tgtName[0]
	except:
		print '[+] Scan results for ' + tgtIP
	setdefaulttimeout(1)

	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()

screenLock = Semaphore(value=1)

# Accept hostname and list of ports to scan from user
parser = optparse.OptionParser('usage %prog -H' + '<targethost> -p <targetport>')
parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
parser.add_optio('-p', dest='tgtPort', type='string', help='specify target port')

(options, args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPorts = str(options.tgtPort).split(',')

if (tgtHost == None) | (tgtPorts[0] == None):
	print parser.usage
	exit(0)

portScan(tgtHost, tgtPorts)

