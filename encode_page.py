# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encode_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 700)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.label.setStyleSheet("border-image: url(:/images/hacker.jpg);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(590, 110, 541, 541))
        self.label_3.setStyleSheet("background-color:rgba(0,0,0,100);\n"
"border-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.encodeButton = QtWidgets.QPushButton(self.widget)
        self.encodeButton.setGeometry(QtCore.QRect(880, 550, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.encodeButton.setFont(font)
        self.encodeButton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"   color:rgba(255, 255, 255, 210);\n"
"   border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"   }\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.encodeButton.setObjectName("encodeButton")
        self.messageTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.messageTextEdit.setGeometry(QtCore.QRect(640, 150, 431, 341))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.messageTextEdit.setFont(font)
        self.messageTextEdit.setStyleSheet("background-color:rgba(0,0,0,150);\n"
"color: rgb(255, 170, 0);\n"
"border-radius:15px;")
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.selectButton = QtWidgets.QPushButton(self.widget)
        self.selectButton.setGeometry(QtCore.QRect(130, 540, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.selectButton.setFont(font)
        self.selectButton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"   color:rgba(255, 255, 255, 210);\n"
"   border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"   }\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.selectButton.setObjectName("selectButton")
        self.saveButton = QtWidgets.QPushButton(self.widget)
        self.saveButton.setGeometry(QtCore.QRect(330, 540, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"   color:rgba(255, 255, 255, 210);\n"
"   border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"   }\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.saveButton.setObjectName("saveButton")
        self.backButton = QtWidgets.QPushButton(self.widget)
        self.backButton.setGeometry(QtCore.QRect(20, 630, 70, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("border-image: url(:/images/images.jpeg);\n"
"border-radius:20px")
        self.backButton.setText("")
        self.backButton.setObjectName("backButton")
        self.titleframe = QtWidgets.QFrame(self.widget)
        self.titleframe.setGeometry(QtCore.QRect(0, 0, 1200, 90))
        self.titleframe.setStyleSheet("border-radius:20px;")
        self.titleframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleframe.setObjectName("titleframe")
        self.minimizeButton = QtWidgets.QPushButton(self.titleframe)
        self.minimizeButton.setGeometry(QtCore.QRect(1090, 10, 51, 41))
        self.minimizeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/chrome-minimize-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeButton.setIcon(icon)
        self.minimizeButton.setIconSize(QtCore.QSize(40, 40))
        self.minimizeButton.setObjectName("minimizeButton")
        self.label_6 = QtWidgets.QLabel(self.titleframe)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 60, 60))
        self.label_6.setStyleSheet("image: url(:/images/logoimgae.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.titleframe)
        self.label_5.setGeometry(QtCore.QRect(90, 30, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.closeButton = QtWidgets.QPushButton(self.titleframe)
        self.closeButton.setGeometry(QtCore.QRect(1140, 10, 51, 41))
        self.closeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/—Pngtree—check mark and cross gradient_15118783.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon1)
        self.closeButton.setIconSize(QtCore.QSize(36, 36))
        self.closeButton.setObjectName("closeButton")
        self.encodeImageLabel = QtWidgets.QLabel(self.widget)
        self.encodeImageLabel.setGeometry(QtCore.QRect(110, 110, 400, 400))
        self.encodeImageLabel.setStyleSheet("background-color:rgba(0,0,0,100);\n"
"border-radius:15px;")
        self.encodeImageLabel.setText("")
        self.encodeImageLabel.setObjectName("encodeImageLabel")
        self.encryptButton = QtWidgets.QPushButton(self.widget)
        self.encryptButton.setGeometry(QtCore.QRect(630, 550, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.encryptButton.setFont(font)
        self.encryptButton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"   color:rgba(255, 255, 255, 210);\n"
"   border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"   }\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.encryptButton.setObjectName("encryptButton")
        self.histogramButton = QtWidgets.QPushButton(self.widget)
        self.histogramButton.setGeometry(QtCore.QRect(610, 620, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.histogramButton.setFont(font)
        self.histogramButton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"   color:rgba(255, 255, 255, 210);\n"
"   border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"   }\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.histogramButton.setObjectName("histogramButton")

        self.retranslateUi(Dialog)
        self.closeButton.clicked.connect(Dialog.close) # type: ignore
        self.minimizeButton.clicked.connect(Dialog.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.encodeButton.setText(_translate("Dialog", "ENCODE"))
        self.messageTextEdit.setPlaceholderText(_translate("Dialog", " Type Your Text Here"))
        self.selectButton.setText(_translate("Dialog", "Select Image"))
        self.saveButton.setText(_translate("Dialog", "Save Image"))
        self.label_5.setText(_translate("Dialog", "STEGHIDE"))
        self.encryptButton.setText(_translate("Dialog", "ENCRYPT"))
        self.histogramButton.setText(_translate("Dialog", "ENCRYPT"))
import source_img_rc
