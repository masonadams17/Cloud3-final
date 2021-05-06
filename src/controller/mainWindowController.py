from PyQt5 import QtWidgets as qt
from PyQt5 import uic
from db import connectDB

class mainWindowController(qt.QMainWindow): 
    
    def __init__(self):
        super().__init__()
        uic.loadUi("src/view/main.ui", self)
        self.populateList()
        self.show()
        
        
    def populateList(self):
        dbCol = connectDB()
        
        #queries for all games in the database
        results = dbCol.find({})
        
        #sets a iterator
        i = 0
        #loops through all items and inserts them into the windows listbox
        for items in results:
            self.listWidget.insertItem(i, items["Name"])
            i+=1
            
    
        
        
        