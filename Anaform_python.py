# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/goruntuisleme/Anaform.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1154, 733)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/General OCR_32px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startCam = QtWidgets.QPushButton(self.centralwidget)
        self.startCam.setGeometry(QtCore.QRect(0, 630, 191, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/ocrclose.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startCam.setIcon(icon1)
        self.startCam.setIconSize(QtCore.QSize(32, 32))
        self.startCam.setObjectName("startCam")
        self.imgCamera_2 = QtWidgets.QLabel(self.centralwidget)
        self.imgCamera_2.setGeometry(QtCore.QRect(0, 10, 466, 400))
        self.imgCamera_2.setMinimumSize(QtCore.QSize(466, 400))
        self.imgCamera_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.imgCamera_2.setText("")
        self.imgCamera_2.setObjectName("imgCamera_2")
        self.btnOtomatikDurdur = QtWidgets.QPushButton(self.centralwidget)
        self.btnOtomatikDurdur.setGeometry(QtCore.QRect(200, 630, 151, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/autoon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOtomatikDurdur.setIcon(icon2)
        self.btnOtomatikDurdur.setIconSize(QtCore.QSize(32, 32))
        self.btnOtomatikDurdur.setObjectName("btnOtomatikDurdur")
        self.btnAyarlar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAyarlar.setGeometry(QtCore.QRect(360, 630, 141, 61))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/ayarlar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAyarlar.setIcon(icon3)
        self.btnAyarlar.setIconSize(QtCore.QSize(32, 32))
        self.btnAyarlar.setObjectName("btnAyarlar")
        self.lblogrencicevaplar = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.lblogrencicevaplar.setGeometry(QtCore.QRect(50, 420, 361, 31))
        self.lblogrencicevaplar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lblogrencicevaplar.setObjectName("lblogrencicevaplar")
        self.btnAsamalar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAsamalar.setGeometry(QtCore.QRect(510, 630, 141, 61))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icons/asamagoster.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAsamalar.setIcon(icon4)
        self.btnAsamalar.setIconSize(QtCore.QSize(32, 32))
        self.btnAsamalar.setObjectName("btnAsamalar")
        self.imgBulunan = QtWidgets.QLabel(self.centralwidget)
        self.imgBulunan.setGeometry(QtCore.QRect(470, 10, 466, 400))
        self.imgBulunan.setMinimumSize(QtCore.QSize(466, 400))
        self.imgBulunan.setFrameShape(QtWidgets.QFrame.Panel)
        self.imgBulunan.setText("")
        self.imgBulunan.setObjectName("imgBulunan")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1154, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AnaForm"))
        self.startCam.setText(_translate("MainWindow", "Duraklat"))
        self.btnOtomatikDurdur.setText(_translate("MainWindow", "Otomatik Durdur Kapalı"))
        self.btnAyarlar.setText(_translate("MainWindow", "Ayarları Aç"))
        self.btnAsamalar.setText(_translate("MainWindow", "Aşamaları Göster "))

import icons_rc
