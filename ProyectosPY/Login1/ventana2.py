# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana2(object):
    def setupUi(self, ventana2):
        ventana2.setObjectName("ventana2")
        ventana2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ventana2)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 60, 301, 261))
        self.pushButton.setObjectName("pushButton")
        ventana2.setCentralWidget(self.centralwidget)

        self.retranslateUi(ventana2)
        QtCore.QMetaObject.connectSlotsByName(ventana2)

    def retranslateUi(self, ventana2):
        _translate = QtCore.QCoreApplication.translate
        ventana2.setWindowTitle(_translate("ventana2", "MainWindow"))
        self.pushButton.setText(_translate("ventana2", "ventana2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana2 = QtWidgets.QMainWindow()
    ui = Ui_ventana2()
    ui.setupUi(ventana2)
    ventana2.show()
    sys.exit(app.exec_())