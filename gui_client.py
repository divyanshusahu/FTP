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
		self.button.resize(self.button.sizeHint())

		#self.vbox = QVBoxLayout()
		#self.vbox.addStretch(1)
		#self.vbox.addWidget(self.button)
		
		#self.setLayout(self.vbox)
		return self.button

	def welcomeMsg(self) :
		
		self.label = QLabel(self)
		self.label.setText(FTPConnect.welcomeMsg[4:])
		#self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.label.setAlignment(Qt.AlignCenter)

		#self.vbox = QVBoxLayout()
		#self.vbox.addWidget(self.label)
		return self.label

	def previewBox(self) :

		self.label = QLabel(self)
		self.label.setText("Preview")
		self.label.setAlignment(Qt.AlignCenter)

		return self.label

	def loginButton(self) :

		self.button = QPushButton('Login', self)
		self.button.resize(self.button.sizeHint())

		return self.button

	def initUI(self) :

		FTPConnect()

		grid = QGridLayout()
		grid.setSpacing(2)
		
		grid.addWidget(self.welcomeMsg(),0,3,1,6)
		grid.addWidget(self.loginButton(),0,9,1,3)
		grid.addWidget(self.previewBox(),1,9,1,3)
		grid.addWidget(self.createQButton(),2,9,1,3)

		self.setLayout(grid)
		cy, cx = (grid.columnCount(), grid.rowCount())
		
		# For Window Screen
		self.setGeometry(300,300,800,600)
		self.setWindowTitle("FTP Server")
		self.show()

def main() :
	
	app = QApplication([])
	window = MainWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
 	
 	main() 