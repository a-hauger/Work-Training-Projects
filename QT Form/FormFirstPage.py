#!/usr/bin/env python3


from textBox import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class firstPageWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)


		"""*****************************************************************"""
		"""CREATE ALL LABELS, LAYOUTS, BUTTONS AND TEXT BOXES FOR FIRST PAGE"""
		"""*****************************************************************"""
		self.boldFont = QFont()
		self.boldFont.setBold(True)

		self.customFont = QFont("Serif", 12, QFont.Bold)

		self.label = QLabel("Input the words you want to use for the story!")
		self.label.setFont(self.customFont)
		self.firstPageLayout = QVBoxLayout(self)

		self.generateMadLib = QPushButton("Generate Mad Lib!")
		self.generateMadLib.setFont(self.boldFont)
		self.generateMadLib.setFixedSize(150, 50)

		self.textbox1 = textBoxCreator("Adjective")

		self.textbox2 = textBoxCreator("Adjective")

		self.textbox3 = textBoxCreator("Type of Bird")

		self.textbox4 = textBoxCreator("Room of House")

		self.textbox5 = textBoxCreator("Past Tense Verb")

		self.textbox6 = textBoxCreator("Verb")

		self.textbox7 = textBoxCreator("Relative's Name")

		self.textbox8 = textBoxCreator("Noun")

		self.textbox9 = textBoxCreator("Liquid")

		self.textbox10 = textBoxCreator("Verb Ending in -ing")

		self.textbox11 = textBoxCreator("Plural Body Part")

		self.textbox12 = textBoxCreator("Plural Noun")

		self.textbox13 = textBoxCreator("Verb Ending in -ing")

		self.textbox14 = textBoxCreator("Noun")

		self.textboxList = [self.textbox1, self.textbox2, self.textbox3, self.textbox4, self.textbox5, self.textbox6, self.textbox7, self.textbox8, self.textbox9, self.textbox10, self.textbox11, self.textbox12, self.textbox13, self.textbox14]
		
		"""*****************************************************************"""
		"""  END ALL LABELS, LAYOUTS, BUTTONS AND TEXT BOXES FOR FIRST PAGE """
		"""*****************************************************************"""
		"""*****************************************************************"""
		"""                 ADD WIDGETS TO FIRST PAGE                       """
		"""*****************************************************************"""

		self.firstPageLayout.addWidget(self.label, alignment = Qt.AlignCenter)

		for textbox in self.textboxList:
			self.firstPageLayout.addWidget(textbox)

		self.firstPageLayout.addWidget(self.generateMadLib, alignment = Qt.AlignCenter)
		self.firstPageLayout.addStretch(1)
		"""****************************************************************"""
		"""               END WIDGETS FOR FIRST PAGE                       """
		"""****************************************************************"""

	def getTextBoxData(self):
		textList = []

		for textbox in self.textboxList:
			textList.append(textbox.text())
		return (textList)

	def setTextBoxData(self):

		for textbox in self.textboxList:
			textbox.clear()

		return

	def setOpenData(self, textList):
		i = 0
		for textbox in self.textboxList:
			if(textList[i] != ""):
				textbox.setText(textList[i])
				textbox.textMod()
			i = i+1
