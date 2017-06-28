#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class aboutDialog(QDialog):
	def __init__(self):
		QDialog.__init__(self)

		self.createDialog()

	def createDialog(self):
		self.aboutStyle = "QDialog{background-color: #232121; border:1px solid gray; border-radius: 10px}"
 
		self.setWindowTitle("About!")
 
		self.titleFont = QFont("Helvetica", 14)
		self.titleFont.setItalic(True)
		self.bodyFont = QFont("Serif", 10)

		self.aboutTitle = QLabel("About the App!")
		self.aboutTitle.setFont(self.titleFont)
		self.aboutText = QLabel("MadLib! Generator\nVersion: 1.0\nUpdated: 6/23/17")
		self.aboutText.setFont(self.bodyFont)
		self.aboutText.setWordWrap(True)

		self.aboutDeveloperTitle = QLabel("About the Developer! --Anthony Hauger--")
		self.aboutDeveloperTitle.setFont(self.titleFont)
		self.aboutDeveloperText = QLabel("Anthony is a senior at CU Boulder currently working with LASP in or    der to train on how to program code more efficiently.  He is currently working on a two dimensional graphical applica    tion using PyQt5!")
		self.aboutDeveloperText.setWordWrap(True)
		self.aboutDeveloperText.setFont(self.bodyFont)

		self.aboutFrame1 = QFrame()
		self.aboutFrame2 = QFrame()
		self.aboutFrame3 = QFrame()
		self.aboutFrame1.setFrameStyle(QFrame.HLine)
		self.aboutFrame1.setFrameShadow(QFrame.Sunken)
		self.aboutFrame2.setFrameStyle(QFrame.HLine)
		self.aboutFrame2.setFrameShadow(QFrame.Sunken)
		self.aboutFrame3.setFrameStyle(QFrame.HLine)
		self.aboutFrame3.setFrameShadow(QFrame.Sunken)

		self.aboutLayout = QVBoxLayout()
		self.aboutLayout.addWidget(self.aboutTitle, alignment = Qt.AlignCenter)
		self.aboutLayout.addWidget(self.aboutFrame1)
		self.aboutLayout.addWidget(self.aboutText, alignment = Qt.AlignCenter)
		self.aboutLayout.addWidget(self.aboutFrame2)
		self.aboutLayout.addWidget(self.aboutDeveloperTitle, alignment = Qt.AlignCenter)
		self.aboutLayout.addWidget(self.aboutFrame3)
		self.aboutLayout.addWidget(self.aboutDeveloperText, alignment = Qt.AlignCenter)
		self.aboutDeveloperText.setFixedSize(self.aboutDeveloperText.sizeHint())

		self.setLayout(self.aboutLayout)

		self.setStyleSheet(self.aboutStyle)
		self.show()
		return
 
