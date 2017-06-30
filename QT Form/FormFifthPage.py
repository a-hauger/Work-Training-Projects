#!/usr/bin/env python3

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

		self.jumpToFifth = QPushButton()
		self.jumpPix = QPixmap("Explosion.png")
		self.jumpIcon = QIcon(self.jumpPix)
		self.jumpToFifth.setIcon(self.jumpIcon)
		self.jumpToFifth.setIconSize(self.jumpPix.rect().size())
		self.jumpToFifth.setFixedSize(75, 75)

		self.textbox1 = QLineEdit(self)
		self.textbox1.setPlaceholderText("Mans Name")

		self.textbox2 = QLineEdit(self)
		self.textbox2.setPlaceholderText("Occupation")

		self.textbox3 = QLineEdit(self)
		self.textbox3.setPlaceholderText("Noun")

		self.textbox4 = QLineEdit(self)
		self.textbox4.setPlaceholderText("Noun")

		self.textbox5 = QLineEdit(self)
		self.textbox5.setPlaceholderText("Noun")

		self.textbox6 = QLineEdit(self)
		self.textbox6.setPlaceholderText("Shape")

		self.textbox7 = QLineEdit(self)
		self.textbox7.setPlaceholderText("Mans Name")

		self.textbox8 = QLineEdit(self)
		self.textbox8.setPlaceholderText("Verb")

		self.textbox9 = QLineEdit(self)
		self.textbox9.setPlaceholderText("Womans Name")

		self.textbox10 = QLineEdit(self)
		self.textbox10.setPlaceholderText("Body Part")

		self.textbox11 = QLineEdit(self)
		self.textbox11.setPlaceholderText("Verb")

		self.textbox12 = QLineEdit(self)
		self.textbox12.setPlaceholderText("Noun")

		self.textbox13 = QLineEdit(self)
		self.textbox13.setPlaceholderText("Noun")

		self.textbox14 = QLineEdit(self)
		self.textbox14.setPlaceholderText("Restaurant Name")

		self.textbox15 = QLineEdit(self)
		self.textbox15.setPlaceholderText("Historic Monument")

		self.textbox16 = QLineEdit(self)
		self.textbox16.setPlaceholderText("Verb")

		self.textbox17 = QLineEdit(self)
		self.textbox17.setPlaceholderText("Noun")

		self.textbox18 = QLineEdit(self)
		self.textbox18.setPlaceholderText("Noun")

		self.textbox19 = QLineEdit(self)
		self.textbox19.setPlaceholderText("Noun")

		self.textbox20 = QLineEdit(self)
		self.textbox20.setPlaceholderText("Verb")

		self.textbox21 = QLineEdit(self)
		self.textbox21.setPlaceholderText("Noun")

		self.textbox22 = QLineEdit(self)
		self.textbox22.setPlaceholderText("Adjective")

		self.textbox23 = QLineEdit(self)
		self.textbox23.setPlaceholderText("Adjective")

		self.textbox24 = QLineEdit(self)
		self.textbox24.setPlaceholderText("Emotion")

		self.textbox25 = QLineEdit(self)
		self.textbox25.setPlaceholderText("Verb")

		self.textbox26 = QLineEdit(self)
		self.textbox26.setPlaceholderText("Noun")

		self.textbox27 = QLineEdit(self)
		self.textbox27.setPlaceholderText("Noun")

		self.textbox28 = QLineEdit(self)
		self.textbox28.setPlaceholderText("Verb")

		self.textboxList = [self.textbox1, self.textbox2, self.textbox3, self.textbox4, self.textbox5, self.textbox6, self.textbox7, self.textbox8, self.textbox9, self.textbox10, self.textbox11, self.textbox12, self.textbox13, self.textbox14, self.textbox15, self.textbox16, self.textbox17, self.textbox18, self.textbox19, self.textbox20, self.textbox21, self.textbox22, self.textbox23, self.textbox24, self.textbox25, self.textbox26, self.textbox27, self.textbox28]
		"""*************************"""
		"""ADD WIDGETS TO FIRST PAGE"""
		"""*************************"""

		self.fifthPageLayout.addWidget(self.label, alignment = Qt.AlignCenter)

		self.fifthPageLayout.addWidget(self.textbox1)
		self.fifthPageLayout.addWidget(self.textbox2)
		self.fifthPageLayout.addWidget(self.textbox3)
		self.fifthPageLayout.addWidget(self.textbox4)
		self.fifthPageLayout.addWidget(self.textbox5)
		self.fifthPageLayout.addWidget(self.textbox6)
		self.fifthPageLayout.addWidget(self.textbox7)
		self.fifthPageLayout.addWidget(self.textbox8)
		self.fifthPageLayout.addWidget(self.textbox9)
		self.fifthPageLayout.addWidget(self.textbox10)
		self.fifthPageLayout.addWidget(self.textbox11)
		self.fifthPageLayout.addWidget(self.textbox12)
		self.fifthPageLayout.addWidget(self.textbox13)
		self.fifthPageLayout.addWidget(self.textbox14)
		self.fifthPageLayout.addWidget(self.textbox15)
		self.fifthPageLayout.addWidget(self.textbox16)
		self.fifthPageLayout.addWidget(self.textbox17)
		self.fifthPageLayout.addWidget(self.textbox18)
		self.fifthPageLayout.addWidget(self.textbox19)
		self.fifthPageLayout.addWidget(self.textbox20)
		self.fifthPageLayout.addWidget(self.textbox21)
		self.fifthPageLayout.addWidget(self.textbox22)
		self.fifthPageLayout.addWidget(self.textbox23)
		self.fifthPageLayout.addWidget(self.textbox24)
		self.fifthPageLayout.addWidget(self.textbox25)
		self.fifthPageLayout.addWidget(self.textbox26)
		self.fifthPageLayout.addWidget(self.textbox27)
		self.fifthPageLayout.addWidget(self.textbox28)

		self.fifthPageLayout.addWidget(self.generateMadLib, alignment = Qt.AlignCenter)

		"""*******************"""
		"""GETTERS AND SETTERS"""
		"""*******************"""

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
		textList.append(self.textbox20.text())
		textList.append(self.textbox21.text())
		textList.append(self.textbox22.text())
		textList.append(self.textbox23.text())
		textList.append(self.textbox24.text())
		textList.append(self.textbox25.text())
		textList.append(self.textbox26.text())
		textList.append(self.textbox27.text())
		textList.append(self.textbox28.text())

		return(textList)

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
		self.textbox20.clear()
		self.textbox21.clear()
		self.textbox22.clear()
		self.textbox23.clear()
		self.textbox24.clear()
		self.textbox25.clear()
		self.textbox26.clear()
		self.textbox27.clear()
		self.textbox28.clear()

	def setOpenData(self, textList):
		i = 0
		for textbox in self.textboxList:
			textbox.setText(textList[i])
			i = i+1

