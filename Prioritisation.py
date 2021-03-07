#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 20:07:20 2021

@author: Catherine
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#import WelcomePage as WelcomePage
import Result as Result

class Prior(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("What's on the agenda today? - 2 -")
        self.setStyleSheet("background-color: mediumslateblue")
        self.text = QLabel("What do you want to get done today?")
        self.text.setStyleSheet("color: white")

        self.text.setAlignment(Qt.AlignCenter)

        #self.space = QLabel("  ")
        # self.space.setAlignment(Qt.AlignLeft)
        # self.space.setAlignment(Qt.AlignTop)
        self.task = QLineEdit("Type your task here")
        self.task.setStyleSheet("color: white")

        self.coltitle1 = QLabel("How urgent is this task?")
        self.coltitle1.setStyleSheet("color: white")

        self.slider1 = QSlider(Qt.Horizontal)
        self.urgency = []
        self.slider1value = self.slider1.value()
        self.urgency.append(self.slider1value)
        #self.slider1print = QLabel("Urgency Value")
        
        # self.coltitle1.setAlignment(Qt.AlignLeft)
        # self.coltitle1.setAlignment(Qt.AlignTop)
        self.coltitle2 = QLabel("How important is this task to you?")
        self.coltitle2.setStyleSheet("color: white")
        self.slider2 = QSlider(Qt.Horizontal)
        # self.coltitle2.setAlignment(Qt.AlignCenter)
        # self.coltitle2.setAlignment(Qt.AlignTop)
        self.coltitle3 = QLabel("How long do you anticipate this task taking?")
        self.coltitle3.setStyleSheet("color: white")
        self.slider3 = QSlider(Qt.Horizontal)
        # self.coltitle3.setAlignment(Qt.AlignRight)
        # self.coltitle3.setAlignment(Qt.AlignTop)
        self.newtaskbutton = QPushButton("Input New Task")
        self.newtaskbutton.setStyleSheet("background-color: lemonchiffon")
        self.nextpagebutton = QPushButton("Next Page")
        self.nextpagebutton.setStyleSheet("background-color: lemonchiffon")

        # self.layout = QVBoxLayout(self.text)
        # self.layout.addWidget(self.text)
        # self.setLayout(self.layout)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        #self.layout.addWidget(self.space)
        self.layout.addWidget(self.task)
        self.layout.addWidget(self.coltitle1)
        self.layout.addWidget(self.slider1)
        #self.layout.addWidget(self.slider1print)
        self.layout.addWidget(self.coltitle2)
        self.layout.addWidget(self.slider2)
        self.layout.addWidget(self.coltitle3)
        self.layout.addWidget(self.slider3)
        self.layout.addWidget(self.newtaskbutton)
        self.layout.addWidget(self.nextpagebutton)
        self.setLayout(self.layout)
        

        # self.grid = QGridLayout()
        

        # self.grid.addWidget(QLabel("  "),0,0)
        # self.grid.addWidget(self.coltitle1,0,0)
        # self.grid.addWidget(self.coltitle2,0,0)
        # self.grid.addWidget(self.coltitle3,0,0)

        # self.setLayout(self.grid)
        

        self.nextpagebutton.clicked.connect(self.nextpage)


    def setupUi(self, Prior):
        Prior.setObjectName("OtherWindow")
        
        # self.text = QLabel("What do you want to get done today?")
        # self.text.setAlignment(Qt.AlignCenter)
        
        # self.space = QLabel(" ")
        # self.coltitle1 = QLabel("How urgent is this task?")
        # self.coltitle1.setAlignment(Qt.AlignLeft)
        # self.coltitle2 = QLabel("How important is this task to you?")
        # self.coltitle2.setAlignment(Qt.AlignCenter)
        # self.coltitle3 = QLabel("How long do you anticipate this task taking?")
        # self.coltitle3.setAlignment(Qt.AlignRight)
        
        # self.line1 = QLineEdit('Type your task here')
        # self.line2 = QLineEdit('Type your task here')
        # self.line3 = QLineEdit('Type your task here')
        
        #self.button = QPushButton("Next Page")

        # self.layout = QVBoxLayout()
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)
        # self.setLayout(self.layout)

        #self.button.clicked.connect(self.setupUi)
        #print("You're here")
        
        #self.button.clicked.connect(self.nextpage)


    def nextpage(self):
        #self.text.setText('Ready to go!')
        #self.window = QMainWindow()
        self.dialog = Result.Result()
        #self.windows.append(dialog)
        #self.ui.setupUi(self.window)
        self.dialog.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = Prior()
    #widget.setGeometry(0, 0, 1024, 768)
    widget.setStyleSheet("background-color: mediumslateblue")
    widget.showFullScreen()
    
    sys.exit(app.exec_())

