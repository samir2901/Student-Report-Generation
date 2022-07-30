from firebase_config import *
import pyrebase
from student import ClassPrepStudent
from firebase import *
from PyQt5 import QtCore, QtGui, QtWidgets
from login import *
from generate_report import * 
import sys 

if __name__ == "__main__":     
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  ui = Ui_MainWindow()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec_())  
  
  
  
  
  
  


    





