# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.py'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import mywindow
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mwin = mywindow()
    mwin.show()
    sys.exit(app.exec_())
