from PyQt5 import *

from model.user import User
from controller.mainWindowController import mainWindowController
from controller.newUserWindowController import newUserWindowController
from db import connectDB

class loginWindowController(QtWidgets.QWidget):
    nextWindow=""
    def __init__(self):
        super().__init__()
        
        #Loads screen components from ui file
        uic.loadUi("src/view/login.ui", self)
        
        
        self.loginButton.clicked.connect(self.loginPressed)
        self.createNewButton.clicked.connect(self.createNewPressed)
        
        
    def loginPressed(self):
        print(self.usernameEdit.text())
        print(self.passwordEdit.text())
        
        
        
        
        
    def createNewPressed(self):
        self.nextWindow = newUserWindowController()
        self.nextWindow.show()
        self.close()

        