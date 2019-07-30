import re
import io
import sys
import os
import time
# import json
import platform
from pyqrcode import QRCode
import random
# from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import itchat
from PyQt5.QtGui import QPixmap

class WeChat:
    def __init__(self):
        self.uuid = None
        self.picDir = 'QR.png'
        self.isLogging = None

    def open_qr(self):
        print('Getting uuid')
        uuid = itchat.get_QRuuid()
        self.uuid = uuid
        while uuid is None: uuid = itchat.get_QRuuid();time.sleep(1)
        print('Getting QR Code')

        qrStorage = io.BytesIO()
        qrCode = QRCode('https://login.weixin.qq.com/l/' + uuid)
        qrCode.png(qrStorage, scale=6)
        with open(self.picDir, 'wb') as f:
            f.write(qrStorage.getvalue())
        print('Please scan the QR Code')
        return uuid

    def run(self):
        userInfo = itchat.web_init()
        itchat.show_mobile_login()
        itchat.get_contact(True)

        print('Login successfully as %s' % userInfo['User']['NickName'])


    def init_username(self):
        """ 初始化微信所需数据 """
        dic = itchat.web_init()
        print(dic)
        return ['User']['NickName']


    def exit_msg(self):
        """ 退出通知 """
        print('程序已退出')

