#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from client import *
import login_gui

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

		#### Added event to execute the login_gui script when login button is clicked

		self.button.clicked.connect(self.open_new_window)
		return self.button

	#### Function to run the login_gui script

	def open_new_window(self) :
		login_gui.main()

	def dirLName(self) :

		self.label = QLabel(self)
		self.label.setText("Name")
		self.label.setAlignment(Qt.AlignCenter)

		return self.label

	def dirLMod(self) :

		self.label = QLabel(self)
		self.label.setText("Modified")
		self.label.setAlignment(Qt.AlignCenter)

		return self.label

	def dirLPerm(self) :

		self.label = QLabel(self)
		self.label.setText("Permissions")
		self.label.setAlignment(Qt.AlignCenter)

		return self.label

	def dirLSize(self) :

		self.label = QLabel(self)
		self.label.setText("Size")
		self.label.setAlignment(Qt.AlignCenter)

		return self.label

	def dirLType(self) :

		self.label = QLabel(self)
		self.label.setText("Type")
		self.label.setAlignment(Qt.AlignCenter)

		return self.label

	def showDir(self) :

		self.dirObj = FTPConnect.dirList(self)
		self.labelList = []

		for dirItem in self.dirObj :
			
			filename, fileinfo = dirItem
			curList = []
			
			l1 = QLabel(self)
			l1.setText(filename)
			l1.setAlignment(Qt.AlignCenter)
			curList.append(l1)

			l2 = QLabel(self)
			l2.setText(fileinfo['modify'][:8])
			l2.setAlignment(Qt.AlignCenter)
			curList.append(l2)

			l3 = QLabel(self)
			l3.setText(fileinfo['perm'])
			l3.setAlignment(Qt.AlignCenter)
			curList.append(l3)

			l4 = QLabel(self)
			l4.setText(fileinfo['size'])
			l4.setAlignment(Qt.AlignCenter)
			curList.append(l4)

			l5 = QLabel(self)
			l5.setText(fileinfo['type'])
			l5.setAlignment(Qt.AlignCenter)
			curList.append(l5)

			self.labelList.append(curList)

		return self.labelList


	def initUI(self) :

		FTPConnect()

		grid = QGridLayout()
		grid.setSpacing(2)
		
		grid.addWidget(self.welcomeMsg(),0,3,1,6)
		grid.addWidget(self.loginButton(),0,9,1,3)
		
		# Directory Listing title
		grid.addWidget(self.dirLName(),1,3,1,2)
		grid.addWidget(self.dirLMod(),1,5,1,1)
		grid.addWidget(self.dirLPerm(),1,6,1,1)
		grid.addWidget(self.dirLSize(),1,7,1,1)
		grid.addWidget(self.dirLType(),1,8,1,1)

		# Directory Listing
		cx = 2
		dl = self.showDir()
		for items in dl :
			cy = 3
			for i in items :
				if cy == 3 :
					grid.addWidget(i,cx,cy,cx,2)
					cy += 2
				else :
					grid.addWidget(i,cx,cy,cx,1)
					cy += 1
			cx += 1

		ty, tx = (grid.columnCount(), grid.rowCount())

		grid.addWidget(self.previewBox(),1,9,tx-1,3)
		grid.addWidget(self.createQButton(),tx-1,9,1,3)

		self.setLayout(grid)
		#cy, cx = (grid.columnCount(), grid.rowCount())
		print(grid.rowCount(), grid.columnCount())
		
		# For Window Screen
		self.setGeometry(300,300,1000,600)
		self.setWindowTitle("FTP Server : Logged in as (%s)" % FTPConnect.curUser)
		self.show()

def main() :
	
	app = QApplication([])
	window = MainWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
 	
 	main() 