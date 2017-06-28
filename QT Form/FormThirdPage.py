#!/usr/bin/env python3

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

		self.textbox1 = QLineEdit(self)
		self.textbox1.setPlaceholderText("Adjective")

		self.textbox2 = QLineEdit(self)
		self.textbox2.setPlaceholderText("Noun")

		self.textbox3 = QLineEdit(self)
		self.textbox3.setPlaceholderText("Adjective")

		self.textbox4 = QLineEdit(self)
		self.textbox4.setPlaceholderText("Noun (plural)")

		self.textbox5 = QLineEdit(self)
		self.textbox5.setPlaceholderText("Adverb")

		self.textbox6 = QLineEdit(self)
		self.textbox6.setPlaceholderText("Verb ending in -ing")

		self.textbox7 = QLineEdit(self)
		self.textbox7.setPlaceholderText("Silly Plural Word")

		self.textbox8 = QLineEdit(self)
		self.textbox8.setPlaceholderText("Adjective")

		self.textbox9 = QLineEdit(self)
		self.textbox9.setPlaceholderText("Plural Noun")

		self.textbox10 = QLineEdit(self)
		self.textbox10.setPlaceholderText("First Name")

		self.textbox11 = QLineEdit(self)
		self.textbox11.setPlaceholderText("Adjective")

		self.textbox12 = QLineEdit(self)
		self.textbox12.setPlaceholderText("Number")

		self.textbox13 = QLineEdit(self)
		self.textbox13.setPlaceholderText("First Name")

		self.textbox14 = QLineEdit(self)
		self.textbox14.setPlaceholderText("First Name")

		self.textbox15 = QLineEdit(self)
		self.textbox15.setPlaceholderText("First Name")

		self.textbox16 = QLineEdit(self)
		self.textbox16.setPlaceholderText("First Name")

		self.textbox17 = QLineEdit(self)
		self.textbox17.setPlaceholderText("First Name")

		self.textbox18 = QLineEdit(self)
		self.textbox18.setPlaceholderText("First Name")

		self.textbox19 = QLineEdit(self)
		self.textbox19.setPlaceholderText("Plural Noun")

		self.textboxList = [self.textbox1, self.textbox2, self.textbox3, self.textbox4, self.textbox5, self.textbox6, self.textbox7, self.textbox8, self.textbox9, self.textbox10, self.textbox11, self.textbox12, self.textbox13, self.textbox14, self.textbox15, self.textbox16, self.textbox17, self.textbox18, self.textbox19]

		"""*************************************************************************"""
		"""          END ALL LABELS, LAYOUTS, BUTTONS AND TEXT BOXES                """
		"""*************************************************************************"""

		"""*************************************************************************"""
		"""                       ADD WIDGETS TO THIRD PAGE                         """
		"""*************************************************************************"""

		self.thirdPageLayout.addWidget(self.label, alignment = Qt.AlignCenter)

		self.thirdPageLayout.addWidget(self.textbox1)
		self.thirdPageLayout.addWidget(self.textbox2)
		self.thirdPageLayout.addWidget(self.textbox3)
		self.thirdPageLayout.addWidget(self.textbox4)
		self.thirdPageLayout.addWidget(self.textbox5)
		self.thirdPageLayout.addWidget(self.textbox6)
		self.thirdPageLayout.addWidget(self.textbox7)
		self.thirdPageLayout.addWidget(self.textbox8)
		self.thirdPageLayout.addWidget(self.textbox9)
		self.thirdPageLayout.addWidget(self.textbox10)
		self.thirdPageLayout.addWidget(self.textbox11)
		self.thirdPageLayout.addWidget(self.textbox12)
		self.thirdPageLayout.addWidget(self.textbox13)
		self.thirdPageLayout.addWidget(self.textbox14)
		self.thirdPageLayout.addWidget(self.textbox15)
		self.thirdPageLayout.addWidget(self.textbox16)
		self.thirdPageLayout.addWidget(self.textbox17)
		self.thirdPageLayout.addWidget(self.textbox18)
		self.thirdPageLayout.addWidget(self.textbox19)

		self.thirdPageLayout.addWidget(self.generateMadLib, alignment = Qt.AlignCenter)
		"""*************************************************************************"""
		"""                            END WIDGETS                                  """
		"""*************************************************************************"""

	def getTextBoxData(self):
		textList = []

		textList.append(self.textbox1.text())
		textList.append(self.textbox2.text())
		textList.append(self.textbox3.text())
		textList.append(self.textbox4.text())
		textList.append(self.textbox5.text())
		textList.append(self.textbox6.text())
		textList.append(self.textbox7.text())
		textList.append(self.textbox8.text())
		textList.append(self.textbox9.text())
		textList.append(self.textbox10.text())
		textList.append(self.textbox11.text())
		textList.append(self.textbox12.text())
		textList.append(self.textbox13.text())
		textList.append(self.textbox14.text())
		textList.append(self.textbox15.text())
		textList.append(self.textbox16.text())
		textList.append(self.textbox17.text())
		textList.append(self.textbox18.text())
		textList.append(self.textbox19.text())
	
		return (textList)

	def setTextBoxData(self):

		self.textbox1.clear()
		self.textbox2.clear()
		self.textbox3.clear()
		self.textbox4.clear()
		self.textbox5.clear()
		self.textbox6.clear()
		self.textbox7.clear()
		self.textbox8.clear()
		self.textbox9.clear()
		self.textbox10.clear()
		self.textbox11.clear()
		self.textbox12.clear()
		self.textbox13.clear()
		self.textbox14.clear()
		self.textbox15.clear()
		self.textbox16.clear()
		self.textbox17.clear()
		self.textbox18.clear()
		self.textbox19.clear()

		return

	def setOpenData(self, textList):
		i = 0
		for textbox in self.textboxList:
			textbox.setText(textList[i])
			i = i+1

