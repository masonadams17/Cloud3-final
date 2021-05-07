
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
        self.tableWidget.setRowCount(0)
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
        rowPosition = 0
        data = []
        #loops through all items and inserts them into the windows listbox
        for items in results:
            game = videoGame(items["Rank"],
                            items["Name"],
                            items["Genre"],
                            items["Platform"],
                            items["Publisher"],
                            8,
                            items["img_url"])   
            
            self.tableWidget.insertRow(rowPosition)
            #sets the row for the current item
            self.tableWidget.setItem(rowPosition, 0, qt.QTableWidgetItem(game.Rank))
            self.tableWidget.setItem(rowPosition, 1, qt.QTableWidgetItem(game.Name))
            self.tableWidget.setItem(rowPosition, 2, qt.QTableWidgetItem(game.Platform))
            #sets next row number
            rowPosition = self.tableWidget.rowCount()
            
        
        
            
    def handleSearch(self):
        print("search button clicked")
        searchEntry = self.searchBar.text()
        
        dbCol = connectDB()
        
        results = dbCol.find({ "$or" : [{"Name":searchEntry},{"Genre":searchEntry},{"platform":searchEntry}]}  )
        self.tableWidget.setRowCount(0)
        rowPosition = 0
        for i in results: 
            game = videoGame(i["Rank"], i["Name"], i["Genre"], i["Platform"], i["Publisher"], 8, i["img_url"])
            
            print(repr(game))
            #Dynamicaly adds new row
            self.tableWidget.insertRow(rowPosition)
            
            #sets the row for the current item
            self.tableWidget.setItem(rowPosition, 0, qt.QTableWidgetItem(game.Rank))
            self.tableWidget.setItem(rowPosition, 1, qt.QTableWidgetItem(game.Name))
            self.tableWidget.setItem(rowPosition, 2, qt.QTableWidgetItem(game.Platform))
            #sets next row number
            rowPosition = self.tableWidget.rowCount()
            
            
            
            
        
            

            
    
        
        
        