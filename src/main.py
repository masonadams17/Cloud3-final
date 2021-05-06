import sys
from PyQt5 import QtWidgets, uic
from db import connectDB
from controller.mainWindowController import mainWindowController

#initializes application
app = QtWidgets.QApplication([])

#creates and opens the main window
window = mainWindowController()

#listens for app exit and closes python instance
sys.exit(app.exec_()) 