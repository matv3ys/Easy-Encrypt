# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rotor_change.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(912, 193)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 861, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_perms = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_perms.sizePolicy().hasHeightForWidth())
        self.lineEdit_perms.setSizePolicy(sizePolicy)
        self.lineEdit_perms.setStyleSheet("border: 3px solid;\n"
"border-color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_perms.setObjectName("lineEdit_perms")
        self.horizontalLayout_2.addWidget(self.lineEdit_perms)
        self.lineEdit_turnover = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_turnover.sizePolicy().hasHeightForWidth())
        self.lineEdit_turnover.setSizePolicy(sizePolicy)
        self.lineEdit_turnover.setStyleSheet("border: 3px solid;\n"
"border-color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_turnover.setObjectName("lineEdit_turnover")
        self.horizontalLayout_2.addWidget(self.lineEdit_turnover)
        self.lineEdit_ring_set = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ring_set.sizePolicy().hasHeightForWidth())
        self.lineEdit_ring_set.setSizePolicy(sizePolicy)
        self.lineEdit_ring_set.setStyleSheet("border: 3px solid;\n"
"border-color: rgb(0, 255, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_ring_set.setObjectName("lineEdit_ring_set")
        self.horizontalLayout_2.addWidget(self.lineEdit_ring_set)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 120, 861, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.horizontalLayoutWidget_3.setFont(font)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pshb_Random_rotor = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.pshb_Random_rotor.setFont(font)
        self.pshb_Random_rotor.setObjectName("pshb_Random_rotor")
        self.horizontalLayout_3.addWidget(self.pshb_Random_rotor)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Изменить ротор"))
        self.label_3.setText(_translate("Dialog", "Позиции                                                                   Точка поворота  Стартовая позиция"))
        self.pshb_Random_rotor.setText(_translate("Dialog", "Случайный ротор"))
