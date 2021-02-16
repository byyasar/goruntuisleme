# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/goruntuisleme/ayarlarPage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(309, 360)
        self.sliderIsik = QtWidgets.QSlider(Form)
        self.sliderIsik.setGeometry(QtCore.QRect(49, 60, 161, 22))
        self.sliderIsik.setMinimum(0)
        self.sliderIsik.setMaximum(255)
        self.sliderIsik.setOrientation(QtCore.Qt.Horizontal)
        self.sliderIsik.setObjectName("sliderIsik")
        self.lblIsik = QtWidgets.QLabel(Form)
        self.lblIsik.setGeometry(QtCore.QRect(50, 40, 161, 16))
        self.lblIsik.setObjectName("lblIsik")
        self.sliderEsik = QtWidgets.QSlider(Form)
        self.sliderEsik.setGeometry(QtCore.QRect(50, 170, 160, 22))
        self.sliderEsik.setMinimum(50)
        self.sliderEsik.setMaximum(500)
        self.sliderEsik.setOrientation(QtCore.Qt.Horizontal)
        self.sliderEsik.setObjectName("sliderEsik")
        self.sliderFocus = QtWidgets.QSlider(Form)
        self.sliderFocus.setGeometry(QtCore.QRect(49, 120, 161, 22))
        self.sliderFocus.setMinimum(0)
        self.sliderFocus.setMaximum(100)
        self.sliderFocus.setOrientation(QtCore.Qt.Horizontal)
        self.sliderFocus.setObjectName("sliderFocus")
        self.sliderTresh = QtWidgets.QSlider(Form)
        self.sliderTresh.setGeometry(QtCore.QRect(50, 220, 160, 22))
        self.sliderTresh.setMaximum(255)
        self.sliderTresh.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTresh.setObjectName("sliderTresh")
        self.lblTresh = QtWidgets.QLabel(Form)
        self.lblTresh.setGeometry(QtCore.QRect(50, 200, 161, 20))
        self.lblTresh.setObjectName("lblTresh")
        self.lblEsik = QtWidgets.QLabel(Form)
        self.lblEsik.setGeometry(QtCore.QRect(50, 150, 151, 16))
        self.lblEsik.setObjectName("lblEsik")
        self.lblFocus = QtWidgets.QLabel(Form)
        self.lblFocus.setGeometry(QtCore.QRect(50, 100, 161, 16))
        self.lblFocus.setObjectName("lblFocus")
        self.btnAyarlariKaydet = QtWidgets.QPushButton(Form)
        self.btnAyarlariKaydet.setGeometry(QtCore.QRect(80, 270, 111, 23))
        self.btnAyarlariKaydet.setObjectName("btnAyarlariKaydet")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ayarlar"))
        self.lblIsik.setText(_translate("Form", "Işık"))
        self.lblTresh.setText(_translate("Form", "Tresh"))
        self.lblEsik.setText(_translate("Form", "Esik"))
        self.lblFocus.setText(_translate("Form", "Focus"))
        self.btnAyarlariKaydet.setText(_translate("Form", "Ayarları Kaydet"))

