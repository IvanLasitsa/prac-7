# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(334, 384)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setGeometry(QtCore.QRect(90, 280, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_generate.setFont(font)
        self.btn_generate.setStyleSheet("background-color: black;\n"
"color: white;\n"
"border: 5px solid purple;\n"
"border-radius: 10px;")
        self.btn_generate.setObjectName("btn_generate")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(60, 110, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result.setFont(font)
        self.result.setStyleSheet("border: 5px solid pink;")
        self.result.setObjectName("result")
        self.cb_alphabet = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_alphabet.setGeometry(QtCore.QRect(50, 230, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_alphabet.setFont(font)
        self.cb_alphabet.setStyleSheet("border: 5px solid orange;\n"
"color: blue;")
        self.cb_alphabet.setObjectName("cb_alphabet")
        self.cb_numbers = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_numbers.setGeometry(QtCore.QRect(50, 180, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_numbers.setFont(font)
        self.cb_numbers.setStyleSheet("border: 5px solid orange;\n"
"color: blue;")
        self.cb_numbers.setObjectName("cb_numbers")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(40, 30, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(240, 340, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.quit.setFont(font)
        self.quit.setStyleSheet("border: 2px solid black;\n"
"background-color: black;\n"
"color: white;\n"
"")
        self.quit.setObjectName("quit")
        self.value = QtWidgets.QSpinBox(self.centralwidget)
        self.value.setGeometry(QtCore.QRect(280, 130, 42, 22))
        self.value.setObjectName("value")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_generate.setText(_translate("MainWindow", "Згенерувати"))
        self.result.setText(_translate("MainWindow", "Тут буде результат"))
        self.cb_alphabet.setText(_translate("MainWindow", "Використати алфавіт"))
        self.cb_numbers.setText(_translate("MainWindow", "Використати числа"))
        self.title.setText(_translate("MainWindow", "Генератор паролів"))
        self.quit.setText(_translate("MainWindow", "Вихід"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
