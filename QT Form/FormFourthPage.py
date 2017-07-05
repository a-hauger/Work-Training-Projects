#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class fourthPageWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		"""******************************************************************"""
		"""             CREATE ALL LAYOUTS, AND BUTTONS FOR FOURTH PAGE      """
		"""******************************************************************"""

		self.secondPageLayout = QVBoxLayout(self)

		self.boldFont = QFont()
		self.boldFont.setBold(True)

		self.againButton = QPushButton("Again?")
		self.againButton.setFont(self.boldFont)
		self.againButton.setFixedSize(150, 50)

		self.label = QLabel("BLAHBLAH")
		self.label.setWordWrap(True)

		self.secondPageLayout.addWidget(self.label, alignment = Qt.AlignCenter)
		self.secondPageLayout.addWidget(self.againButton, alignment = Qt.AlignCenter)


		"""******************************************************************"""
		"""     END ALL LAYOUTS, AND BUTTONS AND FOR FOURTH PAGE             """
		"""******************************************************************"""

	def setTextBoxData(self, textList):

		self.label.setText("")

		self.box1 = ""
		self.box2 = ""
		self.box3 = ""
		self.box4 = ""
		self.box5 = ""
		self.box6 = ""
		self.box7 = ""
		self.box8 = ""
		self.box9 = ""
		self.box10 = ""
		self.box11 = ""
		self.box12 = ""
		self.box13 = ""
		self.box14 = ""
		self.box15 = ""
		self.box16 = ""
		self.box17 = ""
		self.box18 = ""
		self.box19 = ""

		self.box1 = textList[0]
		self.box2 = textList[1]
		self.box3 = textList[2]
		self.box4 = textList[3]
		self.box5 = textList[4]
		self.box6 = textList[5]
		self.box7 = textList[6]
		self.box8 = textList[7]
		self.box9 = textList[8]
		self.box10 = textList[9]
		self.box11 = textList[10]
		self.box12 = textList[11]
		self.box13 = textList[12]
		self.box14 = textList[13]
		self.box15 = textList[14]
		self.box16 = textList[15]
		self.box17 = textList[16]
		self.box18 = textList[17]
		self.box19 = textList[18]

		self.label.setText("When we look up into the sky on a/an " + self.box1 + " Summer night, we see millions of tiny spots of light.  Each one represent a/an " + self.box2 + " which is the center of a/an " + self.box3 + "solar system with dozens of " + self.box4 + " revolving " + self.box5 + " around a distant sun.  Sometimes these suns expand and begin " + self.box6 + " their neighbors.  Soon they will become so big, hey will turn into " + self.box7 + ".  Eventually, they subside and become " + self.box8 + " giants or perhaps black " + self.box9 + ".  our own planet, which we call " + self.box10 + ", circles around our " + self.box11 + " sun " + self.box12 + " times every year.  there are eight other planets in our solar system.  They are named " + self.box13 + ", " + self.box14 + ", " + self.box15 + ", " + self.box16 + ", " + self.box17 + ", " + self.box18 + ", Jupiter and Mars.  Scientists who study these planets are called " + self.box19 + ".")

		return
