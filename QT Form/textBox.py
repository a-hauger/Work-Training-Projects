#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class textBoxCreator(QLineEdit):
	def __init__(self, kindOfWord):
		QLineEdit.__init__(self)

		self.isModified = 0

		self.setPlaceholderText(kindOfWord)

	def isTextMod(self):
		if (self.isModified == 0):
			return (0)
		else:
			return (1)

	def textMod(self):
		if (self.text() != ""):
			if (self.isModified == 0):
				self.isModified = 1
		else:
			self.isModified = 0

		return
