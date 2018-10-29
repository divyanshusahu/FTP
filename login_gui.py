import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from getpass import getpass
 
class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'LoginWindow - FTP Tool'
        
        self.left = 100
        self.top = 100
        self.width = 420
        self.height = 300

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

        ###### Username Label
    def usernameLabel(self) :
    	self.unameLabel = QLabel(self)
    	self.unameLabel.setText("Username")
    	self.unameLabel.move(20, 0)

        ###### Inputting Username
    def enterUsername(self) :
        self.uname_box = QLineEdit(self)
        self.uname_box.move(20, 20)
        self.uname_box.resize(280,40)
        username = self.uname_box.text()
        return self.uname_box

        ###### Password Label
    def passwordLabel(self) :
    	self.pwdLabel = QLabel(self)
    	self.pwdLabel.setText("Password")
    	self.pwdLabel.move(20, 80)

        ###### Inputting Password
    def enterPassword(self) :
        self.pwd_box = QLineEdit(self)
        self.pwd_box.setEchoMode(QLineEdit.Password)
        self.pwd_box.move(20, 100)
        self.pwd_box.resize(280,40)
        password = self.pwd_box.text()
        return self.pwd_box

        ###### Login Button
    def createLoginButton(self) :
        self.login_button = QPushButton('Login',self)
        #self.login_button.move(20, 140)
        self.login_button.clicked.connect(self.on_login)
        return self.login_button

        ###### Quit Button
    def createQuitButton(self) :
        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.close)
        self.quit_button.resize(self.quit_button.sizeHint())
        #self.quit_button.move(160,140)
        return self.quit_button

        ###### Layout for Login and Quit Buttons
    def createButtonLayout(self):
    	self.horizontalGroupBox = QGroupBox()
    	self.layout = QHBoxLayout()
    	self.login_button = self.createLoginButton()
    	self.layout.addWidget(self.login_button)
    	self.quit_button = self.createQuitButton()
    	self.layout.addWidget(self.quit_button)
    	self.horizontalGroupBox.setLayout(self.layout)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createButtonLayout()
        #quit_button = self.createQuitButton()
        #login_button = self.createLoginButton()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        uname_box = self.enterUsername()
        pwd_box = self.enterPassword()
        self.usernameLabel()
        self.passwordLabel()
        self.show()
    
    '''
    def createGridLayout(self) :
        layout = QGridLayout()
    '''


    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
    def on_login(self) :
        print('Username is '+ self.uname_box.text())
        self.close()

def main() :
	#app1 = QApplication(sys.argv)
	ex1 = LoginWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
    main()