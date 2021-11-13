# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\ProyectosPY\MenuUmbrella\menu3.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 782)
        MainWindow.setStyleSheet("*{\n"
"\n"
"    border:none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(24,24,32);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menuslide = QtWidgets.QFrame(self.centralwidget)
        self.menuslide.setMinimumSize(QtCore.QSize(0, 0))
        self.menuslide.setMaximumSize(QtCore.QSize(0, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menuslide.setFont(font)
        self.menuslide.setStyleSheet("background-color:black;")
        self.menuslide.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuslide.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuslide.setObjectName("menuslide")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menuslide)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.slide = QtWidgets.QFrame(self.menuslide)
        self.slide.setMinimumSize(QtCore.QSize(198, 0))
        self.slide.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide.setObjectName("slide")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.slide)
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.slide)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.frame_7.setFont(font)
        self.frame_7.setStyleSheet("")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_12.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/umbrella.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QtCore.QSize(48, 40))
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_9.addWidget(self.pushButton_12, 0, QtCore.Qt.AlignLeft)
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setStyleSheet("color:white;\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_5.addWidget(self.frame_7, 0, QtCore.Qt.AlignLeft)
        self.frame_8 = QtWidgets.QFrame(self.slide)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("*{\n"
"color:white;\n"
"border-bottom: 2px solid white;\n"
"border-top: 2px solid white;\n"
"\n"
" }\n"
"\n"
"QPushButton:hover{\n"
"    color:red;\n"
"    border-bottom: 2px solid red;\n"
"    border-top: 2px solid red;\n"
"    font-size:20px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_7.addWidget(self.pushButton_4)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("*{\n"
"color:white;\n"
"border-bottom: 2px solid white;\n"
" }\n"
"\n"
"QPushButton:hover{\n"
"    color:red;\n"
"    border-bottom: 2px solid red;\n"
"    font-size:20px;\n"
"}")
        self.pushButton_10.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_7.addWidget(self.pushButton_10)
        self.pushButton_10.raise_()
        self.pushButton_4.raise_()
        self.verticalLayout_6.addWidget(self.frame_10, 0, QtCore.Qt.AlignTop)
        self.frame_15 = QtWidgets.QFrame(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_14.setContentsMargins(0, 50, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame_15)
        self.textEdit_5.setStyleSheet("QTextEdit{\n"
"\n"
"color:white;\n"
"}")
        self.textEdit_5.setObjectName("textEdit_5")
        self.verticalLayout_14.addWidget(self.textEdit_5)
        self.verticalLayout_6.addWidget(self.frame_15)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.slide)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setContentsMargins(14, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("*{\n"
"color:white;\n"
"\n"
"\n"
" }\n"
"\n"
"QPushButton:hover{\n"
"    color:red;\n"
"\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconos/icons8-ajustes-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QtCore.QSize(32, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_10.addWidget(self.pushButton_9, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.verticalLayout_2.addWidget(self.slide)
        self.horizontalLayout.addWidget(self.menuslide)
        self.menu = QtWidgets.QFrame(self.centralwidget)
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uno = QtWidgets.QFrame(self.menu)
        self.uno.setMinimumSize(QtCore.QSize(8, 0))
        font = QtGui.QFont()
        font.setKerning(True)
        self.uno.setFont(font)
        self.uno.setStyleSheet("background-color:black;")
        self.uno.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uno.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uno.setMidLineWidth(7)
        self.uno.setObjectName("uno")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.uno)
        self.horizontalLayout_2.setContentsMargins(8, 12, 8, 6)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.uno)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.volver = QtWidgets.QFrame(self.frame_3)
        self.volver.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.volver.setFrameShadow(QtWidgets.QFrame.Raised)
        self.volver.setObjectName("volver")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.volver)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btnvolver = QtWidgets.QPushButton(self.volver)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnvolver.setFont(font)
        self.btnvolver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnvolver.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconos/cil-justify-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnvolver.setIcon(icon2)
        self.btnvolver.setIconSize(QtCore.QSize(50, 50))
        self.btnvolver.setObjectName("btnvolver")
        self.horizontalLayout_8.addWidget(self.btnvolver, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout_6.addWidget(self.volver)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.uno)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.frame_2 = QtWidgets.QFrame(self.uno)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconos/cil-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7, 0, QtCore.Qt.AlignRight)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/iconos/cil-folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.horizontalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.uno)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 6, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/iconos/cil-window-minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/iconos/cil-media-stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/iconos/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.uno)
        self.stackedWidget = QtWidgets.QStackedWidget(self.menu)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_11 = QtWidgets.QFrame(self.page_0)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_11.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("color:white;")
        self.pushButton_11.setIconSize(QtCore.QSize(16, 40))
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_10.addWidget(self.pushButton_11, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("color:white;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_9.addWidget(self.textEdit_2)
        self.verticalLayout_10.addWidget(self.frame_12)
        self.verticalLayout_8.addWidget(self.frame_11, 0, QtCore.Qt.AlignTop)
        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_13 = QtWidgets.QFrame(self.page_1)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_13)
        self.textEdit_3.setStyleSheet("color:white;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_11.addWidget(self.textEdit_3)
        self.verticalLayout_13.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.page_1)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame_14)
        self.textEdit_4.setStyleSheet("color:white;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_12.addWidget(self.textEdit_4)
        self.verticalLayout_13.addWidget(self.frame_14)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textEdit = QtWidgets.QTextEdit(self.page_2)
        self.textEdit.setGeometry(QtCore.QRect(370, 180, 104, 87))
        self.textEdit.setStyleSheet("color:white;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.tres = QtWidgets.QFrame(self.menu)
        self.tres.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tres.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tres.setObjectName("tres")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tres)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.tres)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, 8)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_7.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"\n"
