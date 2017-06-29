#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class howToDialog(QDialog):
	def __init__(self, styleSheet):
		QDialog.__init__(self)

		self.style = styleSheet
		self.createDialog()

	def createDialog(self): 
		self.howToStyle = self.style

		self.setWindowTitle("How To!")

		self.titleFont = QFont("Helvetica", 14)
		self.titleFont.setItalic(True)
		self.bodyFont = QFont("Helvetica", 10)
 
		self.howToTitle = QLabel("How to Play!")
		self.howToText = QLabel("\tFirst, choose a Mad Lib you would like to play from the drop down box.  After you have selected a choice, click the 'Go To MadLib!' button found below the drop down box.  You will be taken to a screen with multiple blank text boxes to fill; these text boxes include the desired word types.  Fill in the text boxes and continue to the bottom of the screen.  A box with the words 'Generate MadLib!' is located there and will take you to a screen with the completed MadLib!  You can click 'Again?' to return to the main page and choose another MadLib!\n\n\t If you would like to go back and alter your mad lib, click Edit -> Back.  If you want to restart your Mad Lib, click File -> Restart.  If you want to start a new Mad Lib, click File -> New.  You can save your current Mad Lib by clicking File -> Save and you can restart a Mad Lib by clicking File -> Open.  Clicking File -> Exit or the 'Close' button at any time will exit this application.")
 
		self.howToTitle.setFont(self.titleFont)

		self.howToText.setFont(self.bodyFont)
		self.howToText.setWordWrap(True)
 
		self.howToFrame1 = QFrame()
		self.howToFrame1.setFrameStyle(QFrame.HLine)
		self.howToFrame1.setFrameShadow(QFrame.Sunken)
 
		self.howToLayout = QVBoxLayout()
		self.howToLayout.addWidget(self.howToTitle, alignment = Qt.AlignCenter)
		self.howToLayout.addWidget(self.howToFrame1)
		self.howToLayout.addWidget(self.howToText, alignment = Qt.AlignCenter)
 
		self.setLayout(self.howToLayout)

		self.setStyleSheet(self.howToStyle)
		self.show()
		return
