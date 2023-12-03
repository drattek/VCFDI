# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_Menu(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(339, 445)
        Form.setStyleSheet(u"QMenu {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(43, 43, 43);\n"
"	font-size: 11px;\n"
"}\n"
"\n"
" QToolButton QMenu::item:selected {\n"
"	background: rgb(34, 62, 85);\n"
"}")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 340, 450))
        self.widget.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.solicitar_button = QPushButton(self.widget)
        self.solicitar_button.setObjectName(u"solicitar_button")
        self.solicitar_button.setGeometry(QRect(50, 50, 240, 40))
        self.solicitar_button.setFocusPolicy(Qt.StrongFocus)
        self.solicitar_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(95, 95, 95);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	outline: none;\n"
"	background-color: rgb(95, 95, 95);\n"
"}")
        self.validar_button = QPushButton(self.widget)
        self.validar_button.setObjectName(u"validar_button")
        self.validar_button.setGeometry(QRect(50, 110, 240, 40))
        self.validar_button.setFocusPolicy(Qt.StrongFocus)
        self.validar_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(95, 95, 95);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	outline: none;\n"
"	background-color: rgb(95, 95, 95);\n"
"}")
        self.xml_v_button = QPushButton(self.widget)
        self.xml_v_button.setObjectName(u"xml_v_button")
        self.xml_v_button.setGeometry(QRect(50, 170, 240, 40))
        self.xml_v_button.setFocusPolicy(Qt.StrongFocus)
        self.xml_v_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(95, 95, 95);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	outline: none;\n"
"	background-color: rgb(95, 95, 95);\n"
"}")
        self.Bienvenido = QLabel(self.widget)
        self.Bienvenido.setObjectName(u"Bienvenido")
        self.Bienvenido.setGeometry(QRect(70, 0, 200, 50))
        self.Bienvenido.setFocusPolicy(Qt.NoFocus)
        self.Bienvenido.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	font: bold;\n"
"	font-size: 18pt;\n"
"}")
        self.Bienvenido.setAlignment(Qt.AlignCenter)
        self.txt_button = QPushButton(self.widget)
        self.txt_button.setObjectName(u"txt_button")
        self.txt_button.setGeometry(QRect(50, 230, 180, 40))
        self.txt_button.setFocusPolicy(Qt.StrongFocus)
        self.txt_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(95, 95, 95);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	outline: none;\n"
"	background-color: rgb(95, 95, 95);\n"
"}")
        self.util_button = QPushButton(self.widget)
        self.util_button.setObjectName(u"util_button")
        self.util_button.setGeometry(QRect(100, 400, 140, 20))
        self.util_button.setFocusPolicy(Qt.StrongFocus)
        self.util_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(95, 95, 95);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	outline: none;\n"
"	background-color: rgb(95, 95, 95);\n"
"}")
        self.file_button = QPushButton(self.widget)
        self.file_button.setObjectName(u"file_button")
        self.file_button.setGeometry(QRect(250, 230, 40, 40))
        self.file_button.setFocusPolicy(Qt.StrongFocus)
        self.file_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(95, 95, 95);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	outline: none;\n"
"	background-color: rgb(95, 95, 95);\n"
"}")
        self.return_button = QPushButton(self.widget)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setGeometry(QRect(250, 230, 40, 40))
        self.return_button.setFocusPolicy(Qt.StrongFocus)
        self.return_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(95, 95, 95);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	outline: none;\n"
"	background-color: rgb(95, 95, 95);\n"
"}")
        self.delimiter_input = QLineEdit(self.widget)
        self.delimiter_input.setObjectName(u"delimiter_input")
        self.delimiter_input.setGeometry(QRect(90, 295, 160, 30))
        self.delimiter_input.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(40, 40, 40);\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(180, 180, 180);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-bottom: 1px solid rgb(0, 110, 190);\n"
"}")
        self.delimiter_input.setMaxLength(1)
        self.delimiter_input.setEchoMode(QLineEdit.Normal)
        self.delimiter_input.setAlignment(Qt.AlignCenter)
        self.delimiter_input.setClearButtonEnabled(True)
        self.export_button = QPushButton(self.widget)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setGeometry(QRect(90, 350, 160, 20))
        self.export_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 130, 210);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(0, 105, 185);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 110, 190);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	outline: none;\n"
