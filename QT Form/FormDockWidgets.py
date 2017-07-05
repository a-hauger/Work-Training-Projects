#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class docks(QDockWidget):
	def __init__(self):
		QDockWidget.__init__(self, "Jump!")

		"""BUTTONS"""
		"""FIRST"""
		self.jumpToFirst = QPushButton()
		self.jumpPix = QPixmap("turkey.png")
		self.jumpIcon = QIcon(self.jumpPix)
		self.jumpToFirst.setIcon(self.jumpIcon)
		self.jumpToFirst.setIconSize(self.jumpPix.rect().size())
		self.jumpToFirst.setFixedSize(75, 75)

		"""THIRD"""
		self.jumpToThird = QPushButton()
		self.jumpPix = QPixmap("Earth.png")
		self.jumpIcon = QIcon(self.jumpPix)
		self.jumpToThird.setIcon(self.jumpIcon)
		self.jumpToThird.setIconSize(self.jumpPix.rect().size())
		self.jumpToThird.setFixedSize(75, 75)

		"""FIFTH"""
		self.jumpToFifth = QPushButton()
		self.jumpPix = QPixmap("Explosion.png")
		self.jumpIcon = QIcon(self.jumpPix)
		self.jumpToFifth.setIcon(self.jumpIcon)
		self.jumpToFifth.setIconSize(self.jumpPix.rect().size())
		self.jumpToFifth.setFixedSize(75, 75)
	
		"""CREATE DOCK"""

		self.widget = QWidget()
		self.dockLayout = QHBoxLayout()
		self.dockLayout.addWidget(self.jumpToFirst)
		self.dockLayout.addWidget(self.jumpToThird)
		self.dockLayout.addWidget(self.jumpToFifth)

		self.widget.setLayout(self.dockLayout)

		self.setWidget(self.widget)
