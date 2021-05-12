from PyQt5 import *

from model.user import User
from controller.mainWindowController import mainWindowController
class newUserWindowController(QtWidgets.QWidget):
    nextWindow = ""
    def __init__(self):
        super().__init__()
        
        uic.loadUi("src/view/createUser.ui", self)
        
        self.createButton.clicked.connect(self.createUser)
        
    def createUser(self):
        
        if self.passwordEdit.text() != self.rPasswordEdit.text():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Unable to create user: \nPasswords do not match")
            msg.exec_()
        else:  
            newUser = User(self.nameEdit.text(), self.emailEdit.text(), self.usernameEdit.text(), self.passwordEdit.text())
            newUser.saveUser()
            self.nextWindow = mainWindowController(newUser)
            self.nextWindow.show()
            self.close()
            
            
        