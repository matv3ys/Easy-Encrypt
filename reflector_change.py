# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reflector_change.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 141)
        self.lineEdit_Reflector = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Reflector.setGeometry(QtCore.QRect(20, 20, 401, 31))
        self.lineEdit_Reflector.setStyleSheet("border: 3px solid;\n"
"border-color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_Reflector.setObjectName("lineEdit_Reflector")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(18, 60, 401, 80))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pshb_Random_reflector = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.pshb_Random_reflector.setFont(font)
        self.pshb_Random_reflector.setObjectName("pshb_Random_reflector")
        self.horizontalLayout.addWidget(self.pshb_Random_reflector)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Изменить рефлектор"))
        self.pshb_Random_reflector.setText(_translate("Dialog", "Случайный рефлектор"))
