from PyQt5 import *

from model.user import User


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
        db = connectDB("Users")
        
        try:
            results = db.find_one({"username": self.usernameEdit.text(), "password": self.passwordEdit.text()})
        except NameError:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("User not found, Please try again")
            msg.exec_()
            print(NameError)
            return
            
            
        if not results:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("User not found, Please try again")
            msg.exec_()
            
        else :
            from controller.mainWindowController import mainWindowController
            user = User(results["name"], results["email"], results["username"], results["password"])
            self.nextWindow = mainWindowController(user)
            self.nextWindow.show()
            self.close()
            
    
        
        
        
        
        
    def createNewPressed(self):
        from controller.newUserWindowController import newUserWindowController
        self.nextWindow = newUserWindowController()
        self.nextWindow.show()
        self.close()

        