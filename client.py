from ftplib import FTP

class FTPConnect() :

	welcomeMsg = ''

	def __init__(self) :

		self.initFTP()

	def initFTP(self) :

		ftp = FTP('')
		ftp.connect('127.0.0.1',2121)
		ftp.login('guest','')

		print(ftp.getwelcome())
		FTPConnect.welcomeMsg = ftp.getwelcome()

		ftp.close()