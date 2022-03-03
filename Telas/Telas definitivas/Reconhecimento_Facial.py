# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reconhecimento_Facial_1.0.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from PyQt5.QtGui import QImage
import imutils
import cv2
import time
import numpy as np
faceCascade = cv2.CascadeClassifier('../../modelos_e_XLM/haarcascade_frontalface_default.xml')
import numpy as np

class reconhecimento_facial_individuo(object):
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
        self.label_5.setMinimumSize(QtCore.QSize(210, 0))
        self.label_5.setMaximumSize(QtCore.QSize(125, 16777215))
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
        self.label.setPixmap(QtGui.QPixmap("../../imagens/Frame 1.png"))
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
        self.rec_facial_pushButton_voltar = QtWidgets.QPushButton(self.frame_5)
        self.rec_facial_pushButton_voltar.setMinimumSize(QtCore.QSize(60, 20))
        self.rec_facial_pushButton_voltar.setMaximumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rec_facial_pushButton_voltar.setFont(font)
        self.rec_facial_pushButton_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rec_facial_pushButton_voltar.setStyleSheet("QPushButton{\n"
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
        self.rec_facial_pushButton_voltar.setObjectName("rec_facial_pushButton_voltar")
        self.horizontalLayout_3.addWidget(self.rec_facial_pushButton_voltar)
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
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setMinimumSize(QtCore.QSize(91, 86))
        self.label_2.setMaximumSize(QtCore.QSize(70, 70))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../imagens/Frame 19 (1).png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(20, 40, 53, 13))
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
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 53, 13))
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
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(20, 0, 53, 13))
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
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(90, 0, 201, 16))
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setGeometry(QtCore.QRect(90, 20, 211, 16))
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setGeometry(QtCore.QRect(90, 40, 211, 16))
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Georgian")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{\n"
"text-align: center;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.frame_4)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(290, 200))
        self.tableWidget.setMaximumSize(QtCore.QSize(302, 199))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.frame_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Adicionar codigo aqui
        self.tmp = None # Onde sera armazenado a imagem do dysplay
        self.fps=0
        self.started = False

        self.armazenando_image = None #1° Imagens capturadas do rosto
        self.captura = None

    def loadImage(self):
        """
            Esta função inicializara a camera Inicializar a camera.
            :return:
        """
        if self.started:
            self.started = False
            self.cad_img_pushButton_start_camera.setText('Ligar a Camera')
            self.armazenando_image = None  # 1° Imagens capturadas do rosto
            #self.armazenando_image_2 = None  # 2° Imagens capturadas do rosto
            #self.armazenando_image_3 = None  # 3° Imagens capturadas do rosto
            self.setPhoto_imagem(cv2.imread("../../imagens/Frame 19 (1).png"), 0)
            self.setPhoto_imagem(cv2.imread("../../imagens/Frame 19 (1).png"), 1)
            self.setPhoto_imagem(cv2.imread("../../imagens/Frame 19 (1).png"), 2)
            image_flag = cv2.imread("../../imagens/Group 144.png")
            self.setPhoto(self.flag_foto_1,image_flag,h=27,w=24)
            self.setPhoto(self.flag_foto_2,image_flag,h=27,w=24)
            self.setPhoto(self.flag_foto_3,image_flag,h=27,w=24)
            self.flag_captura = 0
            self.cont_aramzena_image = 0
        else:
            self.flag_captura = 1
            self.started = True
            self.cad_img_pushButton_start_camera.setText('Desligar a Camera')



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

            maior_dimencao = 0
            x_p = None
            for (x,y,w,h) in faces:
                if(maior_dimencao <= 2**((x-x+w) * (y-y+h))):
                        x_p = x
                        y_p = y
                        w_p = w
                        h_p = h
                        maior_dimencao = 2**((x-x+w) * (y-y+h))
                        #print('-- CAPTURA --',type(captura))
                        #print('-- IMAGEM --', type(self.image))
            if x_p != None:
                self.captura = self.image[y_p:y_p + h_p, x_p:x_p + w_p]
                cv2.rectangle(self.image, (x_p, y_p), (x_p + w_p, y_p + h_p), (20, 255, 57), 5)
                #cv2.circle(self.image,(x_p, y_p),10,(255, 0, 0), 3)
                #cv2.circle(self.image,(w_p+x, h_p+y),10, (0, 0, 255), 3)

                #Armazenar as imagens dos rostos detectados
                #Armazenar as imagens dos rostos detectados


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
            if self.started == False:
                    self.image = cv2.imread("../../imagens/Frame 1.png")
                    #self.update()
                    self.setPhoto(self.display_camera,self.image)
                    break #Loop break

    def captura_face(self):
        try:
            if(self.cont_aramzena_image <= 4):
                self.setPhoto_imagem(self.captura, self.cont_aramzena_image)
                self.cont_aramzena_image += 1
        except:
            pass

    def setPhoto(self,display,image,h=300, w=502):
            
        """
            Essa função vair utilizar a imagem passadapor parametro realizar o
            preprocessamento ajustando seu diametro e inserindo no display da
            da interface.
            :param image:
            :return:
        """
        self.tmp = image
        image = imutils.resize(image, height=h, width=w)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        display.setPixmap(QtGui.QPixmap.fromImage(image))

    def setPhoto_imagem(self,image,flag):
        """
            Essa função vair utilizar a imagem passadapor parametro realizar o
            preprocessamento ajustando seu diametro e inserindo no display da
            da interface.
            :param image:
            :return:
        """
        #self.tmp = image
        image_copy = image
        image = imutils.resize(image, height=90, width=90)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame,frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        image_flag = cv2.imread("../../imagens/Group 143.png")
        #cv2.imwrite('teste_2.png', image)

        if flag == 0:
            self.armazenando_image_1 = image_copy
            self.image_1.setPixmap(QtGui.QPixmap.fromImage(image))
            self.setPhoto(self.flag_foto_1,image_flag,h=27,w=24)
            #QMessageBox.information(None, 'Foto Captuirada', 'Captura da 1 foto!')
        if flag == 1:
            self.armazenando_image_2 = image_copy
            self.Image_2.setPixmap(QtGui.QPixmap.fromImage(image))
            self.setPhoto(self.flag_foto_2,image_flag,h=27,w=24)
            #QMessageBox.information(None, 'Foto Captuirada', 'Captura da 2 foto!')
        if flag == 2:
            self.armazenando_image_3 = image_copy
            self.Image_3.setPixmap(QtGui.QPixmap.fromImage(image))
            self.setPhoto(self.flag_foto_3,image_flag,h=27,w=24)
            #QMessageBox.information(None, 'Foto Captuirada', 'Captura da 3 foto!')


    def update(self):
        """

            :return:
        """
        img = self.image
        #text = 'FPS: '+str(self.fps)
        #img = ps.putBText(img,text,text_offset_x=20,text_offset_y=30,vspace=20,hspace=10, font_scale=1.0,background_RGB=(10,20,222),text_RGB=(255,255,255))
        #text = str(time.strftime("%H:%M %p"))
        #img = ps.putBText(img, text, text_offset_x=self.image.shape[1] - 180, text_offset_y=30, vspace=20, hspace=10,
                          #font_scale=1.0, background_RGB=(228, 20, 222), text_RGB=(255, 255, 255))

        self.setPhoto(self.display_camera,img)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Identificação do Individuo"))
        self.rec_facial_pushButton_voltar.setText(_translate("MainWindow", "<< Voltar"))
        self.label_3.setText(_translate("MainWindow", "Individuo"))
        self.label_7.setText(_translate("MainWindow", "Email:"))
        self.label_6.setText(_translate("MainWindow", "Nome:"))
        self.label_4.setText(_translate("MainWindow", "ID:"))
        self.label_8.setText(_translate("MainWindow", "..."))
        self.label_9.setText(_translate("MainWindow", "..."))
        self.label_10.setText(_translate("MainWindow", "..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Hora"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = reconhecimento_facial_individuo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

