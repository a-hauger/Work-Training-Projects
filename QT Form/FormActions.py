#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Actions(QObject):
	def __init__(self):
		QObject.__init__(self)

		

		self.isModified = 0

		#file actions
		self.newAction = QAction("&New", self)
		self.newAction.setShortcut("CTRL+N")
		self.newAction.setIcon(QIcon("NewMadLib.png"))

		self.restartAction = QAction("&Restart", self)
		self.restartAction.setShortcut("CTRL+R")
		self.restartAction.setIcon(QIcon("reset.png"))

		self.saveAction = QAction("&Save", self)
		self.saveAction.setShortcut("CTRL+S")
		self.saveAction.setIcon(QIcon("SaveIcon.png"))

		self.openAction = QAction("&Open", self)
		self.openAction.setShortcut("CTRL+O")
		self.openAction.setIcon(QIcon("OpenIcon.png"))

		self.exitAction = QAction("&Exit", self)
		self.exitAction.setShortcut("CTRL+E")
		self.exitAction.setIcon(QIcon("exit.png"))

		#edit actions
		self.backAction = QAction("&Back", self)
		self.backAction.setShortcut("CTRL+B")
		self.backAction.setIcon(QIcon("BackIcon.png"))

		self.themeAction = QAction("&Themes", self)
		self.themeAction.setShortcut("CTRL+T")
		self.themeAction.setIcon(QIcon("palette.png"))

		#help actions
		self.howToAction = QAction("&How To", self)
		self.howToAction.setShortcut("CTRL+H")

		self.aboutAction = QAction("&About", self)
		self.aboutAction.setShortcut("CTRL+A")

	def addSeparators(self, actionList):

		for index, action in enumerate(actionList):
			if(action is None):

				sepAction = QAction(self)
				sepAction.setSeparator(True)

				actionList[index] = sepAction

		return(actionList)

	"""*********************************"""
	""" 	    GETTER METHODS 	    """
	"""*********************************"""

	def getFileActions(self):

		actionList = self.addSeparators([self.newAction, self.saveAction, self.openAction, self.restartAction, self.exitAction])

		return (actionList)
	
	def getEditActions(self):
		actionList = self.addSeparators([self.backAction, self.themeAction])

		return (actionList)

	def getHelpActions(self):
		actionList = self.addSeparators([self.howToAction, self.aboutAction])

		return (actionList)

	def getToolbarActions(self):
		actionList = self.addSeparators([self.newAction, self.saveAction, self.openAction, self.backAction])

		return (actionList)

	"""*************************************************************"""
	""" 			HELPER ACTIONS 				"""
	"""*************************************************************"""
	def getIsModified(self):
		return (self.isModified)

	def setIsModified(self):
		mod = self.getIsModified()
		if (mod == 0):
			self.isModified = 1
		return

	def resetIsModified(self):
		self.isModified = 0

	def saveMessageBox(self):
		saveMessageBox = QMessageBox()
		saveMessageBox.setText("Your MadLib has been modified.  Would you like to save?")
		saveMessageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		saveMessageBox.setDefaultButton(QMessageBox.Yes)
		val = saveMessageBox.exec_()
		if (val == QMessageBox.Yes):
			return(1)
		else:
			return(0)

