#!/usr/bin/python2

from ftplib import FTP

def uploadFile() :
	filename = 'testfile.txt'
	ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
	ftp.quit()

def downloadFile() :
	filename = 'testfile.txt'
	localfile = open(filename, 'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
	ftp.quit()
	localfile.close()

def main() :
	
	# initiate the class object
	ftp = FTP('')

	# connect to the server
	ftp.connect('127.0.0.1', 2121)

	# login guest user
	ftp.login('guest', '')

	# welcome message from the server
	print ftp.getwelcome()

	# print files in the directory
	ftp.retrlines('LIST')

	ftp.close()

if __name__ == '__main__':
 	main() 