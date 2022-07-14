# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from test2_ui import Ui_Form       
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, 
                             QLabel, QVBoxLayout)    
import numpy as np
import os
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import sqlite3
from PyQt5.QtWidgets import QMessageBox





class video (QtWidgets.QDialog, Ui_Form):
    def __init__(self,sel):
        super().__init__()                  


        self.setupUi(self)                                 

        self.control_bt.clicked.connect(self.start_webcam)
        self.capture.clicked.connect(self.capture_image)
        self.capture.clicked.connect(self.startUIWindow)       
        self.selecteditems=sel
        
        self.image_label.setScaledContents(True)

        self.cap = None                                       

        self.timer = QtCore.QTimer(self, interval=5)
        self.timer.timeout.connect(self.update_frame)
        self._image_counter = 0

    @QtCore.pyqtSlot()
    def start_webcam(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
        self.timer.start()

    @QtCore.pyqtSlot()
    def update_frame(self):
        ret, image = self.cap.read()
        simage     = cv2.flip(image, 1)
        self.displayImage(image, True)

    @QtCore.pyqtSlot()
    def capture_image(self):
        flag, frame = self.cap.read()
        path = os.getcwd()                       # 
        if flag:
            QtWidgets.QApplication.beep()
            name = "resim.jpg"
            cv2.imwrite(os.path.join(path, name), frame)
            self._image_counter += 1

    def displayImage(self, img, window=True):
        qformat = QtGui.QImage.Format_Indexed8
        if len(img.shape)==3 :
            if img.shape[2]==4:
                qformat = QtGui.QImage.Format_RGBA8888
            else:
                qformat = QtGui.QImage.Format_RGB888
        outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        if window:
            self.image_label.setPixmap(QtGui.QPixmap.fromImage(outImage))
        
    def startUIWindow(self):
        #self.close()
        self.resimyolu=os.getcwd()+os.sep+"resim.jpg"
        

    def goWindow1(self):
        self.show()
        self.Window.hide()




class Ui_MainWindow(object):

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Tür Belirleme Programı")
        MainWindow.resize(1200, 450)
        self.item=True
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 290, 181, 91))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 60, 171, 16))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 90, 256, 192))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(470, 90, 661, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(750, 60, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1010, 650, 141, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.kamerayagec)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tür Belirleme Programı"))
        self.pushButton.setText(_translate("MainWindow", "Türü tanımla"))
        self.label.setText(_translate("MainWindow", "Lütfen Bir Cins Seçiniz"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Köpek"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Mantar"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Çiçek"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Kuş"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "Bulunan Tür Bilgileri"))
        self.label_3.setText(_translate("MainWindow", "Ekrem Dağ"))


    def verial(self):
        try:
            self.veriler=[]
            sqliteConnection = sqlite3.connect('canlilar.db')
            cursor = sqliteConnection.cursor()


            if self.listWidget.currentItem().text()=="Köpek":
                sql_select_query = """select * from kopek where Cinsi = ?"""
                cursor.execute(sql_select_query, (self.cins,))
                records = cursor.fetchall()
                for row in records:
                    self.veriler.append([row[0],row[1],row[2],row[3]])
            elif self.listWidget.currentItem().text()=="Mantar":
                sql_select_query = """select * from mantar where Bilinenadi = ?"""
                cursor.execute(sql_select_query, (self.cins,))
                records = cursor.fetchall()
                for row in records:
                    self.veriler.append([row[0],row[1],row[2],row[3],row[4]])
            elif self.listWidget.currentItem().text()=="Kuş":
                sql_select_query = """select * from kus where Ad = ?"""
                cursor.execute(sql_select_query, (self.cins,))
                records = cursor.fetchall()
                for row in records:
                    self.veriler.append([row[0],row[1],row[2],row[3],row[4]])
            elif self.listWidget.currentItem().text()=="Çiçek":
                sql_select_query = """select * from cicek where Ad = ?"""
                cursor.execute(sql_select_query, (self.cins,))
                records = cursor.fetchall()
                for row in records:
                    self.veriler.append([row[0],row[1],row[2]])


            cursor.close()
            return self.veriler
        except sqlite3.Error as error:
            print("Veriler Okunurken Hatayla karşılaşıldı", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("Veritabanı Bağlantısı kapatıldı")

    def tabloya_yaz(self):
        self.tableWidget.setRowCount(2)
        if self.listWidget.currentItem().text()=="Köpek":
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem("Köpek id"))
            self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem("Cinsi"))
            self.tableWidget.setItem(0,2,QtWidgets.QTableWidgetItem("Ortalama Yaşam Süresi"))
            self.tableWidget.setItem(0,3,QtWidgets.QTableWidgetItem("Köken"))
        elif self.listWidget.currentItem().text()=="Mantar":
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem("Mantar id"))
            self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem("Latince adı"))
            self.tableWidget.setItem(0,2,QtWidgets.QTableWidgetItem("Bilinen adı"))
            self.tableWidget.setItem(0,3,QtWidgets.QTableWidgetItem("Yenilebilir"))
            self.tableWidget.setItem(0,4,QtWidgets.QTableWidgetItem("Değeri"))
        elif self.listWidget.currentItem().text()=="Kuş":
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem("Kuş id"))
            self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem("Ad"))
            self.tableWidget.setItem(0,2,QtWidgets.QTableWidgetItem("Bölge"))
            self.tableWidget.setItem(0,3,QtWidgets.QTableWidgetItem("İklim"))
            self.tableWidget.setItem(0,4,QtWidgets.QTableWidgetItem("EvdeBeslenmesi"))
        elif self.listWidget.currentItem().text()=="Çiçek":
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem("Çiçek id"))
            self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem("Ad"))
            self.tableWidget.setItem(0,2,QtWidgets.QTableWidgetItem("Bölge"))

        satir=0
        sutun=0
        for i in self.veriler:
            print(satir)
            satir+=1
            sutun=0
            for j in i:
                print(j)
                self.tableWidget.setItem(satir,sutun,QtWidgets.QTableWidgetItem(str(j)))
                sutun+=1
        
        self.tableWidget.setColumnCount(sutun)

    def kamerayagec(self):
        
        self.camerawindow = video(self.listWidget.currentItem().text())
        
        self.camerawindow.setWindowTitle('Resim Çek')
        self.camerawindow.capture.clicked.connect(self.changewindow)
        self.camerawindow.show()
        
        
    def changewindow(self):
        imgpath=self.camerawindow.resimyolu

        class_names=['gul', 'guvercin', 'kangal', 'kulturmantari']
        modelpath=os.getcwd()+os.sep+"model"
        model = keras.models.load_model(modelpath)
        img = keras.preprocessing.image.load_img(
            str(imgpath), target_size=(180, 180)
        )
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0) 

        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(class_names[np.argmax(score)], 100 * np.max(score))
        )
        self.camerawindow.close()
        
        if self.listWidget.currentItem().text()=="Köpek" and class_names[np.argmax(score)]=="kangal":
            self.cins="Kangal"
            msg.setWindowTitle(self.cins)
            msg.setText(self.cins+" bilgileri veritabanından getirildi")
            x = msg.exec_()
            self.verial()
            self.tabloya_yaz()

        elif self.listWidget.currentItem().text()=="Mantar" and class_names[np.argmax(score)]=="kulturmantari":
            self.cins="Kültür Mantarı"
            msg.setWindowTitle(self.cins)
            msg.setText(self.cins+" bilgileri veritabanından getirildi")
            x = msg.exec_()
            self.verial()
            self.tabloya_yaz()
    
        elif self.listWidget.currentItem().text()=="Çiçek" and class_names[np.argmax(score)]=="gul":
            self.cins="Gül"
            msg.setWindowTitle(self.cins)
            msg.setText(self.cins+" bilgileri veritabanından getirildi")
            x = msg.exec_()
            self.verial()
            self.tabloya_yaz()
        elif self.listWidget.currentItem().text()=="Kuş" and class_names[np.argmax(score)]=="guvercin":
            self.cins="Güvercin"
            msg.setWindowTitle(self.cins)
            msg.setText(self.cins+" bilgileri veritabanından getirildi")
            x = msg.exec_()
            self.verial()
            self.tabloya_yaz()
        else:
            msg.setWindowTitle("Hata")
            msg.setText("Resimdeki canlı bulunamadı")
            x = msg.exec_()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    mainwindow=Ui_MainWindow()
    msg = QMessageBox()
    mainwindow.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

