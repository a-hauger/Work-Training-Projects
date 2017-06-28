#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Actions(QObject):
	def __init__(self):
		QObject.__init__(self)

		

		self.isModified = 0

		#file actions
		self.newAction = QAction("New", self)
		self.restartAction = QAction("Restart", self)
		self.saveAction = QAction("Save", self)
		self.openAction = QAction("Open", self)
		self.exitAction = QAction("Exit", self)

		#edit actions
		self.backAction = QAction("Back", self)
		self.themeAction = QAction("Themes", self)

		#help actions
		self.howToAction = QAction("How To", self)
		self.aboutAction = QAction("About", self)

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

