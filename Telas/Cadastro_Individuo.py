# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cadastro_Individuo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils
import time
import numpy as np
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
import numpy as np
import cv2
import pyshine as ps


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 545)
        MainWindow.setStyleSheet("background-color: rgb(242, 242, 242)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(349, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setMinimumSize(QtCore.QSize(165, 0))
        self.label_5.setMaximumSize(QtCore.QSize(108, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(348, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_7)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(502, 300))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../imagens/Frame 1.png"))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.login_pushButton_logar_4 = QtWidgets.QPushButton(self.frame_5)
        self.login_pushButton_logar_4.setMinimumSize(QtCore.QSize(60, 20))
        self.login_pushButton_logar_4.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_pushButton_logar_4.setFont(font)
        self.login_pushButton_logar_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_pushButton_logar_4.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
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
        self.login_pushButton_logar_4.setObjectName("login_pushButton_logar_4")
        self.horizontalLayout_3.addWidget(self.login_pushButton_logar_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.frame_7)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMinimumSize(QtCore.QSize(142, 0))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 98))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.login_lineEdit_cpf_2 = QtWidgets.QLineEdit(self.frame_10)
        self.login_lineEdit_cpf_2.setMinimumSize(QtCore.QSize(0, 50))
        self.login_lineEdit_cpf_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.login_lineEdit_cpf_2.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 2px;")
        self.login_lineEdit_cpf_2.setInputMask("")
        self.login_lineEdit_cpf_2.setText("")
        self.login_lineEdit_cpf_2.setObjectName("login_lineEdit_cpf_2")
        self.verticalLayout_4.addWidget(self.login_lineEdit_cpf_2)
        self.login_lineEdit_cpf = QtWidgets.QLineEdit(self.frame_10)
        self.login_lineEdit_cpf.setMinimumSize(QtCore.QSize(0, 50))
        self.login_lineEdit_cpf.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.login_lineEdit_cpf.setStyleSheet("border-width: 1px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 2px;")
        self.login_lineEdit_cpf.setInputMask("")
        self.login_lineEdit_cpf.setText("")
        self.login_lineEdit_cpf.setObjectName("login_lineEdit_cpf")
        self.verticalLayout_4.addWidget(self.login_lineEdit_cpf)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 97))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_9)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.frame_9)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.horizontalLayout_4.addWidget(self.frame_9)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.frame_11)
        self.label_9.setMinimumSize(QtCore.QSize(29, 29))
        self.label_9.setMaximumSize(QtCore.QSize(29, 29))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../imagens/Group 144.png"))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.frame_11)
        self.label_8.setMinimumSize(QtCore.QSize(29, 29))
        self.label_8.setMaximumSize(QtCore.QSize(29, 29))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../imagens/Group 144.png"))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.label_2 = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(29)
        sizePolicy.setVerticalStretch(29)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(29, 29))
        self.label_2.setMaximumSize(QtCore.QSize(29, 29))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../imagens/Group 144.png"))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_4.addWidget(self.frame_11)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.login_pushButton_logar = QtWidgets.QPushButton(self.frame_6)
        self.login_pushButton_logar.setMinimumSize(QtCore.QSize(0, 50))
        self.login_pushButton_logar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_pushButton_logar.setFont(font)
        self.login_pushButton_logar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_pushButton_logar.setStyleSheet("QPushButton{\n"
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
        self.login_pushButton_logar.setObjectName("login_pushButton_logar")
        self.verticalLayout_7.addWidget(self.login_pushButton_logar)
        self.login_pushButton_logar_2 = QtWidgets.QPushButton(self.frame_6)
        self.login_pushButton_logar_2.setMinimumSize(QtCore.QSize(0, 50))
        self.login_pushButton_logar_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_pushButton_logar_2.setFont(font)
        self.login_pushButton_logar_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_pushButton_logar_2.setStyleSheet("QPushButton{\n"
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
        self.login_pushButton_logar_2.setObjectName("login_pushButton_logar_2")
        self.verticalLayout_7.addWidget(self.login_pushButton_logar_2)
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.frame_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Adicionar codigo aqui
        self.filename = 'Snapssho '+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png' # Localização da foto que sera salva
        self.tmp = None # Onde sera armazenado a imagem do dysplay
        self.fps=0
        self.started = False

        self.login_pushButton_logar_4.clicked.connect(self.loadImage)

    def loadImage(self):
        """
            Esta função inicializara a camera Inicializar a camera.
            :return:
        """
        if self.started:
            self.started = False
            #self.login_pushButton_logar.setText('Salvar Foto FRONTAL')

        cam = True #Possui WebCam
        if cam:
            vid = cv2.VideoCapture(0)

        cnt = 0
        frames_to_count=20
        st = 0
        fps = 0

        while(vid.isOpened()):
            img, self.image = vid.read()
            self.image = imutils.resize(self.image, width=502, height=300)

            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor=1.15,
                    minNeighbors=7,
                    minSize=(80, 80),
                    flags=cv2.CASCADE_SCALE_IMAGE)

            for (x,y,w,h) in faces:
                cv2.rectangle(self.image, (x,y), (x+w,y+h), (10,228,220),5)

            if cnt == frames_to_count:
                try:  # To avoid divide by 0 we put it in try except
                    print(frames_to_count / (time.time() - st), 'FPS')
                    self.fps = round(frames_to_count / (time.time() - st))

                    st = time.time()
                    cnt = 0
                except:
                    pass
            cnt+=1

            self.update()

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

    def setPhoto(self,image):
        """
            Essa função vair utilizar a imagem passadapor parametro realizar o
            preprocessamento ajustando seu diametro e inserindo no display da
            da interface.
            :param image:
            :return:
        """
        self.tmp = image
        image = imutils.resize(image, height=300, width=502)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def update(self):
        """

            :return:
        """
        img = self.image
        text = 'FPS: '+str(self.fps)
        img = ps.putBText(img,text,text_offset_x=20,text_offset_y=30,vspace=20,hspace=10, font_scale=1.0,background_RGB=(10,20,222),text_RGB=(255,255,255))
        text = str(time.strftime("%H:%M %p"))
        img = ps.putBText(img, text, text_offset_x=self.image.shape[1] - 180, text_offset_y=30, vspace=20, hspace=10,
                          font_scale=1.0, background_RGB=(228, 20, 222), text_RGB=(255, 255, 255))

        self.setPhoto(img)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Cadastrar Individuo"))
        self.login_pushButton_logar_4.setText(_translate("MainWindow", "<< Voltar"))
        self.label_3.setText(_translate("MainWindow", "Informe os dados"))
        self.login_lineEdit_cpf_2.setPlaceholderText(_translate("MainWindow", "    nome"))
        self.login_lineEdit_cpf.setPlaceholderText(_translate("MainWindow", "    email"))
        self.label_4.setText(_translate("MainWindow", "Imagem 1"))
        self.label_6.setText(_translate("MainWindow", "Imagem 2"))
        self.label_7.setText(_translate("MainWindow", "Imagem 3"))
        self.login_pushButton_logar.setText(_translate("MainWindow", "Salvar Foto"))
        self.login_pushButton_logar_2.setText(_translate("MainWindow", "Cadastrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())