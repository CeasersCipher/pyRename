# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bulkrename_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bulkrename(object):
    def setupUi(self, bulkrename):
        bulkrename.setObjectName("bulkrename")
        bulkrename.resize(200, 150)
        bulkrename.setMaximumSize(QtCore.QSize(200, 150))
        self.start = QtWidgets.QPushButton(bulkrename)
        self.start.setGeometry(QtCore.QRect(10, 100, 181, 32))
        self.start.setObjectName("start")
        self.URL = QtWidgets.QTextEdit(bulkrename)
        self.URL.setGeometry(QtCore.QRect(20, 10, 161, 31))
        self.URL.setObjectName("URL")
        self.Append = QtWidgets.QTextEdit(bulkrename)
        self.Append.setGeometry(QtCore.QRect(20, 60, 161, 31))
        self.Append.setObjectName("Append")

        self.retranslateUi(bulkrename)
        QtCore.QMetaObject.connectSlotsByName(bulkrename)

    def retranslateUi(self, bulkrename):
        _translate = QtCore.QCoreApplication.translate
        bulkrename.setWindowTitle(_translate("bulkrename", "Bulk Rename"))
        self.start.setText(_translate("bulkrename", "Start"))
        self.URL.setPlaceholderText(_translate("bulkrename", "Folder Path of Files"))
        self.Append.setPlaceholderText(_translate("bulkrename", "New Names"))