"    color:white;\n"
"\n"
"}")
        self.pushButton_8.setIconSize(QtCore.QSize(56, 48))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_4.addWidget(self.pushButton_8, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout_7.addWidget(self.frame_6)
        self.abajoderecha = QtWidgets.QFrame(self.frame_5)
        self.abajoderecha.setMinimumSize(QtCore.QSize(10, 10))
        self.abajoderecha.setMaximumSize(QtCore.QSize(10, 10))
        self.abajoderecha.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.abajoderecha.setFrameShadow(QtWidgets.QFrame.Raised)
        self.abajoderecha.setObjectName("abajoderecha")
        self.horizontalLayout_7.addWidget(self.abajoderecha, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.tres, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.menu)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        # activar textos al pasar el mouse por los botones

               
       # activar las dos paginas en el menu

        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.pushButton_10.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))



      #  funcion para poder deslizar el menu a un lado 

        self.btnvolver.clicked.connect(lambda: self.deslizarmenu())
        #cerrar el programa con la X
        self.pushButton_3.clicked.connect(lambda: exit())

        #funcion para deslizar el menu

    def deslizarmenu(self):

        ancho = self.menuslide.width()

        if ancho == 0:
                anchonuevo = 280
        else:
                anchonuevo = 0

        self.animation = QtCore.QPropertyAnimation(self.menuslide, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(ancho)
        self.animation.setEndValue(anchonuevo)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


 




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "UMBRELLA S.A"))
        self.pushButton_4.setText(_translate("MainWindow", "RASTREO FACIAL"))
        self.pushButton_10.setText(_translate("MainWindow", "RECONOCIMIENTO FACIAL"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DESCRIPCION DE </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">RASTREO FACIAL</p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "  AJUSTES"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_11.setText(_translate("MainWindow", "Bienvenido a RecFace"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gill Sans MT\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">RecFace es una aplicacion para poder detectar el reconocimiento facial en tiempo real</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Aqui iria la camara</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Aqui iria los algoritmos</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">pagina 2</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "Umbrella S.A"))
import Recursos.iconos


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
