#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class mainPageWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.mainPageLayout = QVBoxLayout(self)

		self.boldFont = QFont()
		self.boldFont.setBold(True)

		self.customFont = QFont("Helvetica", 12, QFont.Bold)

		self.label = QLabel("Choose the Mad Lib you would like to complete!")
		self.label.setFont(self.customFont)

		self.moveToFormButton = QPushButton("Go To MadLib!")
		self.moveToFormButton.setFixedSize(150, 50)
		self.moveToFormButton.setFont(self.boldFont)

		self.comboBox = QComboBox()
		self.comboBox.SizeAdjustPolicy(QComboBox.AdjustToContents)

		self.comboBox.addItem("Choose your Mad Lib!")
		self.comboBox.addItem("1. Thanksgiving Day!")
		self.comboBox.addItem("2. Our Solar System!")
		self.comboBox.addItem("3. Michael Bay!")
		self.comboBox.setFixedWidth(self.comboBox.sizeHint().width()+30)

		self.fillerPix = QPixmap("NewMadLib.png")
		self.fillerLabel = QLabel()
		self.fillerLabel.setPixmap(self.fillerPix)

		self.mainPageLayout.addWidget(self.fillerLabel, alignment = Qt.AlignCenter)	
		self.mainPageLayout.addWidget(self.label, alignment = Qt.AlignCenter)
		self.mainPageLayout.addWidget(self.comboBox, alignment = Qt.AlignCenter)
		self.mainPageLayout.addWidget(self.moveToFormButton, alignment = Qt.AlignCenter)
		self.mainPageLayout.addStretch(stretch = 2)
