#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from client import *

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

class MainWindow(QWidget) :

	def __init__(self) :
		super().__init__()

		self.initUI()

	def closeEvent(self, event) :
		
		replay = QMessageBox.question(self,'Quit',
			"Do you want to close the connection?",
			QMessageBox.Yes | QMessageBox.No,
			QMessageBox.No)

		if replay == QMessageBox.Yes :
			event.accept()
		else :
			event.ignore()

	def createQButton(self) :

		self.button = QPushButton('Quit', self)
		self.button.clicked.connect(self.close)
		#self.button.resize(self.button.sizeHint())

		self.vbox = QVBoxLayout()
		self.vbox.addStretch(1)
		self.vbox.addWidget(self.button)
		
		self.setLayout(self.vbox)

	def initUI(self) :

		self.createQButton()

		self.setGeometry(300,300,800,600)
		self.setWindowTitle("FTP Server")
		self.show()

		FTPConnect()

def main() :
	
	app = QApplication([])
	window = MainWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
 	
 	main() 