#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from FormMainWindow import MainWindow
from FormThemeChange import *
import sys

def main():
	app = QApplication([])
	mainWindow = MainWindow()
	
	mainWindow.show()
	exit(app.exec_())

if (__name__ == "__main__"):
	main()
