# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'freemessagebox.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_messagebox_free(object):
    def setupUi(self, messagebox_free):
        messagebox_free.setObjectName("messagebox_free")
        messagebox_free.resize(741, 474)
        messagebox_free.setAutoFillBackground(False)
        self.horizontalLayoutWidget = QtWidgets.QWidget(messagebox_free)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 160, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Repeat = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_Repeat.setObjectName("label_Repeat")
        self.horizontalLayout.addWidget(self.label_Repeat)
        self.comboBox_Repeat = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_Repeat.setMouseTracking(False)
        self.comboBox_Repeat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_Repeat.setObjectName("comboBox_Repeat")
        self.comboBox_Repeat.addItem("")
        self.comboBox_Repeat.addItem("")
        self.comboBox_Repeat.addItem("")
        self.comboBox_Repeat.addItem("")
        self.comboBox_Repeat.addItem("")
        self.comboBox_Repeat.addItem("")
        self.comboBox_Repeat.addItem("")
        self.comboBox_Repeat.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_Repeat)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(messagebox_free)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 60, 160, 22))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_Sendtime = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_Sendtime.setObjectName("label_Sendtime")
        self.horizontalLayout_2.addWidget(self.label_Sendtime)
        self.timeEdit_Sendtime = QtWidgets.QTimeEdit(self.horizontalLayoutWidget_2)
        self.timeEdit_Sendtime.setObjectName("timeEdit_Sendtime")
        self.horizontalLayout_2.addWidget(self.timeEdit_Sendtime)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(messagebox_free)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 100, 160, 21))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Msgcontent = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_Msgcontent.setObjectName("label_Msgcontent")
        self.horizontalLayout_3.addWidget(self.label_Msgcontent)
        self.textEdit_geren = QtWidgets.QTextEdit(messagebox_free)
        self.textEdit_geren.setGeometry(QtCore.QRect(30, 130, 351, 291))
        self.textEdit_geren.setObjectName("textEdit_geren")
        self.verticalLayoutWidget = QtWidgets.QWidget(messagebox_free)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 430, 681, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_Preview = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Preview.setObjectName("pushButton_Preview")
        self.horizontalLayout_8.addWidget(self.pushButton_Preview)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.pushButton_Reset = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.horizontalLayout_8.addWidget(self.pushButton_Reset)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.pushButton_Determine = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Determine.setObjectName("pushButton_Determine")
        self.horizontalLayout_8.addWidget(self.pushButton_Determine)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.pushButton_Close = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.horizontalLayout_8.addWidget(self.pushButton_Close)
        self.label_8 = QtWidgets.QLabel(messagebox_free)
        self.label_8.setGeometry(QtCore.QRect(410, 30, 61, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(messagebox_free)
        self.label_9.setGeometry(QtCore.QRect(410, 200, 61, 20))
        self.label_9.setObjectName("label_9")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(messagebox_free)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(480, 30, 221, 22))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_9.addWidget(self.lineEdit_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.label_Repeat.setBuddy(self.comboBox_Repeat)
        self.label_Sendtime.setBuddy(self.timeEdit_Sendtime)

        self.retranslateUi(messagebox_free)
        self.pushButton_Close.clicked.connect(messagebox_free.close)
        QtCore.QMetaObject.connectSlotsByName(messagebox_free)

    def retranslateUi(self, messagebox_free):
        _translate = QtCore.QCoreApplication.translate
        messagebox_free.setWindowTitle(_translate("messagebox_free", "消息详情"))
        self.label_Repeat.setText(_translate("messagebox_free", "重复："))
        self.comboBox_Repeat.setToolTip(_translate("messagebox_free", "选择消息发送的频率"))
        self.comboBox_Repeat.setItemText(0, _translate("messagebox_free", "每天"))
        self.comboBox_Repeat.setItemText(1, _translate("messagebox_free", "星期一"))
        self.comboBox_Repeat.setItemText(2, _translate("messagebox_free", "星期二"))
        self.comboBox_Repeat.setItemText(3, _translate("messagebox_free", "星期三"))
        self.comboBox_Repeat.setItemText(4, _translate("messagebox_free", "星期四"))
        self.comboBox_Repeat.setItemText(5, _translate("messagebox_free", "星期五"))
        self.comboBox_Repeat.setItemText(6, _translate("messagebox_free", "星期六"))
        self.comboBox_Repeat.setItemText(7, _translate("messagebox_free", "星期日"))
        self.label_Sendtime.setText(_translate("messagebox_free", "时间："))
        self.timeEdit_Sendtime.setToolTip(_translate("messagebox_free", "设置消息发送的时间"))
        self.timeEdit_Sendtime.setStatusTip(_translate("messagebox_free", "设置消息发送的时间"))
        self.label_Msgcontent.setText(_translate("messagebox_free", "消息内容："))
        self.textEdit_geren.setPlaceholderText(_translate("messagebox_free", "请输入个人要发送的消息内容"))
        self.pushButton_Preview.setText(_translate("messagebox_free", "预览消息"))
        self.pushButton_Reset.setText(_translate("messagebox_free", "重置消息"))
        self.pushButton_Determine.setText(_translate("messagebox_free", "确定"))
        self.pushButton_Close.setText(_translate("messagebox_free", "关闭"))
        self.label_8.setText(_translate("messagebox_free", "好友名称："))
        self.label_9.setText(_translate("messagebox_free", "群聊名称："))
        self.label_10.setText(_translate("messagebox_free", "TextLabel"))


