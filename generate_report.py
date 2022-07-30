from PyQt5 import QtCore, QtGui, QtWidgets
from firebase import * 

class Ui_GenerateReportWindow(object):
    def setupUi(self, GenerateReportWindow):
        GenerateReportWindow.setObjectName("GenerateReportWindow")
        GenerateReportWindow.resize(506, 234)
        GenerateReportWindow.setMaximumSize(QtCore.QSize(506, 234))
        self.centralwidget = QtWidgets.QWidget(GenerateReportWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.clss = QtWidgets.QLineEdit(self.centralwidget)
        self.clss.setGeometry(QtCore.QRect(130, 40, 321, 20))
        self.clss.setObjectName("clss")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 71, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.section = QtWidgets.QLineEdit(self.centralwidget)
        self.section.setGeometry(QtCore.QRect(130, 80, 321, 20))
        self.section.setObjectName("section")
        self.rptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.rptBtn.setGeometry(QtCore.QRect(190, 140, 101, 31))
        self.rptBtn.setObjectName("rptBtn")
        self.rptBtn.clicked.connect(self.genRpt)
        GenerateReportWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GenerateReportWindow)
        QtCore.QMetaObject.connectSlotsByName(GenerateReportWindow)

    def retranslateUi(self, GenerateReportWindow):
        _translate = QtCore.QCoreApplication.translate
        GenerateReportWindow.setWindowTitle(_translate("GenerateReportWindow", "GenerateReport"))
        self.label.setText(_translate("GenerateReportWindow", "Class"))
        self.label_2.setText(_translate("GenerateReportWindow", "Section"))
        self.rptBtn.setText(_translate("GenerateReportWindow", "Generate Report"))

    def genRpt(self):
        c = self.clss.text()
        sec = self.section.text()
        msg = QtWidgets.QMessageBox()
        try:
            datalist = getData(c,sec)
            for data in datalist:
                student = getStudent(c,sec,data)
                generateReport(student)    
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Success!")
            msg.setText("Report Generation Successful!!")
            msg.exec_() 
        except:
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Error!")
            msg.setText("Error in generating report!")
            msg.exec_()