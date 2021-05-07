
# external imports
from PyQt5 import QtWidgets as qt
from PyQt5 import uic, QtGui
import pip._vendor.requests as requests

#internal imports
from db import connectDB
from model.videoGame import videoGame


class mainWindowController(qt.QMainWindow): 

    def __init__(self):
        super().__init__()
        #loads the view into the controller
        uic.loadUi("src/view/main.ui", self)
        
        #configure the table
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setHorizontalHeaderItem(0, qt.QTableWidgetItem("Rank"))
        self.tableWidget.setHorizontalHeaderItem(1, qt.QTableWidgetItem("Name"))
        self.tableWidget.setHorizontalHeaderItem(2, qt.QTableWidgetItem("Platform"))
        self.searchButton.clicked.connect(self.handleSearch)
        
        #fill the table with rank, name, and image for each videogame
        self.populateTable()
        
        self.show()
        
        
    def populateTable(self):
        
        dbCol = connectDB()
        
        #queries for all games in the database
        results = dbCol.find({})
        
        #sets a iterator
        i = 0
        data = []
        #loops through all items and inserts them into the windows listbox
        for items in results[0:100]:
            game = videoGame(items["Rank"],
                            items["Name"],
                            items["Genre"],
                            items["Platform"],
                            items["Publisher"],
                            8,
                            items["img_url"])   
            
            #sets the row for the current item
            self.tableWidget.setItem(i, 0, qt.QTableWidgetItem(game.Rank))
            self.tableWidget.setItem(i, 1, qt.QTableWidgetItem(game.Name))
            self.tableWidget.setCellWidget(i, 2, qt.QTableWidgetItem(game.Platform))
                    
                
            i+=1
            
    def handleSearch(self):
        print("search button clicked")
        
            
            
            
        
            

            
    
        
        
        