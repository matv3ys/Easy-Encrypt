# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_plug.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 583)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(25, 21, 311, 481))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("border: 1px solid;\n"
"border-color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 550, 193, 28))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pshb_Random = QtWidgets.QPushButton(Dialog)
        self.pshb_Random.setGeometry(QtCore.QRect(30, 510, 301, 28))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.pshb_Random.setFont(font)
        self.pshb_Random.setObjectName("pshb_Random")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Подключения"))
        self.pshb_Random.setText(_translate("Dialog", "Случайные подключения"))
