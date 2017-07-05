#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class themeChange(QDialog):
	def __init__(self):
		QDialog.__init__(self)
	
		self.sheet = "QMenuBar{background-color: #232121;}\
				QMenuBar::item{background-color: #232121;}\
				QMenuBar::item:selected{background-color: #504b4b;}\
				QMenu{background-color: #232121;}\
				QWidget{background-color: #232121;}\
				QToolBar::handle{background-color: #504b4b;}\
				QToolBar{background-color:#232121; border: none;}\
				QScrollBar:horizontal, QScrollBar:vertical{border: 2px solid #232121; border-radius: 5px; border-width: 1px;}\
				QScrollBar::handle:horizontal, QScrollBar::handle:vertical{background: #504b4b; border-color: 1px solid black; border-radius: 5px;}\
				QScrollBar::add-line:horizontal{background-color: #232121; border: 1px solid #232121; border-radius: 5px; width: 16px;}\
				QScrollBar::add-line:vertical{background-color: #232121; border: 1px solid #232121; border-radius: 5px; height: 16px;}\
				QScrollBar::sub-line:horizontal{background-color: #232121; border: 1px solid #232121; border-radius: 5px; width: 16px;}\
				QScrollBar::sub-line:vertical{background-color: #232121; border: 1px solid #232121; border-radius: 5px; height: 16px;}\
				QLabel{color: #ffffff;}\
				QPushButton{background-color: #504b4b; border-style: solid; border-width: 1px; border-radius: 10px; border-color: #000000;}\
				QLineEdit{background-color: #504b4b; border: 2px solid #232121; border-radius: 10px;}\
				QStatusBar::item{border: None;}\
				QDialog{background-color: #232121; border: 1px solid gray; border-radius: 10px}\
				QMessageBox{background-color: #232121; border: 1px solid black; border-radius: 10px}\
				QGroupBox{background-color: #232121; border: 1px solid black; border-radius: 10px}\
				QComboBox{border: 1px solid black; border-radius: 3px; padding: 1px 18px 1px 3px; min-width: 6em;}\
				QComboBox:editable{background:white;}\
				QComboBox:!editable, QComboBox::drop-down:editable{background: #504b4b;}\
				QComboBox:!editable:on, QComboBox::drop-down:editable:on{background: #232121;}\
				QComboBox::drop-down{subcontrol-origin: padding; subcontrol-position: top right; width 15px; border: 1px solid #504b4b; border-radius: 3px;}\
				QProgressBar{border: 1px solid #232121; border-radius: 5px; text-align: center}\
				QProgressBar::chunk{background-color: #504b4b; width: 10px; margin: 1px;}"
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
		return

	def changeTheme(self):
		if (self.changeThemeRed.isChecked()):
			#change theme to red
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
                                QGroupBox{background-color: #230000; border: 1px solid #cd5359; border-radius: 10px}\
				QScrollBar:horizontal, QScrollBar:vertical{border: 2px solid #230000; border-radius: 5px; border-width: 1px;}\
				QScrollBar::handle:horizontal, QScrollBar::handle:vertical{background: #500000; border-color: 1px solid black; border-radius: 5px;}\
				QScrollBar::add-line:horizontal{background-color: #230000; border: 1px solid #230000; border-radius: 5px; width: 16px;}\
				QScrollBar::add-line:vertical{background-color: #230000; border: 1px solid #230000; border-radius: 5px; height: 16px;}\
				QScrollBar::sub-line:horizontal{background-color: #230000; border: 1px solid #230000; border-radius: 5px; width: 16px;}\
				QScrollBar::sub-line:vertical{background-color: #230000; border: 1px solid #230000; border-radius: 5px; height: 16px;}\
				QToolBar::handle{background-color: #500000;}\
				QToolBar{background-color:#230000; border: none;}\
				QComboBox{border: 1px solid #cd5359; border-radius: 3px; padding: 1px 18px 1px 3px; min-width: 6em;}\
				QComboBox:editable{background:white;}\
				QComboBox:!editable, QComboBox::drop-down:editable{background: #500000;}\
				QComboBox:!editable:on, QComboBox::drop-down:editable:on{background: #230000;}\
				QComboBox::drop-down{subcontrol-origin: padding; subcontrol-position: top right; width 15px; border: 1px solid #500000; border-radius: 3px;}\
				QProgressBar{border: 1px solid #230000; border-radius: 5px; text-align: center}\
				QProgressBar::chunk{background-color: #500000; width: 10px; margin: 1px;}"

		elif (self.changeThemeGreen.isChecked()):
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
                                QGroupBox{background-color: #002300; border: 1px solid #53cd69; border-radius: 10px}\
				QScrollBar:horizontal, QScrollBar:vertical{border: 2px solid #002300; border-radius: 5px; border-width: 1px;}\
				QScrollBar::handle:horizontal, QScrollBar::handle:vertical{background: #00500b; border-color: 1px solid black; border-radius: 5px;}\
				QScrollBar::add-line:horizontal{background-color: #002300; border: 1px solid #002300; border-radius: 5px; width: 16px;}\
				QScrollBar::add-line:vertical{background-color: #002300; border: 1px solid #002300; border-radius: 5px; height: 16px;}\
				QScrollBar::sub-line:horizontal{background-color: #002300; border: 1px solid #002300; border-radius: 5px; width: 16px;}\
				QScrollBar::sub-line:vertical{background-color: #002300; border: 1px solid #002300; border-radius: 5px; height: 16px;}\
				QToolBar::handle{background-color: #00500b;}\
				QToolBar{background-color:#002300; border: none;}\
QComboBox{border: 1px solid #53cd69; border-radius: 3px; padding: 1px 18px 1px 3px; min-width: 6em;}\
                                QComboBox:editable{background:white;}\
                                QComboBox:!editable, QComboBox::drop-down:editable{background: #00500b;}\
                                QComboBox:!editable:on, QComboBox::drop-down:editable:on{background: #002300;}\
                                QComboBox::drop-down{subcontrol-origin: padding; subcontrol-position: top right; width 15px; border: 1px solid #00500b; border-radius: 3px;}\
				QProgressBar{border: 1px solid #002300; border-radius: 5px; text-align: center}\
				QProgressBar::chunk{background-color: #00500b; width: 10px; margin: 1px}"

		elif (self.changeThemeBlue.isChecked()):
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
                                QGroupBox{background-color: #000423; border: 1px solid #535acd; border-radius: 10px}\
				QScrollBar:horizontal, QScrollBar:vertical{border: 2px solid #000423; border-radius: 5px; border-width: 1px;}\
				QScrollBar::handle:horizontal, QScrollBar::handle:vertical{background: #020050; border-color: 1px solid black; border-radius: 5px;}\
				QScrollBar::add-line:horizontal{background-color: #000423; border: 1px solid #000423; border-radius: 5px; width: 16px;}\
				QScrollBar::add-line:vertical{background-color: #000423; border: 1px solid #000423; border-radius: 5px; height: 16px;}\
				QScrollBar::sub-line:horizontal{background-color: #000423; border: 1px solid #000423; border-radius: 5px; width: 16px;}\
				QScrollBar::sub-line:vertical{background-color: #000423; border: 1px solid #000423; border-radius: 5px; height: 16px;}\
				QToolBar::handle{background-color: #020050;}\
				QToolBar{background-color:#000423; border: none;}\
				QComboBox{border: 1px solid #535acd; border-radius: 3px; padding: 1px 18px 1px 3px; min-width: 6em;}\
				QComboBox:editable{background:white;}\
				QComboBox:!editable, QComboBox::drop-down:editable{background: #020050;}\
				QComboBox:!editable:on, QComboBox::drop-down:editable:on{background: #000423;}\
				QComboBox::drop-down{subcontrol-origin: padding; subcontrol-position: top right; width 15px; border: 1px solid #020050; border-radius: 3px;}\
				QProgressBar{border: 1px solid #000423; border-radius: 5px; text-align: center}\
				QProgressBar::chunk{background-color: #020050; width: 10px; margin: 1px}"

		elif (self.changeThemeDefault.isChecked()):
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
				QMessageBox{color: #232121; border: 1px solid gray; border-radius: 10px}\
				QGroupBox{background-color: #232121; border: 1px solid black; border-radius: 10px}\
				QScrollBar:horizontal, QScrollBar:vertical{border: 2px solid #232121; border-radius: 5px; border-width: 1px;}\
				QScrollBar::handle:horizontal, QScrollBar::handle:vertical{background: #504b4b; border-color: 1px solid black; border-radius: 5px;}\
				QScrollBar::add-line:horizontal{background-color: #232121; border: 1px solid #232121; border-radius: 5px; width: 16px;}\
				QScrollBar::add-line:vertical{background-color: #232121; border: 1px solid #232121; border-radius: 5px; height: 16px;}\
				QScrollBar::sub-line:horizontal{background-color: #232121; border: 1px solid #232121; border-radius: 5px; width: 16px;}\
				QScrollBar::sub-line:vertical{background-color: #232121; border: 1px solid #232121; border-radius: 5px; height: 16px;}\
				QToolBar::handle{background-color: #504b4b;}\
				QToolBar{background-color:#232121; border: none;}\
				QComboBox{border: 1px solid black; border-radius: 3px; padding: 1px 18px 1px 3px; min-width: 6em;}\
				QComboBox:editable{background:white;}\
				QComboBox:!editable, QComboBox::drop-down:editable{background: #504b4b;}\
				QComboBox:!editable:on, QComboBox::drop-down:editable:on{background: #232121;}\
				QComboBox::drop-down{subcontrol-origin: padding; subcontrol-position: top right; width 15px; border: 1px solid #504b4b; border-radius: 3px;}\
				QProgressBar{border: 1px solid #232121; border-radius: 5px; text-align: center}\
				QProgressBar::chunk{background-color: #504b4b; width: 10px; margin: 1px;}"

		else:
			self.sheet = "QMenuBar{background-color: #232121;}\
				QMenuBar::item{background-color: #232121;}\
				QMenuBar::item:selected{background-color: #504b4b;}\
				QMainWindow{background-color: #232121;}\
				QWidget{background-color: #232121;}\
				QLabel{color: #ffffff;}\
				QPushButton{background-color: #504b4b; border-style: solid; border-width: 1px; border-radius: 10px; border-color: #000000;}\
				QLineEdit{background-color: #504b4b; border: 2px solid #232121; border-radius: 10px;}\
				QStatusBar::item{border: None;}\
				QDialog{background-color: #232121; border: 1px solid gray; border-radius: 10px}\
				QMessageBox{color: #232121; border: 1px solid black; border-radius: 10px}\
				QGroupBox{background-color: #232121; border: 1px solid black; border-radius: 10px}\
				QScrollBar:horizontal, QScrollBar:vertical{border: 2px solid #232121; border-radius: 5px; border-width: 1px;}\
				QScrollBar::handle:horizontal, QScrollBar::handle:vertical{background: #504b4b; border-color: 1px solid black; border-radius: 5px;}\
				QScrollBar::add-line:horizontal{background-color: #232121; border: 1px solid #232121; border-radius: 5px; width: 16px;}\
				QScrollBar::add-line:vertical{background-color: #232121; border: 1px solid #232121; border-radius: 5px; height: 16px;}\
				QScrollBar::sub-line:horizontal{background-color: #232121; border: 1px solid #232121; border-radius: 5px; width: 16px;}\
				QScrollBar::sub-line:vertical{background-color: #232121; border: 1px solid #232121; border-radius: 5px; height: 16px;}\
				QToolBar::handle{background-color: #504b4b;}\
				QToolBar{background-color:#232121; border: none;}\
				QComboBox{border: 1px solid black; border-radius: 3px; padding: 1px 18px 1px 3px; min-width: 6em;}\
				QComboBox:editable{background:white;}\
				QComboBox:!editable, QComboBox::drop-down:editable{background: #504b4b;}\
				QComboBox:!editable:on, QComboBox::drop-down:editable:on{background: #232121;}\
				QComboBox::drop-down{subcontrol-origin: padding; subcontrol-position: top right; width 15px; border: 1px solid #504b4b; border-radius: 3px;}\
				QProgressBar{border:1px solid #232121; border-radius: 5px; text-align: center;}\
				QProgressBar::chunk{background-color: #504b4b; width: 10px; margin: 1px}"

		self.close()

	def getStyleSheet(self):
		return(self.sheet)
