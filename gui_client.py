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

	def changeColor(self, l, r, g, b, a) :

		# To change background color of the label
		l.setAutoFillBackground(True)
		color = QColor(r,g,b)
		alpha = a
		values = "{r}, {g}, {b}, {a}".format(r = color.red(),
												g = color.green(),
												b = color.blue(),
												a = alpha
												)
		l.setStyleSheet("QLabel { background-color: rgba("+values+");}")

		return l

	def previewBox(self) :

		self.label = QLabel(self)
		self.label.setText("Preview")
		self.label.setAlignment(Qt.AlignCenter)

		self.label = self.changeColor(self.label, 200, 200, 200, 255)

		return self.label

	def loginButton(self) :

		self.button = QPushButton('Login', self)
		self.button.resize(self.button.sizeHint())

		return self.button

	def dirLName(self) :

		self.label = QLabel(self)
		self.label.setText("Name")
		self.label.setAlignment(Qt.AlignCenter)

		self.label = self.changeColor(self.label, 215,215,215,255)

		return self.label

	def dirLMod(self) :

		self.label = QLabel(self)
		self.label.setText("Modified")
		self.label.setAlignment(Qt.AlignCenter)

		self.label = self.changeColor(self.label,215,215,215,255)

		return self.label

	def dirLPerm(self) :

		self.label = QLabel(self)
		self.label.setText("Permissions")
		self.label.setAlignment(Qt.AlignCenter)

		self.label = self.changeColor(self.label, 215,215,215,255)

		return self.label

	def dirLSize(self) :

		self.label = QLabel(self)
		self.label.setText("Size")
		self.label.setAlignment(Qt.AlignCenter)

		self.label = self.changeColor(self.label, 215,215,215,255)

		return self.label

	def dirLType(self) :

		self.label = QLabel(self)
		self.label.setText("Type")
		self.label.setAlignment(Qt.AlignCenter)

		self.label = self.changeColor(self.label, 215,215,215,255)

		return self.label

	def showDir(self) :

		self.dirObj = FTPConnect.dirList(self)
		self.labelList = []

		for dirItem in self.dirObj :
			
			fileinfo = dirItem
			curList = []
			
			l1 = QLabel(self)
			l1.setText(fileinfo['filename'])
			l1.setAlignment(Qt.AlignCenter)
			l1 = self.changeColor(l1, 255,255,255,255)
			curList.append(l1)

			l2 = QLabel(self)
			l2.setText(fileinfo['modify'][:8])
			l2.setAlignment(Qt.AlignCenter)
			l2 = self.changeColor(l2, 255,255,255,255)
			curList.append(l2)

			l3 = QLabel(self)
			l3.setText(fileinfo['perm'])
			l3.setAlignment(Qt.AlignCenter)
			l3 = self.changeColor(l3, 255,255,255,255)
			curList.append(l3)

			l4 = QLabel(self)
			l4.setText(fileinfo['size'])
			l4.setAlignment(Qt.AlignCenter)
			l4 = self.changeColor(l4, 255,255,255,255)
			curList.append(l4)

			l5 = QLabel(self)
			l5.setText(fileinfo['type'])
			l5.setAlignment(Qt.AlignCenter)
			l5 = self.changeColor(l5, 255,255,255,255)
			curList.append(l5)

			self.labelList.append(curList)

		return self.labelList

	def backDirButton(self) :

		self.button = QPushButton('Back', self)
		self.button.resize(self.button.sizeHint())

		return self.button


	def initUI(self) :

		FTPConnect()

		grid = QGridLayout()
		grid.setSpacing(0)
		
		grid.addWidget(self.welcomeMsg(),0,3,2,6)
		grid.addWidget(self.loginButton(),0,11,2,1)
		
		# Directory Listing title
		grid.addWidget(self.dirLName(),2,3,1,2)
		grid.addWidget(self.dirLMod(),2,5,1,1)
		grid.addWidget(self.dirLPerm(),2,6,1,1)
		grid.addWidget(self.dirLSize(),2,7,1,1)
		grid.addWidget(self.dirLType(),2,8,1,1)

		# Directory Listing
		cx = 3
		dl = self.showDir()
		for items in dl :
			cy = 3
			for i in items :
				if cy == 3 :
					grid.addWidget(i,cx,cy,1,2)
					cy += 2
				else :
					grid.addWidget(i,cx,cy,1,1)
					cy += 1
			cx += 1

		ty, tx = (grid.columnCount(), grid.rowCount())
		#print(tx,ty)

		grid.addWidget(self.previewBox(),2,9,tx-2,3)
		grid.addWidget(self.createQButton(),tx,11,2,1)
		grid.addWidget(self.backDirButton(),tx,3,2,1)

		self.setLayout(grid)
		#cy, cx = (grid.columnCount(), grid.rowCount())
		#print(grid.rowCount(), grid.columnCount())
		
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