"	background-color: rgb(0, 110, 190);\n"
"}")
        self.export_button.setAutoDefault(True)
        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 300, 240, 30))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(70, 70, 70);\n"
"	border-radius: 1px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(0, 130, 210);\n"
"	border-radius: 1px;\n"
"	color: rgb(70, 211, 0);\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.stop_button = QPushButton(self.widget)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(120, 350, 100, 20))
        self.stop_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(210, 50, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(185, 25, 45);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 75, 95);\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	outline: none;\n"
"	background-color: rgb(185, 25, 45);\n"
"}")
        self.stop_button.setAutoDefault(True)
        self.stop_button.raise_()
        self.return_button.raise_()
        self.solicitar_button.raise_()
        self.validar_button.raise_()
        self.xml_v_button.raise_()
        self.Bienvenido.raise_()
        self.txt_button.raise_()
        self.util_button.raise_()
        self.file_button.raise_()
        self.delimiter_input.raise_()
        self.progressBar.raise_()
        self.export_button.raise_()
        QWidget.setTabOrder(self.solicitar_button, self.validar_button)
        QWidget.setTabOrder(self.validar_button, self.xml_v_button)
        QWidget.setTabOrder(self.xml_v_button, self.txt_button)
        QWidget.setTabOrder(self.txt_button, self.return_button)
        QWidget.setTabOrder(self.return_button, self.file_button)
        QWidget.setTabOrder(self.file_button, self.delimiter_input)
        QWidget.setTabOrder(self.delimiter_input, self.export_button)
        QWidget.setTabOrder(self.export_button, self.util_button)

        self.retranslateUi(Form)

        self.solicitar_button.setDefault(True)
        self.validar_button.setDefault(True)
        self.xml_v_button.setDefault(True)
        self.txt_button.setDefault(True)
        self.util_button.setDefault(True)
        self.file_button.setDefault(True)
        self.return_button.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.solicitar_button.setText(QCoreApplication.translate("Form", u"Solicitar descarga", None))
#if QT_CONFIG(shortcut)
        self.solicitar_button.setShortcut(QCoreApplication.translate("Form", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.validar_button.setText(QCoreApplication.translate("Form", u"Validar solicitud de descarga", None))
#if QT_CONFIG(shortcut)
        self.validar_button.setShortcut(QCoreApplication.translate("Form", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.xml_v_button.setText(QCoreApplication.translate("Form", u"CFDI a Excel", None))
#if QT_CONFIG(shortcut)
        self.xml_v_button.setShortcut(QCoreApplication.translate("Form", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.Bienvenido.setText(QCoreApplication.translate("Form", u"Bienvenido", None))
        self.txt_button.setText(QCoreApplication.translate("Form", u"Metadata o data stage a Excel", None))
#if QT_CONFIG(shortcut)
        self.txt_button.setShortcut(QCoreApplication.translate("Form", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.util_button.setText(QCoreApplication.translate("Form", u"Indicadores fiscales", None))
#if QT_CONFIG(shortcut)
        self.util_button.setShortcut(QCoreApplication.translate("Form", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.file_button.setText(QCoreApplication.translate("Form", u"...", None))
#if QT_CONFIG(shortcut)
        self.file_button.setShortcut(QCoreApplication.translate("Form", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.return_button.setText(QCoreApplication.translate("Form", u"\u2ba8", None))
#if QT_CONFIG(shortcut)
        self.return_button.setShortcut(QCoreApplication.translate("Form", u"Shift+Esc", None))
#endif // QT_CONFIG(shortcut)
        self.delimiter_input.setPlaceholderText(QCoreApplication.translate("Form", u"Delimitador personalizado", None))
        self.export_button.setText(QCoreApplication.translate("Form", u"Seleccionar el archivo", None))
#if QT_CONFIG(shortcut)
        self.export_button.setShortcut(QCoreApplication.translate("Form", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.stop_button.setText(QCoreApplication.translate("Form", u"Cancelar", None))
#if QT_CONFIG(shortcut)
        self.stop_button.setShortcut(QCoreApplication.translate("Form", u"6", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

