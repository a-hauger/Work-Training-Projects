#!/usr/bin/env python3

from FormMainWidget import MainWidget
from FormActions import Actions
from FormHowTo import howToDialog
from FormAbout import aboutDialog
from FormThemeChange import themeChange
from FormDockWidgets import docks
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)

		self.actions= Actions()

		self.mainWidget = MainWidget()



		self.theme = themeChange()

		self.isModified = 0
		"""*************************************************************************"""
		""" 			CREATE AND SET STYLE SHEETS 			    """
		"""*************************************************************************"""
		defaultStyle = self.theme.getStyleSheet()
		self.setStyleSheet(defaultStyle)
		"""*************************************************************************"""
		""" 			CREATE WINDOW TITLE, MENU, STATUS BARS 		    """
		"""*************************************************************************"""
		#window
		self.setWindowTitle("MadLibs!")
		self.resize(500, 600)
		self.setCentralWidget(self.mainWidget)

		self.tools = QToolBar()
		self.tools.addActions(self.actions.getToolbarActions())

		self.addToolBar(self.tools)
	
		#Menu Bar	
		self.fileMenu = QMenu("&File")
		self.fileMenu.addActions(self.actions.getFileActions())

		self.editMenu = QMenu("&Edit")
		self.editMenu.addActions(self.actions.getEditActions())
	
		self.helpMenu = QMenu("&Help")
		self.helpMenu.addActions(self.actions.getHelpActions())
	
		self.menuBar().addMenu(self.fileMenu)
		self.menuBar().addMenu(self.editMenu)
		self.menuBar().addMenu(self.helpMenu)
		
		#status bar
		self.statusLabel = QLabel("Main Page")
		self.statusBar().insertWidget(0, self.statusLabel)

		#file actions
		self.actions.exitAction.triggered.connect(self.exitMadLib)
		self.actions.newAction.triggered.connect(self.newMadLib)
		self.actions.restartAction.triggered.connect(self.restartMadLib)
		self.actions.saveAction.triggered.connect(self.saveMadLib)
		self.actions.openAction.triggered.connect(self.openMadLib)

		#help actions
		self.actions.howToAction.triggered.connect(self.howTo)
		self.actions.aboutAction.triggered.connect(self.aboutMadLib)

		#edit actions
		self.actions.backAction.triggered.connect(self.backAction)
		self.actions.themeAction.triggered.connect(self.themeChangeBox)
		
		#push button actions
		self.mainWidget.mainPage.moveToFormButton.clicked.connect(self.moveToAction)
		self.mainWidget.closeButton.clicked.connect(self.exitMadLib)

		self.mainWidget.firstPage.generateMadLib.clicked.connect(self.generateAction)
		self.mainWidget.secondPage.againButton.clicked.connect(self.againAction)

		self.mainWidget.thirdPage.generateMadLib.clicked.connect(self.generateAction)
		self.mainWidget.fourthPage.againButton.clicked.connect(self.againAction)

		"""**************************************************************************"""
		""" 	      CREATE LINE EDIT CHANGE CONNECTIONS FOR 1ST PAGE 		     """
		"""**************************************************************************"""
		
		for textbox in self.mainWidget.firstPage.textboxList:
			textbox.textEdited.connect(self.actions.setIsModified)

		"""**************************************************************************"""
		""" 	   CREATE LINE EDIT CHANGE CONNECTIONS FOR 3RD PAGE 	             """
		"""**************************************************************************"""

		for textbox in self.mainWidget.thirdPage.textboxList:
			textbox.textEdited.connect(self.actions.setIsModified)
 
	"""********************************************************************************"""
	"""  				BUTTON PRESS ACTIONS 				   """
	"""********************************************************************************"""

	"""************"""
	"""FILE ACTIONS"""
	"""************"""
	def exitMadLib(self):
		index = self.mainWidget.mainPage.comboBox.currentIndex()
		if (index == 1 or index ==2):
			textList = self.mainWidget.firstPage.getTextBoxData()
		elif (index == 3 or index ==3):
			textList = self.mainWidget.thirdPage.getTextBoxData()

		mod = self.actions.getIsModified()
		if (mod == 1):
			retval = self.actions.saveMessageBox()

			if (retval == 0):
				self.close()
			else:
				self.saveMadLib()
				self.close()

		else:
			self.close()

		return

	def newMadLib(self):
		mod = self.actions.getIsModified()
		if (mod == 1):
			self.retval = self.actions.saveMessageBox()
			if (self.retval == 0):
				self.actions.resetIsModified()
				self.mainWidget.firstPage.setTextBoxData()
				self.mainWidget.thirdPage.setTextBoxData()
				self.mainWidget.Stack.setCurrentIndex(0)

			else:
				self.saveMadLib()
				self.mainWidget.firstPage.setTextBoxData()
				self.mainWidget.thirdPage.setTextBoxData()
				self.mainWidget.Stack.setCurrentIndex(0)
				self.actions.resetIsModified()
		else:
			self.mainWidget.firstPage.setTextBoxData()
			self.mainWidget.thirdPage.setTextBoxData()
			self.mainWidget.Stack.setCurrentIndex(0)

		return

	def restartMadLib(self):

		if (self.mainWidget.Stack.currentIndex() == 2):
			self.mainWidget.Stack.setCurrentIndex(1)
			self.mainWidget.firstPage.setTextBoxData()

		elif (self.mainWidget.Stack.currentIndex() == 4):
			self.mainWidget.Stack.setCurrentIndex(3)
			self.mainWidget.thirdPage.setTextBoxData()
		else:
			self.mainWidget.Stack.setCurrentIndex(0)
			self.mainWidget.firstPage.setTextBoxData()
			self.mainWidget.thirdPage.setTextBoxData()
	
		self.mainWidget.scrollArea.verticalScrollBar().setValue(0)
		return

	def saveMadLib(self):
		index = self.mainWidget.mainPage.comboBox.currentIndex()
		if (index == 1):
			textList = self.mainWidget.firstPage.getTextBoxData()
		elif (index == 2):
			textList = self.mainWidget.thirdPage.getTextBoxData()
		else:
			self.retryMessageBox = QMessageBox()
			self.retryMessageBox.setText("You are on the Main Page, there is nothing to save!")
			self.retryMessageBox.setStandardButtons(QMessageBox.Ok)
			self.retryMessageBox.exec_()
			return

		fileName = QFileDialog.getSaveFileName(self, "Save MadLib!", "", "Comma Separated Value(*.csv)")
		if (fileName == None):
			return
		else:
			i = index
			if not fileName[0].endswith(".csv"):
				writeName = fileName[0] + ".csv"
			else:
				writeName = fileName[0]

			with open(writeName, mode = "w") as WRITE_FILE:
				if (i==1):
					WRITE_FILE.write("{0}\n".format(1))
					for word in textList:
						WRITE_FILE.write("{0}\n".format(word))
				elif (i==2):
					WRITE_FILE.write("{0}\n".format(2))
					for word in textList:
						WRITE_FILE.write("{0}\n".format(word))
				else:
					return
			WRITE_FILE.close()
		self.actions.resetIsModified()
		return
			
	def openMadLib(self):
		textList = []
		index = 0
		fileName = QFileDialog.getOpenFileName(self,"Open Madlib!", "", "Comma Separated Value (*.csv)")
		if (fileName[0] == ""):
			return
		else:
			with open(fileName[0], mode = "r") as READ_FILE:
				for i, line in enumerate(READ_FILE):
					if (i == 0):
						index = int(line)
					else:
						textList.append(line.strip('\n'))
		READ_FILE.close()
	
		if (index == 1):
			self.mainWidget.Stack.setCurrentIndex(1)
			textList.append(line.strip('\n'))
			self.statusLabel.setText("Thanksgiving Day!")
			self.mainWidget.scrollArea.verticalScrollBar().setValue(0)
			self.mainWidget.firstPage.setOpenData(textList)
		if (index == 2):
			self.mainWidget.Stack.setCurrentIndex(3)
			textList.append(line.strip('\n'))
			self.statusLabel.setText("Our Solar System!")
			self.mainWidget.scrollArea.verticalScrollBar().setValue(0)
			self.mainWidget.thirdPage.setOpenData(textList)
		return

	"""************"""
	"""HELP ACTIONS"""
	"""************"""
	def howTo(self):
		style = self.theme.getStyleSheet()
		self.howTo = howToDialog(style)

		return

	def aboutMadLib(self):
		style = self.theme.getStyleSheet()
		self.about = aboutDialog(style)
		return
	"""************"""
	"""EDIT ACTIONS"""
	"""************"""
	def backAction(self):
		if (self.mainWidget.Stack.currentIndex() == 1):
			self.mainWidget.Stack.setCurrentIndex(0)

		elif (self.mainWidget.Stack.currentIndex() == 2):
			self.mainWidget.Stack.setCurrentIndex(1)

		elif (self.mainWidget.Stack.currentIndex() == 3):
			self.mainWidget.Stack.setCurrentIndex(0)

		elif (self.mainWidget.Stack.currentIndex() == 4):
			self.mainWidget.Stack.setCurrentIndex(3)

		self.mainWidget.scrollArea.verticalScrollBar().setValue(0)
		return

	def themeChangeBox(self):
		#theme = themeChange()
		self.theme.exec_()
		newStyle = self.theme.getStyleSheet()
		
		self.setStyleSheet(newStyle)

	"""**********************"""
	"""GENERAL BUTTON ACTIONS"""
	"""**********************"""
		
	def moveToAction(self):
		i = self.mainWidget.mainPage.comboBox.currentIndex()

		if (i == 1):
			self.mainWidget.Stack.setCurrentIndex(1)
			self.statusLabel.setText("Thanksgiving Day!")
			self.mainWidget.scrollArea.verticalScrollBar().setValue(0)

		elif (i == 2):
			self.mainWidget.Stack.setCurrentIndex(3)
			self.statusLabel.setText("Our Solar System!")		
			self.mainWidget.scrollArea.verticalScrollBar().setValue(0)

		else:
			self.messageBox = QMessageBox()
			self.messageBox.setText("You must choose a Mad Lib to complete!")
			self.messageBox.setStandardButtons(QMessageBox.Retry)
			self.messageBox.setDefaultButton(QMessageBox.Retry)
			self.messageBox.exec_()

	def generateAction(self):
		textList = []

		if (self.mainWidget.Stack.currentIndex() == 1):

			textList = self.mainWidget.firstPage.getTextBoxData()	
			self.mainWidget.secondPage.setTextBoxData(textList)
			self.mainWidget.Stack.setCurrentIndex(2)

			self.mainWidget.scrollArea.verticalScrollBar().setValue(0)

		elif (self.mainWidget.Stack.currentIndex() == 3):

			textList = self.mainWidget.thirdPage.getTextBoxData()
			self.mainWidget.fourthPage.setTextBoxData(textList)
			self.mainWidget.Stack.setCurrentIndex(4)

			self.mainWidget.scrollArea.verticalScrollBar().setValue(0)

		return


	def againAction(self):
		mod = self.actions.getIsModified()	
		if (mod == 1):
			retval = self.actions.saveMessageBox()
			if (retval == 0):
				self.mainWidget.firstPage.setTextBoxData()
				self.mainWidget.thirdPage.setTextBoxData()
				self.mainWidget.Stack.setCurrentIndex(0)
				self.mainWidget.scrollArea.verticalScrollBar().setValue(0)
				self.statusLabel.setText("Main Page!")		
				self.isModified = 0

			else:
				self.saveAction()
				self.mainWidget.firstPage.setTextBoxData()
				self.mainWidget.thirdPage.setTextBoxData()
				self.mainWidget.Stack.setCurrentIndex(0)
				self.mainWidget.Stack.setCurrentIndex(0)
				self.mainWidget.scrollArea.verticalScrollBar().setValue(0)
				self.statusLabel.setText("Main Page!")
				self.isModified = 0

		else:
			self.mainWidget.firstPage.setTextBoxData()
			self.mainWidget.thirdPage.setTextBoxData()
			self.mainWidget.Stack.setCurrentIndex(0)
			self.mainWidget.scrollArea.verticalScrollBar().setValue(0)
			self.statusLabel.setText("Main Page!")
		return



