# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/goruntuisleme/second_page.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(309, 440)
        self.sliderIsik = QtWidgets.QSlider(Form)
        self.sliderIsik.setGeometry(QtCore.QRect(40, 30, 161, 22))
        self.sliderIsik.setMinimum(0)
        self.sliderIsik.setMaximum(255)
        self.sliderIsik.setOrientation(QtCore.Qt.Horizontal)
        self.sliderIsik.setObjectName("sliderIsik")
        self.lblIsik = QtWidgets.QLabel(Form)
        self.lblIsik.setGeometry(QtCore.QRect(41, 10, 161, 16))
        self.lblIsik.setObjectName("lblIsik")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "2.pencere"))
        self.lblIsik.setText(_translate("Form", "Işık"))

