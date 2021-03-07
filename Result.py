#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 23:38:47 2021

@author: antheaml
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 23:16:23 2021

@author: Catherine
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import simpleaudio as sa
#import WelcomePage as WelcomePage

def music(musicfile):
    wave_obj = sa.WaveObject.from_wave_file(musicfile)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    

class Result(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("The action plan - 3 -")
        self.setStyleSheet("background-color: mediumslateblue")
        self.text = QLabel("Since you've indicated you're tired and you have very few tasks to complete, why don't you take some time off?")
        self.text.setStyleSheet("color: white")
        self.text.setAlignment(Qt.AlignCenter)

        self.button = QPushButton(" Click here to listen to some music...")
        self.button.setStyleSheet("background-color: white")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        

        # self.grid = QGridLayout()
        

        # self.grid.addWidget(QLabel("  "),0,0)
        # self.grid.addWidget(self.coltitle1,0,0)
        # self.grid.addWidget(self.coltitle2,0,0)
        # self.grid.addWidget(self.coltitle3,0,0)

        # self.setLayout(self.grid)

        self.button.clicked.connect(self.playmusic)


    def playmusic(self, Prior):
        #Prior.setObjectName("OtherWindow")
        music("ThaiMeditation.wav")


    def nextpage(self):
        #self.text.setText('Ready to go!')
        #self.window = QMainWindow()
        self.dialog = Prior.Prior()
        #self.windows.append(dialog)
        #self.ui.setupUi(self.window)
        self.dialog.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = Prior()
    #widget.setGeometry(0, 0, 1024, 768)
    
    widget.showFullScreen()
    
    sys.exit(app.exec_())
