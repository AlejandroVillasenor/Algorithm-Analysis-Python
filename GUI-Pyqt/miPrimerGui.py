# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'miPrimerGui.ui'
# Created by: PyQt5 UI code generator 5.15.10
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
"""
    Villasenor Rivas Alejandro Rodrigo 
    Tarea 10. GUI con Pyqt
"""
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 533)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../94d07e4f/icono.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 50, 121, 24))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.separarPalabras_p)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 290, 731, 192))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Palabras"])
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 50, 250, 200))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(530, 50, 250, 200))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 100, 121, 24))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.limpiar_p)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 150, 121, 24))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.cambiarTema_p)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Separador de palabras"))
        self.pushButton.setText(_translate("MainWindow", "Separar palabras"))
        self.pushButton_2.setText(_translate("MainWindow", "Limpiar"))
        self.pushButton_3.setText(_translate("MainWindow", "Dark mode"))
    def separarPalabras_p(self):
        texto=self.textEdit.toPlainText()
        self.textEdit_2.setPlainText(texto)
        texto_spliteado=texto.split()#Retorna una lista con las palabras separadas
        for r in range(len(texto_spliteado),self.tableWidget.rowCount()):
            self.tableWidget.removeRow(len(texto_spliteado));
        for r in range(len(texto_spliteado)):
            rowAct=self.tableWidget.rowCount()
            if(rowAct<=r):
                self.tableWidget.insertRow(rowAct)
                self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(texto_spliteado[r]))
            else:
                self.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(texto_spliteado[r]))
    def limpiar_p(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        for r in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0);
    def cambiarTema_p(self):
        if(self.pushButton_3.text()=="Dark mode"):
            #Modo oscuro
            self.pushButton_3.setText("Light mode")
            self.pushButton_3.setStyleSheet("background-color: rgb(54, 54, 54);\n"
                                            "color: rgb(255, 255, 255);")
            self.pushButton_2.setStyleSheet("background-color: rgb(54, 54, 54);\n"
                                            "color: rgb(255, 255, 255);")
            self.pushButton.setStyleSheet("background-color: rgb(54, 54, 54);\n"
                                            "color: rgb(255, 255, 255);")
            self.textEdit.setStyleSheet("background-color: rgb(54, 54, 54);\n"
                                            "color: rgb(255, 255, 255);")
            self.textEdit_2.setStyleSheet("background-color: rgb(54, 54, 54);\n"
                                            "color: rgb(255, 255, 255);")
            self.tableWidget.setStyleSheet("background-color: rgb(54, 54, 54);\n"
                                            "color: rgb(255, 255, 255);")
            MainWindow.setStyleSheet("background-color: rgb(31, 31, 31);")          
        else:
            #Modo claro
            self.pushButton_3.setText("Dark mode")
            self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color: rgb(0, 0, 0);")
            self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color: rgb(0, 0, 0);")
            self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color: rgb(0, 0, 0);")
            self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color: rgb(0, 0, 0);")
            self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color: rgb(0, 0, 0);")
            self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "color: rgb(0, 0, 0);")
            MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())