#!/usr/bin/env python3


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

		self.textbox1 = QLineEdit(self)
		self.textbox1.setPlaceholderText("Adjective")

		self.textbox2 = QLineEdit(self)
		self.textbox2.setPlaceholderText("Adjective")

		self.textbox3 = QLineEdit(self)
		self.textbox3.setPlaceholderText("Type of Bird")

		self.textbox4 = QLineEdit(self)
		self.textbox4.setPlaceholderText("Room of House")

		self.textbox5 = QLineEdit(self)
		self.textbox5.setPlaceholderText("Past Tense Verb")

		self.textbox6 = QLineEdit(self)
		self.textbox6.setPlaceholderText("Verb")

		self.textbox7 = QLineEdit(self)
		self.textbox7.setPlaceholderText("Relative's Name")

		self.textbox8 = QLineEdit(self)
		self.textbox8.setPlaceholderText("Noun")

		self.textbox9 = QLineEdit(self)
		self.textbox9.setPlaceholderText("Liquid")

		self.textbox10 = QLineEdit(self)
		self.textbox10.setPlaceholderText("Verb Ending in -ing")

		self.textbox11 = QLineEdit(self)
		self.textbox11.setPlaceholderText("Plural Body Part")

		self.textbox12 = QLineEdit(self)
		self.textbox12.setPlaceholderText("Plural Noun")

		self.textbox13 = QLineEdit(self)
		self.textbox13.setPlaceholderText("Verb Ending in -ing")

		self.textbox14 = QLineEdit(self)
		self.textbox14.setPlaceholderText("Noun")

		self.textboxList = [self.textbox1, self.textbox2, self.textbox3, self.textbox4, self.textbox5, self.textbox6, self.textbox7, self.textbox8, self.textbox9, self.textbox10, self.textbox11, self.textbox12, self.textbox13, self.textbox14]
		
		"""*****************************************************************"""
		"""  END ALL LABELS, LAYOUTS, BUTTONS AND TEXT BOXES FOR FIRST PAGE """
		"""*****************************************************************"""
		"""*****************************************************************"""
		"""                 ADD WIDGETS TO FIRST PAGE                       """
		"""*****************************************************************"""

		self.firstPageLayout.addWidget(self.label, alignment = Qt.AlignCenter)

		self.firstPageLayout.addWidget(self.textbox1)
		self.firstPageLayout.addWidget(self.textbox2)
		self.firstPageLayout.addWidget(self.textbox3)
		self.firstPageLayout.addWidget(self.textbox4)
		self.firstPageLayout.addWidget(self.textbox5)
		self.firstPageLayout.addWidget(self.textbox6)
		self.firstPageLayout.addWidget(self.textbox7)
		self.firstPageLayout.addWidget(self.textbox8)
		self.firstPageLayout.addWidget(self.textbox9)
		self.firstPageLayout.addWidget(self.textbox10)
		self.firstPageLayout.addWidget(self.textbox11)
		self.firstPageLayout.addWidget(self.textbox12)
		self.firstPageLayout.addWidget(self.textbox13)
		self.firstPageLayout.addWidget(self.textbox14)

		self.firstPageLayout.addWidget(self.generateMadLib, alignment = Qt.AlignCenter)

		"""****************************************************************"""
		"""               END WIDGETS FOR FIRST PAGE                       """
		"""****************************************************************"""

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

		return

	def setOpenData(self, textList):
		i = 0
		for textbox in self.textboxList:
			textbox.setText(textList[i])
			i = i+1
