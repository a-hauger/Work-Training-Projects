#!/usr/bin/env python3


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class secondPageWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		"""******************************************************************"""
		""" 		CREATE ALL LAYOUTS, AND BUTTONS FOR SECOND PAGE	     """
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
		""" 	END ALL LAYOUTS, AND BUTTONS AND FOR SECOND PAGE             """
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

		self.label.setText("It was a(n) " + self.box1 + ", cold November day."\
					"  I woke up to the " + self.box2 + " smell of "\
					+ self.box3 + " roasting in the " + self.box4 \
					+ " downstairs. I " + self.box5 + " down the stairs "\
					"to see if I could help " + self.box6 + "the dinner."\
					" My Mom said, 'See if " + self.box7 + " needs a fresh "\
					+ self.box8 + ".'  So I carried a tray of glasses full "\
					"of " + self.box9 + " into the " + self.box10 + " room."\
					" When I got there, I couldn't believe my " + self.box11 \
					+ "! There were " + self.box12 + " " + self.box13 + " on "\
					"the " + self.box14 + "!")
		return
