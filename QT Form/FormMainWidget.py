#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from FormMainPage import *
from FormFirstPage import *
from FormSecondPage import *
from FormThirdPage import *
from FormFourthPage import *
from FormFifthPage import *
from FormSixthPage import *

class MainWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		"""****************************************************************"""
		"""          CREATE FONT, BUTTON, PAGES, LAYOUT, SCROLL            """
		"""****************************************************************"""

		self.boldFont = QFont()
		self.boldFont.setBold(True)

		self.closeButton = QPushButton("Close")
		self.closeButton.setFont(self.boldFont)
		self.closeButton.setFixedSize(100,50)
			
		self.mainPage = mainPageWidget()
		self.firstPage = firstPageWidget()
		self.secondPage = secondPageWidget()
		self.thirdPage = thirdPageWidget()		
		self.fourthPage = fourthPageWidget()
		self.fifthPage = fifthPageWidget()
		self.sixthPage = sixthPageWidget()

		self.mainLayout = QVBoxLayout(self)

		self.scrollWidget = QWidget()
		
		"""*****************************************************************"""
		"""       CREATE STACK LAYOUT WITH PARENT SCROLLWIDGET              """
		"""*****************************************************************"""

		self.Stack = QStackedLayout(self.scrollWidget)
		self.Stack.addWidget(self.mainPage)
		self.Stack.addWidget(self.firstPage)
		self.Stack.addWidget(self.secondPage)
		self.Stack.addWidget(self.thirdPage)
		self.Stack.addWidget(self.fourthPage)
		self.Stack.addWidget(self.fifthPage)
		self.Stack.addWidget(self.sixthPage)

		"""*****************************************************************"""
		""" CREATE SCROLLAREA, ADD SCROLL WIDGET TO AREA, ADD AREA TO LAYOUT"""
		"""*****************************************************************"""

		self.scrollArea = QScrollArea()
		self.scrollArea.setFrameShape(QFrame.NoFrame)

		self.scrollArea.setWidget(self.scrollWidget)
		self.scrollArea.setWidgetResizable(True)

		self.mainLayout.addWidget(self.scrollArea)

		self.mainLayout.addWidget(self.closeButton, alignment = Qt.AlignRight)

