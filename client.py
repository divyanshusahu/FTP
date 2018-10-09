#!/usr/bin/python3

import sys
from ftplib import FTP
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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

def window() :

	# FTP connection established with guest user
	ftp = FTP('')
	ftp.connect('127.0.0.1',2121)
	ftp.login('guest','')

	# Open the GUI Window
	app = QApplication([])
	app.setStyle('Fusion')

	window = QWidget()
	window.setWindowTitle("FTP Server")
	window.setGeometry(100,100,800,400)
	l1 = QLabel(window)
	l1.setText(ftp.getwelcome()[4:])
	l1.setAlignment(Qt.AlignCenter)

	ftp.retrlines('LIST')
	ftp.close()

	window.show()
	sys.exit(app.exec_())

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

def main() :
	
	app = QApplication([])
	window = MainWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
 	
 	main() 