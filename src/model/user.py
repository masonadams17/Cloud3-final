
from db import connectDB

class User: 
    
    #class attributes
    name = ""
    email = ""
    username = ""
    password = ""
    
    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        super().__init__()
    
    
    def saveUser(self):
       
        # connects to user database
        db = connectDB("Users")
       
        userDict = {"name" : self.name, "email": self.email, "username":  self.username, "password": self.password}
       
        db.insert_one(userDict)
    
    