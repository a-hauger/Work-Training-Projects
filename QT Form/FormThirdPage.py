#!/usr/bin/env python3

from textBox import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


"""Second Madlib Form"""


class thirdPageWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		"""*************************************************************************"""
		"""            CREATE ALL LABELS, LAYOUTS, BUTTONS AND TEXT BOXES           """
		"""*************************************************************************"""

		self.boldFont = QFont()
		self.boldFont.setBold(True)

		self.customFont = QFont("Serif", 12, QFont.Bold)

		self.label = QLabel("Input the words you want to use for the story!")
		self.label.setFont(self.customFont)
		self.thirdPageLayout = QVBoxLayout(self)

		self.generateMadLib = QPushButton("Generate Mad Lib!")
		self.generateMadLib.setFont(self.boldFont)
		self.generateMadLib.setFixedSize(150, 50)

		self.textbox1 = textBoxCreator("Adjective")

		self.textbox2 = textBoxCreator("Noun")

		self.textbox3 = textBoxCreator("Adjective")

		self.textbox4 = textBoxCreator("Noun (plural)")

		self.textbox5 = textBoxCreator("Adverb")

		self.textbox6 = textBoxCreator("Verb ending in -ing")

		self.textbox7 = textBoxCreator("Silly Plural Word")

		self.textbox8 = textBoxCreator("Adjective")

		self.textbox9 = textBoxCreator("Plural Noun")

		self.textbox10 = textBoxCreator("First Name")

		self.textbox11 = textBoxCreator("Adjective")

		self.textbox12 = textBoxCreator("Number")

		self.textbox13 = textBoxCreator("First Name")

		self.textbox14 = textBoxCreator("First Name")

		self.textbox15 = textBoxCreator("First Name")

		self.textbox16 = textBoxCreator("First Name")

		self.textbox17 = textBoxCreator("First Name")

		self.textbox18 = textBoxCreator("First Name")

		self.textbox19 = textBoxCreator("Plural Noun")

		self.textboxList = [self.textbox1, self.textbox2, self.textbox3, self.textbox4, self.textbox5, self.textbox6, self.textbox7, self.textbox8, self.textbox9, self.textbox10, self.textbox11, self.textbox12, self.textbox13, self.textbox14, self.textbox15, self.textbox16, self.textbox17, self.textbox18, self.textbox19]

		"""*************************************************************************"""
		"""          END ALL LABELS, LAYOUTS, BUTTONS AND TEXT BOXES                """
		"""*************************************************************************"""

		"""*************************************************************************"""
		"""                       ADD WIDGETS TO THIRD PAGE                         """
		"""*************************************************************************"""

		self.thirdPageLayout.addWidget(self.label, alignment = Qt.AlignCenter)

		for textbox in self.textboxList:
			self.thirdPageLayout.addWidget(textbox)		

		self.thirdPageLayout.addWidget(self.generateMadLib, alignment = Qt.AlignCenter)
		self.thirdPageLayout.addStretch(1)
		"""*************************************************************************"""
		"""                            END WIDGETS                                  """
		"""*************************************************************************"""

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
			if (textList[i] != ""):
				textbox.setText(textList[i])
				textbox.textMod()
			i = i+1

