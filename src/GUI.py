# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(500, 590)
        Window.setMinimumSize(QtCore.QSize(500, 590))
        Window.setMaximumSize(QtCore.QSize(500, 590))
        self.pushPrevious = QtWidgets.QPushButton(Window)
        self.pushPrevious.setGeometry(QtCore.QRect(10, 550, 231, 31))
        self.pushPrevious.setObjectName("pushPrevious")
        self.pushNext = QtWidgets.QPushButton(Window)
        self.pushNext.setGeometry(QtCore.QRect(260, 550, 231, 31))
        self.pushNext.setObjectName("pushNext")
        self.lineEdit = QtWidgets.QLineEdit(Window)
        self.lineEdit.setGeometry(QtCore.QRect(10, 520, 481, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Window)
        self.label.setGeometry(QtCore.QRect(10, 40, 481, 471))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushBrowse = QtWidgets.QPushButton(Window)
        self.pushBrowse.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.pushBrowse.setObjectName("pushBrowse")
        self.lineBrowse = QtWidgets.QLineEdit(Window)
        self.lineBrowse.setGeometry(QtCore.QRect(90, 10, 401, 20))
        self.lineBrowse.setReadOnly(True)
        self.lineBrowse.setObjectName("lineBrowse")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Image Preview Renamer"))
        self.pushPrevious.setText(_translate("Window", "<"))
        self.pushNext.setText(_translate("Window", ">"))
        self.label.setText(_translate("Window", "Aaron\'s Image Previewer"))
        self.pushBrowse.setText(_translate("Window", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QWidget()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

