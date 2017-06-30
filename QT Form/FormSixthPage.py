#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class sixthPageWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		"""*********************************************"""
		"""CREATE ALL LAYOUTS AND BUTTONS FOR SIXTH PAGE"""
		"""*********************************************"""

		self.sixthPageLayout = QVBoxLayout(self)

		self.boldFont = QFont()
		self.boldFont.setBold(True)

		self.againButton = QPushButton("Again?")
		self.againButton.setFont(self.boldFont)
		self.againButton.setFixedSize(150,50)

		self.label = QLabel("")
		self.label.setWordWrap(True)

		self.sixthPageLayout.addWidget(self.label, alignment = Qt.AlignCenter)
		self.sixthPageLayout.addWidget(self.againButton, alignment = Qt.AlignCenter)

	def setTextBoxData(self, textList):

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
		self.box20 = textList[19]
		self.box21 = textList[20]
		self.box22 = textList[21]
		self.box23 = textList[22]
		self.box24 = textList[23]
		self.box25 = textList[24]
		self.box26 = textList[25]
		self.box27 = textList[26]
		self.box28 = textList[27]

		self.label.setText(self.box1 + " is a normal " + self.box2 + ". Then, one day, a " + self.box3 + " explodes, causing a " + self.box4 + " to blow up, and a nearby " + self.box5 + " erupts into a " + self.box6 + " of flames. " + self.box7 + " realizes that he's being chased by the government, who's trying to " + self.box8 + " him.  While on the run, he teams up with an incredibly attractive woman named " + self.box9 + ", who has an incredible " + self.box10 + ". She may be from the streets, but she can " +self.box11 + " like nobody's business.  The duo decide to turn the tables on their pursuers by blowing up a " + self.box12 + ", which triggers a chain reaction, causing the local " +self.box13 + ", " + self.box14 + ", and the " + self.box15 + " to explode.  Then, the bad guys' helicopter gets " +self.box16 + " by a piece of " + self.box17 + " from when the " + self.box18 + " exploded., and the helicopter explodes and falls onto a " + self.box19 + ", causing it to " + self.box20 + " which shoots a fireball straight into the heart of " + self.box21 + " and destroys the bad guy leader.  Everything is " + self.box22 + " and the two decide that such a " + self.box23 + " ordeal has caused them to fall in " + self.box24 + " with each other.  They decide to celebrate by " + self.box25 + "ing on the " + self.box26 + ", and they even managed to use a " + self.box27 + " from the beginning of the movie, to " + self.box28 + " the whole story together.")

		return

