# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plantilla.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 362)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Seleccionar = QtWidgets.QPushButton(self.centralwidget)
        self.Seleccionar.setGeometry(QtCore.QRect(10, 140, 161, 21))
        self.Seleccionar.setObjectName("Seleccionar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 120, 291, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 230, 171, 61))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 311, 17))
        self.label_2.setObjectName("label_2")
        self.label_path = QtWidgets.QLabel(self.centralwidget)
        self.label_path.setGeometry(QtCore.QRect(10, 180, 411, 17))
        self.label_path.setObjectName("label_path")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 111, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 181, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 191, 17))
        self.label_5.setObjectName("label_5")
        self.estatus = QtWidgets.QLabel(self.centralwidget)
        self.estatus.setGeometry(QtCore.QRect(100, 300, 311, 17))
        self.estatus.setObjectName("estatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Detector de personas"))
        self.Seleccionar.setText(_translate("MainWindow", "Seleccionar"))
        self.label.setText(_translate("MainWindow", "Selecciona un archivo:"))
        self.pushButton.setText(_translate("MainWindow", "Analizar"))
        self.label_2.setText(_translate("MainWindow", "Tu archivo:"))
        self.label_path.setText(_translate("MainWindow", "\'file name\' ningún archivo seleccionado"))
        self.label_3.setText(_translate("MainWindow", "Instrucciones:"))
        self.label_4.setText(_translate("MainWindow", "1. Selecciona una imagen"))
        self.label_5.setText(_translate("MainWindow", "2. Usa el botón analizar"))
        self.estatus.setText(_translate("MainWindow", "Estatus: Selecciona una imagen"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
