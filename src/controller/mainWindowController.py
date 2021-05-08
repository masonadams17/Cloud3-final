
# external imports
from PyQt5 import QtWidgets as qt
from PyQt5 import uic, QtGui

#internal imports
from db import connectDB
from model.videoGame import videoGame
from controller.gameWindowController import gameWindowController


class mainWindowController(qt.QMainWindow): 
    gameList = []
    
    nextWindow = ""
    
    def __init__(self, parent=None):
        super().__init__()
        #loads the view into the controllerad
        uic.loadUi("src/view/main.ui", self)
        
        # sets up event handlers
        self.searchButton.clicked.connect(self.handleSearch)
        self.listWidget.itemDoubleClicked.connect(self.viewGame)
        
        
        #fill the table with rank, name, and image for each videogame
        self.initializeTable()
        
        self.show()
        
        
    def initializeTable(self):
        #queries for all games in the database
        try:
            dbCol = connectDB()      
        
            results = dbCol.find({})
        except Exception :
            print("Mongo Query Error")
    
        
        #sets a iterator
        rowPosition = 0
        data = []
        #loops through all items and inserts them into the windows listbox
        for items in results[0:1000]:
            #creates game object
            game = videoGame(items["Rank"],items["Name"], items["Genre"], items["Platform"], items["Publisher"], 8, items["img_url"])   
            
            self.listWidget.addItem(game.Rank + ". " + game.Name + " - " + game.Platform)
            self.gameList.append(game)
            
    def handleSearch(self):
        #retrieves what the user searched
        searchEntry = self.searchBar.text()
        
        dbCol = connectDB()
        results = dbCol.find({ "$or" : [{"Name":searchEntry},{"Genre":searchEntry},{"Platform":searchEntry}]}  )
        rowPosition = 0
        self.listWidget.clear()
        for i in results: 
            game = videoGame(i["Rank"], i["Name"], i["Genre"], i["Platform"], i["Publisher"], 8, i["img_url"])
            self.listWidget.addItem(game.Rank + ". " + game.Name + " - " + game.Platform)
            
    def viewGame(self):
        selectedGame = self.gameList[self.listWidget.currentRow()]
        self.nexWindow = gameWindowController(selectedGame)
        self.nexWindow.show()
            
            
        
            

            
    
        
        
        