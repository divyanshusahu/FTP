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

		allF = FTPConnect.ftp.mlsd()
		allDir = []
		remFiles = []
		sortedDir = []

		for items in allF :

			filename, fileinfo = items
			if fileinfo['type'] == 'dir' :
				temp1 = {'filename':filename}
				fileinfo = {**temp1, **fileinfo}
				allDir.append(fileinfo)

			elif fileinfo['type'] != 'dir' :
				temp2 = {'filename':filename}
				fileinfo = {**temp2, **fileinfo}
				remFiles.append(fileinfo)

		#print([*allDir, *remFiles])

		sortedDir = [*allDir, *remFiles]

		#print(sortedDir)
		return sortedDir

	def close(self) :

		FTPConnect.ftp.close()