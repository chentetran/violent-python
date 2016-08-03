'''
Takes a file (passwords.txt) of username and password pairs in form of:
	<username1>:<password1>
	<username2>:<password2>
	...

And takes a file of words (dictionary.txt)

For each user-password pair in passwords.txt,
this program checks to see if the password is contained in dictionary.txt
'''

import crypt

def testPass(cryptPass):
	salt = cryptPass[0:2] 	# get salt from pw
	dictFile = open('dictionary.txt', 'r')	# open dictionary

	# for each word in the dictionary, encrypt it and see if match
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word, salt)
		
		if cryptWord == cryptPass:
			print '[+] The password is ' + word
			return

		print '[-] Password not found'
	return 

pwFile = open('passwords.txt', 'r')
for line in pwFile.readlines():
	if ':' in line:
		user = line.split(':')[0]
		cryptPass = line.split(':')[1].strip(' ').strip('\n')
		print '[*] Attempting to crack password for ' + user
		testPass(cryptPass)
