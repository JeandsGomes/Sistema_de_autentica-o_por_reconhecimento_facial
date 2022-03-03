# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_inicial_1.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class menu_inicial(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setStyleSheet("background-color: rgb(30, 30, 30)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 130))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_avatar_adm = QtWidgets.QLabel(self.frame_5)
        self.label_avatar_adm.setText("")
        self.label_avatar_adm.setPixmap(QtGui.QPixmap("../../imagens/Vector.png"))
        self.label_avatar_adm.setObjectName("label_avatar_adm")
        self.horizontalLayout_2.addWidget(self.label_avatar_adm)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_string_ola = QtWidgets.QLabel(self.frame_7)
        self.label_string_ola.setGeometry(QtCore.QRect(10, 10, 28, 18))
        self.label_string_ola.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_string_ola.setFont(font)
        self.label_string_ola.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_string_ola.setStyleSheet("color: rgb(240, 233, 249);")
        self.label_string_ola.setObjectName("label_string_ola")
        self.nome_adm = QtWidgets.QLabel(self.frame_7)
        self.nome_adm.setGeometry(QtCore.QRect(49, 10, 131, 20))
        self.nome_adm.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.nome_adm.setFont(font)
        self.nome_adm.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.nome_adm.setStyleSheet("color: rgb(240, 233, 249);")
        self.nome_adm.setObjectName("nome_adm")
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.cadastro_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.cadastro_pushButton.setMinimumSize(QtCore.QSize(150, 40))
        self.cadastro_pushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cadastro_pushButton.setFont(font)
        self.cadastro_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cadastro_pushButton.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(42, 42, 42);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.cadastro_pushButton.setObjectName("cadastro_pushButton")
        self.verticalLayout_2.addWidget(self.cadastro_pushButton)
        self.reconhecimento_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.reconhecimento_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.reconhecimento_pushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.reconhecimento_pushButton.setFont(font)
        self.reconhecimento_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reconhecimento_pushButton.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(42, 42, 42);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.reconhecimento_pushButton.setObjectName("reconhecimento_pushButton")
        self.verticalLayout_2.addWidget(self.reconhecimento_pushButton)
        self.Editar_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.Editar_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.Editar_pushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Editar_pushButton.setFont(font)
        self.Editar_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Editar_pushButton.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(42, 42, 42);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.Editar_pushButton.setObjectName("Editar_pushButton")
        self.verticalLayout_2.addWidget(self.Editar_pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sair_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.sair_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.sair_pushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sair_pushButton.setFont(font)
        self.sair_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sair_pushButton.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    border-image: url(:/Close_Image/cil-x.png);\n"
"    background-position: center;\n"
"        \n"
"    color: rgb(240, 233, 249);\n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(42, 42, 42);\n"
"    color: rgb(240, 233, 249);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"")
        self.sair_pushButton.setObjectName("sair_pushButton")
        self.verticalLayout_3.addWidget(self.sair_pushButton)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(242, 242, 242)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.indiv_cadastrados_tableWidget = QtWidgets.QTableWidget(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.indiv_cadastrados_tableWidget.sizePolicy().hasHeightForWidth())
        self.indiv_cadastrados_tableWidget.setSizePolicy(sizePolicy)
        self.indiv_cadastrados_tableWidget.setMinimumSize(QtCore.QSize(502, 300))
        self.indiv_cadastrados_tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.indiv_cadastrados_tableWidget.setObjectName("indiv_cadastrados_tableWidget")
        self.indiv_cadastrados_tableWidget.setColumnCount(5)
        self.indiv_cadastrados_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.indiv_cadastrados_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.indiv_cadastrados_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.indiv_cadastrados_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.indiv_cadastrados_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.indiv_cadastrados_tableWidget.setHorizontalHeaderItem(4, item)
        self.horizontalLayout_3.addWidget(self.indiv_cadastrados_tableWidget)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_4.addWidget(self.frame_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_string_ola.setText(_translate("MainWindow", "Olá,"))
        self.nome_adm.setText(_translate("MainWindow", "Uruario Teste"))
        self.cadastro_pushButton.setText(_translate("MainWindow", "Cadastrar Individuo"))
        self.reconhecimento_pushButton.setText(_translate("MainWindow", "Reconhecimento Facial"))
        self.Editar_pushButton.setText(_translate("MainWindow", "Editar Individuo"))
        self.sair_pushButton.setText(_translate("MainWindow", "sair"))
        item = self.indiv_cadastrados_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.indiv_cadastrados_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.indiv_cadastrados_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        item = self.indiv_cadastrados_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data"))
        item = self.indiv_cadastrados_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Hora"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = menu_inicial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())