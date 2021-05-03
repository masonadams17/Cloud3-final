import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel

app = QApplication([])


window = QWidget()
window.setWindowTitle('PyQt5 app')
window.setGeometry(100,100,200,100)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

window.show()

sys.exit(app.exec_())
