from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from mainwindow_form import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

    #定义槽函数
    def pushbtn_clicked(self):
        self.textEdit.setText("The end of the fucking world.")

