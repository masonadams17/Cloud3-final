import sys
from PyQt5 import QtWidgets, uic
from db import connectDB
from controller.mainWindowController import mainWindowController
from controller.loginWindowController import loginWindowController

#initializes application
app = QtWidgets.QApplication([])

#creates and opens the main window
window = loginWindowController()
window.show()

#listens for app exit and closes python instance
sys.exit(app.exec_()) 