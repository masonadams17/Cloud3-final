from PyQt5 import *

from db import connectDB

class editUserWindowController(QtWidgets.QWidget):
    user =""
    
    
    def __init__(self, user):
        super().__init__()
        self.user = user
        
        uic.loadUi("src/view/editUser.ui", self)
        
        self.nameEdit.setText(user.name)
        self.emailEdit.setText(user.email)
        self.usernameEdit.setText(user.username)
        self.passwordEdit.setText(user.password)
        
        self.pushButton.clicked.connect(self.saveChanges)
        
    def saveChanges(self):
        db = connectDB("Users")
        
        db.update_one({
            "username":self.user.username,
            "password":self.user.password
        },
        {
            "$set": {"name": self.nameEdit.text(), "email": self.emailEdit.text(), "username": self.usernameEdit.text(), "password": self.passwordEdit.text()}
        })
        
        
        self.close()