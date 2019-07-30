# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qrbox.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_qrbox(object):
    def setupUi(self, qrbox):
        qrbox.setObjectName("qrbox")
        qrbox.resize(746, 592)
        self.labe_Qrcode = QtWidgets.QLabel(qrbox)
        self.labe_Qrcode.setGeometry(QtCore.QRect(210, 100, 351, 311))
        self.labe_Qrcode.setObjectName("labe_Qrcode")
        self.label_Qrstatus = QtWidgets.QLabel(qrbox)
        self.label_Qrstatus.setGeometry(QtCore.QRect(200, 460, 351, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.label_Qrstatus.setFont(font)
        self.label_Qrstatus.setText("")
        self.label_Qrstatus.setObjectName("label_Qrstatus")

        self.retranslateUi(qrbox)
        QtCore.QMetaObject.connectSlotsByName(qrbox)

    def retranslateUi(self, qrbox):
        _translate = QtCore.QCoreApplication.translate
        qrbox.setWindowTitle(_translate("qrbox", "qrbox"))
        self.labe_Qrcode.setText(_translate("qrbox", "TextLabel"))


