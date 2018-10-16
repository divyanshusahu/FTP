import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QGridLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

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

        ###### Quit Button
    def createQuitButton(self) :
        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.close)
        self.quit_button.resize(self.quit_button.sizeHint())
        self.quit_button.move(100,200)
        return self.quit_button

        ###### Inputting Username
    def enterUsername(self) :
        self.uname_box = QLineEdit('Username', self)
        self.uname_box.move(20, 20)
        self.uname_box.resize(280,40)
        username = self.uname_box.text()
        return self.uname_box

        ###### Inputting Password
    def enterPassword(self) :
        self.pwd_box = QLineEdit('Password', self)
        self.pwd_box.move(20, 80)
        self.pwd_box.resize(280,40)
        password = self.pwd_box.text()
        return self.pwd_box

        ###### Login Button
    def createLoginButton(self) :
        self.login_button = QPushButton('Login',self)
        self.login_button.move(20, 120)
        self.login_button.clicked.connect(self.on_login)
        return self.login_button

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        quit_button = self.createQuitButton()
        login_button = self.createLoginButton()
        uname_box = self.enterUsername()
        pwd_box = self.enterPassword()

        #self.statusBar().showMessage('Message in statusbar.')
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
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginWindow()
    sys.exit(app.exec_())