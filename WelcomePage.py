
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import Mood as Mood

class Welcome(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Welcome to your Virtual Mentor")
        self.button = QPushButton("Press here to begin")
        self.text = QLabel("Welcome to your Virtual Mentor")
        self.text.setStyleSheet("color: white")
        self.text.setAlignment(Qt.AlignCenter)
        
        #self.button.setStyleSheet("text-color: mediumslateblue")

        self.button.setStyleSheet("background-color: lemonchiffon")
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.nextpage)
        
    def nextpage(self):
        #self.text.setText('Ready to go!')
        #self.window = QMainWindow()
        self.dialog = Mood.Mood()
        #self.windows.append(dialog)
        #self.ui.setupUi(self.window)
        self.dialog.show()
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = Welcome()
    widget.setStyleSheet("background-color: mediumslateblue")
    widget.showFullScreen()

    sys.exit(app.exec_())
        

        
    