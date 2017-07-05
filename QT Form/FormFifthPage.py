#!/usr/bin/env python3

from textBox import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class fifthPageWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		"""*****************************************************************"""
		"""CREATE ALL LABELS, LAYOUTS, BUTTONS AND TEXT BOXES FOR FIFTH PAGE"""
		"""*****************************************************************"""
		self.boldFont = QFont()
		self.boldFont.setBold(True)

		self.customFont = QFont("Serif", 12, QFont.Bold)

		self.label = QLabel("Input the words you want to use for the story!")
		self.label.setFont(self.customFont)
		self.fifthPageLayout = QVBoxLayout(self)

		self.generateMadLib = QPushButton("Generate Mad Lib!")
		self.generateMadLib.setFont(self.boldFont)
		self.generateMadLib.setFixedSize(150, 50)

		self.textbox1 = textBoxCreator("Mans Name")

		self.textbox2 = textBoxCreator("Occupation")

		self.textbox3 = textBoxCreator("Noun")

		self.textbox4 = textBoxCreator("Noun")

		self.textbox5 = textBoxCreator("Noun")

		self.textbox6 = textBoxCreator("Shape")

		self.textbox7 = textBoxCreator("Mans Name")

		self.textbox8 = textBoxCreator("Verb")

		self.textbox9 = textBoxCreator("Womans Name")

		self.textbox10 = textBoxCreator("Body Part")

		self.textbox11 = textBoxCreator("Verb")

		self.textbox12 = textBoxCreator("Noun")

		self.textbox13 = textBoxCreator("Noun")

		self.textbox14 = textBoxCreator("Restaurant Name")

		self.textbox15 = textBoxCreator("Historic Monument")

		self.textbox16 = textBoxCreator("Verb")

		self.textbox17 = textBoxCreator("Noun")

		self.textbox18 = textBoxCreator("Noun")

		self.textbox19 = textBoxCreator("Noun")

		self.textbox20 = textBoxCreator("Verb")

		self.textbox21 = textBoxCreator("Noun")

		self.textbox22 = textBoxCreator("Adjective")

		self.textbox23 = textBoxCreator("Adjective")

		self.textbox24 = textBoxCreator("Emotion")

		self.textbox25 = textBoxCreator("Verb")

		self.textbox26 = textBoxCreator("Noun")

		self.textbox27 = textBoxCreator("Noun")

		self.textbox28 = textBoxCreator("Verb")

		self.textboxList = [self.textbox1, self.textbox2, self.textbox3, self.textbox4, self.textbox5, self.textbox6, self.textbox7, self.textbox8, self.textbox9, self.textbox10, self.textbox11, self.textbox12, self.textbox13, self.textbox14, self.textbox15, self.textbox16, self.textbox17, self.textbox18, self.textbox19, self.textbox20, self.textbox21, self.textbox22, self.textbox23, self.textbox24, self.textbox25, self.textbox26, self.textbox27, self.textbox28]
		"""*************************"""
		"""ADD WIDGETS TO FIFTH PAGE"""
		"""*************************"""

		self.fifthPageLayout.addWidget(self.label, alignment = Qt.AlignCenter)

		for textbox in self.textboxList:
			self.fifthPageLayout.addWidget(textbox)

		self.fifthPageLayout.addWidget(self.generateMadLib, alignment = Qt.AlignCenter)

		"""*******************"""
		"""GETTERS AND SETTERS"""
		"""*******************"""

	def getTextBoxData(self):
		textList = []

		for textbox in self.textboxList:
			textList.append(textbox.text())

		return(textList)

	def setTextBoxData(self):

		for textbox in self.textboxList:
			textbox.clear()

	def setOpenData(self, textList):
		i = 0
		for textbox in self.textboxList:
			if(textList[i] != ""):
				textbox.setText(textList[i])
				textbox.textMod()
			i = i+1
