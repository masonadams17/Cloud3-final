
# external imports
from PyQt5 import QtWidgets as qt
from PyQt5 import uic, QtGui

#internal imports
from db import connectDB
from model.videoGame import videoGame
from controller.gameWindowController import gameWindowController
from controller.loginWindowController import loginWindowController
from controller.editUserWindowController import editUserWindowController

class mainWindowController(qt.QMainWindow): 
    gameList = []
    user =""
    nextWindow = ""
    
    def __init__(self, user, parent=None):
        super().__init__()
        
        self.user = user
        
        #loads the view into the controllerad
        uic.loadUi("src/view/main.ui", self)
        
        self.welcomeLabel.setText("Welcome " + self.user.name + "!")
        # sets up event handlers
        self.searchButton.clicked.connect(self.handleSearch)
        self.listWidget.itemDoubleClicked.connect(self.viewGame)
        self.logoutButton.clicked.connect(self.logout)
        self.editUser.clicked.connect(self.handleEditUser)
        
        #fill the table with rank, name, and image for each videogame
        self.initializeTable()
        
        self.show()
        
        
    def initializeTable(self):
        #queries for all games in the database
        
        dbCol = connectDB("VideoGames")      
    
        results = dbCol.find({})
    
        
        #sets a iterator
        rowPosition = 0
        data = []
        #loops through all items and inserts them into the windows listbox
        for items in results[0:1000]:
            #creates game object
            game = videoGame(items["Rank"],items["Name"], items["Genre"], items["Platform"], items["Publisher"], items["img_url"])   
            
            self.listWidget.addItem(game.Rank + ". " + game.Name + " - " + game.Platform)
            self.gameList.append(game)
            
    def handleSearch(self):
        #retrieves what the user searched
        searchEntry = self.searchBar.text()
        
        #connect to database and search for all 
        db = connectDB("VideoGames")
        results = db.find({ "$text": {"$search":self.searchBar.text()}} )
        
        # set current row posistion and 
        rowPosition = 0
        self.listWidget.clear()
        for i in results: 
            game = videoGame(i["Rank"], i["Name"], i["Genre"], i["Platform"], i["Publisher"], i["img_url"])
            self.listWidget.addItem(game.Rank + ". " + game.Name + " - " + game.Platform)
            
    def viewGame(self):
        selectedGame = self.gameList[self.listWidget.currentRow()]
        self.nexWindow = gameWindowController(selectedGame)
        self.nexWindow.show()
        
    def logout(self):
        self.nexWindow = loginWindowController()
        self.nexWindow.show()
        self.close()
        
    def handleEditUser(self):
        self.nextWindow = editUserWindowController(self.user)
        self.nextWindow.show()
        
            
        
            

            
    
        
        
        