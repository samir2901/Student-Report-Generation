from PyQt5 import QtCore, QtGui, QtWidgets
from firebase import login
from ui_selector import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):                
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(291, 227)
        MainWindow.setMaximumSize(QtCore.QSize(291, 227))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.userNameLabel = QtWidgets.QLabel(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.userNameLabel.setFont(font)
        self.userNameLabel.setObjectName("userNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.userNameLabel)
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)       
        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.userNameInput = QtWidgets.QLineEdit(self.centralwidget)
        
        
        font = QtGui.QFont()
        font.setPointSize(16)
        self.userNameInput.setFont(font)
        self.userNameInput.setObjectName("userNameInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.userNameInput)
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        
        
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordInput.setFont(font)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.passwordInput)
        
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setEnabled(True)
        self.loginBtn.setMaximumSize(QtCore.QSize(100, 400))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loginBtn.setFont(font)
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.clicked.connect(self.login)


        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.loginBtn)
        self.title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")


        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.title)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 291, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Report Generation"))
        self.userNameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.loginBtn.setText(_translate("MainWindow", "Login"))
        self.title.setText(_translate("MainWindow", "LOGIN"))

    def login(self):
        username = self.userNameInput.text()
        password = self.passwordInput.text()
        x = login(username,password)
        msg = QtWidgets.QMessageBox()
        if x:            
            self.openUiSelector()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Success!")
            msg.setText("Login successful!")
            msg.exec_()            
        else:
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Error!")
            msg.setText("Invalid password or username")
            msg.exec_()
        
    def openUiSelector(self):
        self.window = QtWidgets.QMainWindow()
        self.uiSelector = Ui_UiSelector()
        self.uiSelector.setupUi(self.window)
        self.window.show()
        pass
    
    
