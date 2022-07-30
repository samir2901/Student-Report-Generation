from PyQt5 import QtCore, QtGui, QtWidgets
from data_entry_prep import * 
from generate_report import * 
from update_data_ui import * 

class Ui_UiSelector(object):
    def setupUi(self, UiSelector):
        UiSelector.setObjectName("UiSelector")
        UiSelector.resize(547, 297)
        UiSelector.setMaximumSize(QtCore.QSize(547, 297))
        self.centralwidget = QtWidgets.QWidget(UiSelector)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 170, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 60, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 180, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        UiSelector.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UiSelector)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 21))
        self.menubar.setObjectName("menubar")
        UiSelector.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UiSelector)
        self.statusbar.setObjectName("statusbar")
        UiSelector.setStatusBar(self.statusbar)

        self.retranslateUi(UiSelector)
        QtCore.QMetaObject.connectSlotsByName(UiSelector)

        self.pushButton.clicked.connect(self.openDataEntryWindow)
        
        self.pushButton_3.clicked.connect(self.openGenerateReportWindow)

    def retranslateUi(self, UiSelector):
        _translate = QtCore.QCoreApplication.translate
        UiSelector.setWindowTitle(_translate("UiSelector", "UI Selector"))
        self.pushButton.setText(_translate("UiSelector", "Data Entry"))
        
        self.pushButton_3.setText(_translate("UiSelector", "Generate Report"))
        self.label.setText(_translate("UiSelector", "Select this for data entry"))
        
        self.label_3.setText(_translate("UiSelector", "Select this for generating report"))

    def openDataEntryWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.dataEntryWindowUI = Ui_DataEntryWindow()
        self.dataEntryWindowUI.setupUi(self.window)
        self.window.show()
                     
    
    def openGenerateReportWindow(self):        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GenerateReportWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        