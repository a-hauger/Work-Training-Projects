#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class themeChange(QDialog):
	def __init__(self):
		QDialog.__init__(self)
	
		self.sheet = ""

		self.createDialog()

	def createDialog(self):
		self.setWindowTitle("Change Theme!")

		self.titleFont = QFont("Helvetica", 14)
		self.titleFont.setItalic(True)

		self.titleText = QLabel("Choose the theme you would like:")
		self.titleText.setFont(self.titleFont)

		self.radioGroupBox = QGroupBox()
		self.changeThemeRed = QRadioButton("Red")
		self.changeThemeGreen = QRadioButton("Green")
		self.changeThemeBlue = QRadioButton("Blue")
		self.changeThemeDefault = QRadioButton("Default")

		self.changeThemePush = QPushButton("Change!")

		self.mainLayout = QVBoxLayout(self)
		self.radioButtonLayout = QHBoxLayout()

		self.mainLayout.addWidget(self.titleText, alignment = Qt.AlignCenter)

		self.radioButtonLayout.addWidget(self.changeThemeRed)
		self.radioButtonLayout.addWidget(self.changeThemeGreen)
		self.radioButtonLayout.addWidget(self.changeThemeBlue)
		self.radioButtonLayout.addWidget(self.changeThemeDefault)

		self.radioGroupBox.setLayout(self.radioButtonLayout)
		
		self.mainLayout.addWidget(self.radioGroupBox)
		self.mainLayout.addWidget(self.changeThemePush, alignment = Qt.AlignCenter)

		self.setLayout(self.mainLayout)

		styleSheet = self.changeThemePush.clicked.connect(self.changeTheme)
		print(styleSheet)
		return

	def changeTheme(self):
		print("You are in change theme!")
		if (self.changeThemeRed.isChecked()):
			#change theme to red
			print("Change color to red~!")
			self.sheet = "QMenuBar{background-color: #230000;}\
                                QMenuBar::item{background-color: #230000;}\
                                QMenuBar::item:selected{background-color: #500000;}\
                                QMainWindow{background-color: #230000;}\
                                QWidget{background-color: #230000;}\
                                QLabel{color: #ffffff;}\
                                QPushButton{background-color: #500000; border-style: solid; border-width: 1px; border-radius: 10px; border-color: #cd5359;}\
                                QLineEdit{background-color: #500000; border: 2px solid #cd5359; border-radius: 10px;}\
                                QStatusBar::item{border: None;}\
                                QDialog{background-color: #230000; border: 1px solid #cd5359; border-radius: 10px}\
                                QMessageBox{color: #230000; border: 1px solid #cd5359; border-radius: 10px}\
                                QGroupBox{background-color: #230000; border: 1px solid #cd5359; border-radius: 10px}"

		elif (self.changeThemeGreen.isChecked()):
			print("Change color to green~!")
			#change theme to green
			self.sheet = "QMenuBar{background-color: #002300;}\
                                QMenuBar::item{background-color: #002300;}\
                                QMenuBar::item:selected{background-color: #00500b;}\
                                QMainWindow{background-color: #002300;}\
                                QWidget{background-color: #002300;}\
                                QLabel{color: #ffffff;}\
                                QPushButton{background-color: #00500b; border-style: solid; border-width: 1px; border-radius: 10px; border-color: #53cd69;}\
                                QLineEdit{background-color: #002300; border: 2px solid #53cd69; border-radius: 10px;}\
                                QStatusBar::item{border: None;}\
                                QDialog{background-color: #002300; border: 1px solid #53cd69; border-radius: 10px}\
                                QMessageBox{color: #002300; border: 1px solid #53cd69; border-radius: 10px}\
                                QGroupBox{background-color: #002300; border: 1px solid #53cd69; border-radius: 10px}"

		elif (self.changeThemeBlue.isChecked()):
			print("Change color to blue~!")
			#change theme to blue
			self.sheet = "QMenuBar{background-color: #000423;}\
                                QMenuBar::item{background-color: #000423;}\
                                QMenuBar::item:selected{background-color: #020050;}\
                                QMainWindow{background-color: #000423;}\
                                QWidget{background-color: #000423;}\
                                QLabel{color: #ffffff;}\
                                QPushButton{background-color: #020050; border-style: solid; border-width: 1px; border-radius: 10px; border-color: #535acd;}\
                                QLineEdit{background-color: #020050; border: 2px solid #535acd; border-radius: 10px;}\
                                QStatusBar::item{border: None;}\
                                QDialog{background-color: #000423; border: 1px solid #535acd; border-radius: 10px}\
                                QMessageBox{color: #000423; border: 1px solid #535acd; border-radius: 10px}\
                                QGroupBox{background-color: #000423; border: 1px solid #535acd; border-radius: 10px}"

		elif (self.changeThemeDefault.isChecked()):
			print("Change color to default~!")
			self.sheet = "QMenuBar{background-color: #232121;}\
				QMenuBar::item{background-color: #232121;}\
				QMenuBar::item:selected{background-color: #504b4b;}\
				QMainWindow{background-color: #232121;}\
				QWidget{background-color: #232121;}\
				QLabel{color: #ffffff;}\
				QPushButton{background-color: #504b4b; border-style: solid; border-width: 1px; border-radius: 10px; border-color: #000000;}\
				QLineEdit{background-color: #504b4b; border: 2px solid #232121; border-radius: 10px;}\
				QStatusBar::item{border: None;}\
				QDialog{background-color: #232121; border: 1px solid black; border-radius: 10px}\
				QMessageBox{color: #232121; border: 1px solid black; border-radius: 10px}\
				QGroupBox{background-color: #232121; border: 1px solid black; border-radius: 10px}"

		else:
			print("No Color Change~!")
			self.sheet = "QMenuBar{background-color: #232121;}\
				QMenuBar::item{background-color: #232121;}\
				QMenuBar::item:selected{background-color: #504b4b;}\
				QMainWindow{background-color: #232121;}\
				QWidget{background-color: #232121;}\
				QLabel{color: #ffffff;}\
				QPushButton{background-color: #504b4b; border-style: solid; border-width: 1px; border-radius: 10px; border-color: #000000;}\
				QLineEdit{background-color: #504b4b; border: 2px solid #232121; border-radius: 10px;}\
				QStatusBar::item{border: None;}\
				QDialog{background-color: #232121; border: 1px solid black; border-radius: 10px}\
				QMessageBox{color: #232121; border: 1px solid black; border-radius: 10px}\
				QGroupBox{background-color: #232121; border: 1px solid black; border-radius: 10px}"

		#print(sheet)
		self.close()

	def getStyleSheet(self):
		return(self.sheet)
