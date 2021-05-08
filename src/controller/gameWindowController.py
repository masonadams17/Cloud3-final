from PyQt5 import *
import requests


class gameWindowController(QtWidgets.QWidget):
    
    
    def __init__(self, game):
        super().__init__()
        
        uic.loadUi("src/view/game.ui", self)
        
        self.pushButton.clicked.connect(self.closeWindow)
        
        img = QtGui.QImage()
        img.loadFromData(requests.get(game.Img_url).content)
        pixmap = QtGui.QPixmap(img)
        pixmap.scaled(131,141)
        self.cover_art.setPixmap(pixmap)
        self.Name.setText(game.Name)
        self.Publisher.setText(game.Publisher)
        self.genre.setText(game.Genre)
        self.Platform.setText(game.Platform)
        
    def closeWindow(self):
        self.close()
        
    