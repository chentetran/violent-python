# unix_pw_cracker

Usage: Run password_cracker.py in a folder with files dictionary.txt and passwords.txt

Takes a file (passwords.txt) of username and encrypted password pairs in form of:
	<username1>:<encryptedpassword1>
	<username2>:<encryptedpassword2>
	...

And takes a file of words (dictionary.txt)

For each user-password pair in passwords.txt,
this program checks to see if the password is contained in dictionary.txt
