# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainform(object):
    def setupUi(self, mainform):
        mainform.setObjectName("mainform")
        mainform.resize(887, 626)
        mainform.setAutoFillBackground(False)
        self.listView = QtWidgets.QListView(mainform)
        self.listView.setGeometry(QtCore.QRect(60, 230, 481, 291))
        self.listView.setObjectName("listView")
        self.horizontalLayoutWidget = QtWidgets.QWidget(mainform)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 540, 481, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_NewMessage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_NewMessage.sizePolicy().hasHeightForWidth())
        self.pushButton_NewMessage.setSizePolicy(sizePolicy)
        self.pushButton_NewMessage.setObjectName("pushButton_NewMessage")
        self.horizontalLayout.addWidget(self.pushButton_NewMessage)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_DeleteMessage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_DeleteMessage.sizePolicy().hasHeightForWidth())
        self.pushButton_DeleteMessage.setSizePolicy(sizePolicy)
        self.pushButton_DeleteMessage.setObjectName("pushButton_DeleteMessage")
        self.horizontalLayout.addWidget(self.pushButton_DeleteMessage)
        self.pushButton_LoginWechat = QtWidgets.QPushButton(mainform)
        self.pushButton_LoginWechat.setGeometry(QtCore.QRect(150, 50, 75, 23))
        self.pushButton_LoginWechat.setObjectName("pushButton_LoginWechat")

        self.retranslateUi(mainform)
        QtCore.QMetaObject.connectSlotsByName(mainform)

    def retranslateUi(self, mainform):
        _translate = QtCore.QCoreApplication.translate
        mainform.setWindowTitle(_translate("mainform", "微信伴侣"))
        self.pushButton_NewMessage.setText(_translate("mainform", "新建消息"))
        self.pushButton.setText(_translate("mainform", "预览消息"))
        self.pushButton_DeleteMessage.setText(_translate("mainform", "删除消息"))
        self.pushButton_LoginWechat.setText(_translate("mainform", "登录微信"))


