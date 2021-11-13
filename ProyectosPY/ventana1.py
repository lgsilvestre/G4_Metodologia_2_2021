import sys
from PyQt5 import QtCore, QtGui, QtWidgets


from Principal.MenuUmbrella.menuumbrella import Ui_MainWindow

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1400, 794)
        mainWindow.setMinimumSize(QtCore.QSize(1200, 794))
        mainWindow.setMaximumSize(QtCore.QSize(1400, 794))
        mainWindow.setStyleSheet("*{\n"
"    font-family:century gothic;\n""    font-size:40\n""}\n""\n""\n""QFrame{\n""    background: transparent;\n""    border-width: 2px;\n""    border-radius:15px;\n"
"      border-style: solid;\n""    border-color: white;\n""}\n""\n""#btningresar{\n""    background: transparent;\n""     border-style: solid;\n"
"    border-color: white;\n""    border-width: 2px;\n""    border-radius:8px;\n""    font-size:18px;\n""\n""}\n""\n"
"#pushButton_2{\n"
"    background: transparent;\n""    border-radius:60px;\n""\n""\n""}\n""QLabel{\n""background:0A2732;\n""color:white;\n"
"font-size: 30px;\n""\n""}\n""\n""QPushButton{\n""    color:white;\n""}\n""\n""QPushButton{\n""    color:white;\n""}\n""#btningresar:hover{\n"
"        background:black;\n"
"        border-style: solid;\n"
"        border-color: white;\n"
"        border-width: 2px;\n"
"        color:red;\n"
"}\n"
"\n"
"#usuario{\n"
"\n"
"    font-size:18px;\n"
"    border-radius:4px;\n"
"    \n"
"\n"
"\n"
"}\n"
"\n"
"#password{\n"
"\n"
"    font-size:18px;\n"
"    border-radius:4px;\n"
"    \n"
"\n"
"\n"
"}\n"
"#textEdit{\n"
"\n"
"    font-size:18px;\n"
"    background:transparent;\n"
"    border-radius:transparent;\n"
"    color:white;\n"
"\n"
"}\n"
"\n"
"#inicia{\n"
"    \n"
"border:transparent;\n"
"color:white;\n"
"font-size:40px;\n"
"font-family: arial;\n"
"}\n"
"\n"
"\n"
"#inicia_2{\n"
"    \n"
"border:transparent;\n"
"color:white;\n"
"font-size:13px;\n"
"}\n"
"\n"
"\n"
"#inicia_3{\n"
"    \n"
"border:transparent;\n"
"color:white;\n"
"font-size:13px;\n"
"}\n"
"\n"
"#error{\n"
"    background: #DA1515;\n"
"    border-radius:8px;\n"
"    font-size:16px;\n"
"\n"
"}\n"
"\n"
"#errorbtn{\n"
"    background: transparent;\n"
"    border-radius:4px;\n"
"    font-size:16px;\n"
"\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"    border-width: 1px;\n"
"    border-radius:8px;\n"
"}\n"
"\n"
"#errorbtn:hover{\n"
"    background: black;\n"
"    border-radius:4px;\n"
"    font-size:16px;\n"
"    border-style: solid;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"    border-radius:8px;\n"
"}\n"
"")
        mainWindow.setIconSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 140, 451, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btningresar = QtWidgets.QPushButton(self.frame)
        self.btningresar.setGeometry(QtCore.QRect(30, 390, 391, 51))
        self.btningresar.setObjectName("btningresar")
        self.btningresar.clicked.connect(self.abrir) # funcion para mostrar error en la contraseña
        self.usuario = QtWidgets.QLineEdit(self.frame)
        self.usuario.setEnabled(True)
        self.usuario.setGeometry(QtCore.QRect(60, 150, 341, 51))
        self.usuario.setMouseTracking(True)
        self.usuario.setAcceptDrops(True)
        self.usuario.setInputMask("")
        self.usuario.setText("")
        self.usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.usuario.setDragEnabled(True)
        self.usuario.setReadOnly(False)
        self.usuario.setClearButtonEnabled(True)
        self.usuario.setObjectName("usuario")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setEnabled(True)
        self.password.setGeometry(QtCore.QRect(60, 230, 341, 51))
        self.password.setMouseTracking(True)
        self.password.setAcceptDrops(True)
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setDragEnabled(True)
        self.password.setReadOnly(False)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inicia = QtWidgets.QLabel(self.frame)
        self.inicia.setGeometry(QtCore.QRect(70, 70, 321, 51))
        self.inicia.setScaledContents(False)
        self.inicia.setAlignment(QtCore.Qt.AlignCenter)
        self.inicia.setObjectName("inicia")
        self.inicia_2 = QtWidgets.QLabel(self.frame)
        self.inicia_2.setGeometry(QtCore.QRect(60, 330, 141, 51))
        self.inicia_2.setScaledContents(False)
        self.inicia_2.setAlignment(QtCore.Qt.AlignCenter)
        self.inicia_2.setObjectName("inicia_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(39, 340, 21, 31))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.inicia_3 = QtWidgets.QLabel(self.frame)
        self.inicia_3.setGeometry(QtCore.QRect(210, 330, 251, 51))
        self.inicia_3.setScaledContents(False)
        self.inicia_3.setAlignment(QtCore.Qt.AlignCenter)
        self.inicia_3.setObjectName("inicia_3")
        self.pushButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 30, 241, 221))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/umbrella.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(400, 600))
        self.pushButton_2.setObjectName("pushButton_2")
        self.error = QtWidgets.QPushButton(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(60, 660, 451, 51))
        self.error.setObjectName("error")
        self.errorbtn = QtWidgets.QPushButton(self.centralwidget)
        self.errorbtn.setEnabled(True)
        self.errorbtn.setGeometry(QtCore.QRect(450, 670, 41, 31))
        self.errorbtn.setIconSize(QtCore.QSize(14, 16))
        self.errorbtn.setObjectName("errorbtn")
        self.fondo = QtWidgets.QPushButton(self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(-30, -250, 1451, 1051))
        self.fondo.setAutoFillBackground(False)
        self.fondo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logos/umbrellafondo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fondo.setIcon(icon1)
        self.fondo.setIconSize(QtCore.QSize(3000, 1200))
        self.fondo.setObjectName("fondo")
        self.fondo.raise_()
        self.frame.raise_()
        self.pushButton_2.raise_()
        self.error.raise_()
        self.errorbtn.raise_()
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


    # FUNCIONES 

        self.errorbtn.hide()        # Inicia el programa con el error sin mostrarse
        self.error.hide()

        self.errorbtn.clicked.connect(lambda: self.error.hide())            # Remover el error dandole a la "X"
        self.errorbtn.clicked.connect(lambda: self.errorbtn.hide())

    def abrir(self):        # funcion que crea una nueva ventana y manda a llamar a la ventana 2

        nombre = self.usuario.text()
        contraseña = self.password.text()


        if(nombre == "nicolas@gmail.com" and contraseña == "nicolas" or nombre == "a" and contraseña == "a" or nombre == "diego@gmail.com" and contraseña == "diego" or nombre == "romina@gmail.com" and contraseña == "romina" or nombre == "victor@gmail.com" and contraseña == "victor"):

            self.ventana2 = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.ventana2)          # Se cierra la primera ventana y se abre la segunda
            self.ventana2.show()
            mainWindow.destroy()
        else:       
            self.errorbtn.show()        # EL programa muestra la barra de error
            self.error.show()


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "RecFace"))
        self.btningresar.setText(_translate("mainWindow", "INGRESAR"))
        self.usuario.setPlaceholderText(_translate("mainWindow", "Usuario"))
        self.password.setPlaceholderText(_translate("mainWindow", "Contraseña"))
        self.inicia.setText(_translate("mainWindow", "INICIAR SESION"))
        self.inicia_2.setText(_translate("mainWindow", "Recordar Contraseña"))
        self.inicia_3.setText(_translate("mainWindow", "Olvidaste la Contraseña?"))
        self.pushButton_2.setText(_translate("mainWindow", "INICIA SESION"))
        self.error.setText(_translate("mainWindow", "Usuario o Contraseña Incorrecta"))
        self.errorbtn.setText(_translate("mainWindow", "X"))
import Recursos.imagenes


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
