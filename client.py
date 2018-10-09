#!/usr/bin/python3

from ftplib import FTP

class FTPConnect :

	welcomeMsg = ''
	curUser = ''
	ftp = FTP('')
	ftp.connect('127.0.0.1', 2121)

	def __init__(self) :

		self.login('guest','')

	def login(self, username, password) :

		FTPConnect.ftp.login(username,password)
		FTPConnect.curUser = username
		FTPConnect.welcomeMsg = FTPConnect.ftp.getwelcome()

	def dirList(self) :

		return FTPConnect.ftp.mlsd()

	def close(self) :

		FTPConnect.ftp.close()