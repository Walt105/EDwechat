#! usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2019/7/13
# Author: walt

from mainform import Ui_mainform
from freemessagebox import Ui_messagebox_free
from normalmessagebox import Ui_messagebox_normal
from qrbox import Ui_qrbox
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, pyqtSignal, QTime
from wechat import WeChat
import itchat
import time


class Thread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.loginflag = False

    def run(self):
        # 线程相关代码

        while not self.loginflag:
            status = itchat.check_login()
            file_str = status
            self.sinOut.emit(file_str)
            self.sleep(3)
            #登录成功
            if status == 200:
                self.loginflag = True
                break
        return 0


class MainWindow(QWidget, Ui_mainform):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.timer = QTime()
        self.newChat = WeChat()
        self.qrUI = QrWindow()
        self.msgUI = FreeMsgWindow()
        self.normalUI = NormalMsgWindow()
        self.pushButton_NewMessage.clicked.connect(self.on_pB_NewMessage_clicked)
        self.pushButton_LoginWechat.clicked.connect(self.on_pB_LoginWechat_clicked)
        self.pushButton_DeleteMessage.clicked.connect(self.on_pB_DeleteMessage_clicked)
        self.thread = Thread()
        self.thread.sinOut.connect(self.login)

    def on_pB_NewMessage_clicked(self):
        self.msgUI.show()

    def on_pB_DeleteMessage_clicked(self):
        self.normalUI.show()

    def on_pB_LoginWechat_clicked(self):
        self.newChat.open_qr()
        qrpic = QPixmap(self.newChat.picDir)
        self.qrUI.labe_Qrcode.setPixmap(qrpic)
        self.qrUI.label_Qrstatus.setText('请打开手机微信扫码登陆')
        self.qrUI.show()
        self.thread.start()

    def login(self, file_inf):
        if file_inf == '200':
            self.qrUI.label_Qrstatus.setText('登陆成功')
            self.newChat.run()
            self.qrUI.close()
            self.thread.loginflag = True
            self.thread.quit()
            return
        elif file_inf == '201':
            self.qrUI.label_Qrstatus.setText('请在手机微信中确认登陆')
        elif file_inf == '408':
            self.qrUI.label_Qrstatus.setText('二维码失效')


class QrWindow(QWidget, Ui_qrbox):
    def __init__(self):
        super(QrWindow, self).__init__()
        self.setupUi(self)


class FreeMsgWindow(QWidget, Ui_messagebox_free):
    def __init__(self):
        super(FreeMsgWindow, self).__init__()
        self.setupUi(self)


class NormalMsgWindow(QWidget, Ui_messagebox_normal):
    def __init__(self):
        super(NormalMsgWindow, self).__init__()
        self.setupUi(self)
