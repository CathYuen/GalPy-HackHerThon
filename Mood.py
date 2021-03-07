#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:49:29 2021

@author: antheaml
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import Prioritisation as Prioritisation

class Mood(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("How are you feeling? - 1 -")
        self.setStyleSheet("background-color: mediumslateblue")
        self.nextbutton = QPushButton("Next Page")
        self.tired = QPushButton("Tired")

        self.creative = QPushButton("Creative")
        self.unmotivated = QPushButton("Unmotivated")
        self.panicked = QPushButton("Panicked")
        self.focused = QPushButton("Focused")
        self.confident = QPushButton("Confident")
        self.upset = QPushButton("Upset")
        self.stressed = QPushButton("Stressed")
        self.refreshed = QPushButton("Refreshed")
        self.peaceful = QPushButton("Peaceful")
        
        self.nextbutton.setStyleSheet("background-color: lemonchiffon")
        self.tired.setStyleSheet("background-color: white")
        self.creative.setStyleSheet("background-color: white")
        self.unmotivated.setStyleSheet("background-color: white")
        self.panicked.setStyleSheet("background-color: white")
        self.focused.setStyleSheet("background-color: white")
        self.confident.setStyleSheet("background-color: white")
        self.upset.setStyleSheet("background-color: white")
        self.stressed.setStyleSheet("background-color: white")
        self.refreshed.setStyleSheet("background-color: white")
        self.peaceful.setStyleSheet("background-color: white")
        
        
        self.text = QLabel("How are you feeling today?")
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet("color: white")


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        
        self.layout.addWidget(self.tired)
        self.tired.clicked.connect(self.addslider)
        
        self.layout.addWidget(self.creative)
        emotion = "creative"
        self.creative.clicked.connect(self.addslider)  
        
        self.layout.addWidget(self.unmotivated)
        self.unmotivated.clicked.connect(self.addslider)      

        self.layout.addWidget(self.panicked)
        self.panicked.clicked.connect(self.addslider)

        self.layout.addWidget(self.focused)
        self.focused.clicked.connect(self.addslider)

        self.layout.addWidget(self.confident)
        self.confident.clicked.connect(self.addslider)

        self.layout.addWidget(self.upset)
        self.upset.clicked.connect(self.addslider)

        
        self.layout.addWidget(self.stressed)
        self.stressed.clicked.connect(self.addslider)

        self.layout.addWidget(self.refreshed)
        self.refreshed.clicked.connect(self.addslider)

        self.layout.addWidget(self.peaceful)
        self.peaceful.clicked.connect(self.addslider)

        self.layout.addWidget(self.nextbutton)
        
        self.setLayout(self.layout)

        self.nextbutton.clicked.connect(self.nextpage)


    def setupUi(self, Mood):
        Mood.setObjectName("OtherWindow")
        

    def addslider(self):
        self.textt = QLabel('How strong is this emotion?')
        self.textt.setStyleSheet("color: white")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.layout.addWidget(self.textt)
        self.layout.addWidget(self.slider)
        self.setLayout(self.layout)
        
    def nextpage(self):
        #self.text.setText('Ready to go!')
        #self.window = QMainWindow()
        self.dialog = Prioritisation.Prior()
        #self.windows.append(dialog)
        #self.ui.setupUi(self.window)
        self.dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget2 = Mood()
    #widget2.setStyleSheet("background-color: mediumslateblue")

    widget2.showFullScreen()

    sys.exit(app.exec_())

        
        