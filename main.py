# -*- coding: utf-8 -*-
import sys
from uicontrol import MainWindow
from wechat import WeChat
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainUI = MainWindow()
    mainUI.show()



    sys.exit(app.exec_())