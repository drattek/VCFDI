# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'validar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_Validar(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(340, 450)
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
        self.rfc = QLabel(self.widget)
        self.rfc.setObjectName(u"rfc")
        self.rfc.setGeometry(QRect(30, 100, 110, 30))
        self.rfc.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rfc.setText(u"RFC")
        self.rfc.setAlignment(Qt.AlignCenter)
        self.passw = QLabel(self.widget)
        self.passw.setObjectName(u"passw")
        self.passw.setGeometry(QRect(30, 140, 110, 30))
        self.passw.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.passw.setAlignment(Qt.AlignCenter)
        self.rfc_input = QLineEdit(self.widget)
        self.rfc_input.setObjectName(u"rfc_input")
        self.rfc_input.setGeometry(QRect(170, 100, 140, 30))
        self.rfc_input.setFocusPolicy(Qt.NoFocus)
        self.rfc_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(40, 40, 40);\n"
"	border:none;\n"
"	color: rgb(255,255,255);\n"
"}")
        self.rfc_input.setMaxLength(13)
        self.rfc_input.setAlignment(Qt.AlignCenter)
        self.rfc_input.setPlaceholderText(u"RFC")
        self.rfc_input.setClearButtonEnabled(False)
        self.pass_input = QLineEdit(self.widget)
        self.pass_input.setObjectName(u"pass_input")
        self.pass_input.setGeometry(QRect(170, 140, 140, 30))
        self.pass_input.setStyleSheet(u"QLineEdit {\n"
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
        self.pass_input.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.pass_input.setAlignment(Qt.AlignCenter)
        self.pass_input.setClearButtonEnabled(True)
        self.cer_button = QPushButton(self.widget)
        self.cer_button.setObjectName(u"cer_button")
        self.cer_button.setGeometry(QRect(30, 20, 110, 30))
        self.cer_button.setStyleSheet(u"QPushButton {\n"
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
        self.cer_button.setAutoDefault(True)
        self.cer_input = QLineEdit(self.widget)
        self.cer_input.setObjectName(u"cer_input")
        self.cer_input.setGeometry(QRect(170, 20, 140, 30))
        self.cer_input.setFocusPolicy(Qt.NoFocus)
        self.cer_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(40, 40, 40);\n"
"	border:none;\n"
"	color: rgb(255,255,255);\n"
"}")
        self.cer_input.setEchoMode(QLineEdit.Normal)
        self.cer_input.setAlignment(Qt.AlignCenter)
        self.cer_input.setReadOnly(True)
        self.cer_input.setPlaceholderText(u"cer")
        self.key_button = QPushButton(self.widget)
        self.key_button.setObjectName(u"key_button")
        self.key_button.setGeometry(QRect(30, 60, 110, 30))
        self.key_button.setStyleSheet(u"QPushButton {\n"
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
        self.key_button.setAutoDefault(True)
        self.key_input = QLineEdit(self.widget)
        self.key_input.setObjectName(u"key_input")
        self.key_input.setGeometry(QRect(170, 60, 140, 30))
        self.key_input.setFocusPolicy(Qt.NoFocus)
        self.key_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(40, 40, 40);\n"
"	border:none;\n"
"	color: rgb(255,255,255);\n"
"}")
        self.key_input.setEchoMode(QLineEdit.Normal)
        self.key_input.setAlignment(Qt.AlignCenter)
        self.key_input.setReadOnly(True)
        self.key_input.setPlaceholderText(u"key")
        self.request_button = QPushButton(self.widget)
        self.request_button.setObjectName(u"request_button")
        self.request_button.setGeometry(QRect(210, 395, 90, 35))
        self.request_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 130, 210);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font: bold;\n"
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
        self.request_button.setAutoDefault(True)
        self.page_button = QPushButton(self.widget)
        self.page_button.setObjectName(u"page_button")
        self.page_button.setGeometry(QRect(40, 395, 35, 35))
        self.page_button.setStyleSheet(u"QPushButton {\n"
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
        self.page_button.setAutoDefault(True)
        self.requestloop_button = QPushButton(self.widget)
        self.requestloop_button.setObjectName(u"requestloop_button")
        self.requestloop_button.setGeometry(QRect(85, 395, 115, 35))
        self.requestloop_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 130, 210);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font: bold;\n"
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
        self.requestloop_button.setAutoDefault(True)
        self.stop_button = QPushButton(self.widget)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(85, 395, 115, 35))
        self.stop_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(210, 50, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font: bold;\n"
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
        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 220, 280, 160))
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	background-color: rgb(70, 70, 70);\n"
"	border: none;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	color: rgb(255, 255, 255);\n"
"	height: 25px;\n"
"}\n"
"\n"
"QScrollBar {\n"
"	background-color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
" background-color: rgb(95, 95, 95);\n"
"	border: none;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"	background-color: rgb(40, 40, 40) ;\n"
"}")
        self.listWidget.setFrameShape(QFrame.StyledPanel)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setWordWrap(True)
        self.status = QLabel(self.widget)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(40, 180, 160, 30))
        self.status.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: bold;")
        self.status.setAlignment(Qt.AlignCenter)
        self.delete_button = QPushButton(self.widget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(240, 185, 60, 20))
        self.delete_button.setStyleSheet(u"QPushButton {\n"
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
        self.delete_button.setAutoDefault(True)
        self.refresh_button = QPushButton(self.widget)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setGeometry(QRect(210, 185, 20, 20))
        self.refresh_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 130, 210);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	font: bold;\n"
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
        self.refresh_button.setAutoDefault(True)
        self.stop_button.raise_()
        self.rfc.raise_()
        self.passw.raise_()
        self.rfc_input.raise_()
        self.pass_input.raise_()
        self.cer_button.raise_()
        self.cer_input.raise_()
        self.key_button.raise_()
        self.key_input.raise_()
        self.request_button.raise_()
        self.page_button.raise_()
        self.requestloop_button.raise_()
        self.listWidget.raise_()
        self.status.raise_()
        self.delete_button.raise_()
        self.refresh_button.raise_()
        QWidget.setTabOrder(self.cer_button, self.key_button)
        QWidget.setTabOrder(self.key_button, self.pass_input)
        QWidget.setTabOrder(self.pass_input, self.refresh_button)
        QWidget.setTabOrder(self.refresh_button, self.delete_button)
        QWidget.setTabOrder(self.delete_button, self.listWidget)
        QWidget.setTabOrder(self.listWidget, self.request_button)
        QWidget.setTabOrder(self.request_button, self.requestloop_button)
        QWidget.setTabOrder(self.requestloop_button, self.stop_button)
        QWidget.setTabOrder(self.stop_button, self.page_button)

        self.retranslateUi(Form)

        self.cer_button.setDefault(False)
        self.key_button.setDefault(False)
        self.listWidget.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.passw.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.pass_input.setPlaceholderText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.cer_button.setText(QCoreApplication.translate("Form", u"Archivo .cer", None))
        self.key_button.setText(QCoreApplication.translate("Form", u"Archivo .key", None))
        self.request_button.setText(QCoreApplication.translate("Form", u"Validar", None))
        self.page_button.setText(QCoreApplication.translate("Form", u"\u2ba8", None))
#if QT_CONFIG(shortcut)
        self.page_button.setShortcut(QCoreApplication.translate("Form", u"Shift+Esc", None))
#endif // QT_CONFIG(shortcut)
        self.requestloop_button.setText(QCoreApplication.translate("Form", u"Validar en bucle", None))
        self.stop_button.setText(QCoreApplication.translate("Form", u"Detener", None))
        self.status.setText(QCoreApplication.translate("Form", u"Selecciona la solicitud", None))
        self.delete_button.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.refresh_button.setText(QCoreApplication.translate("Form", u"\u2b6e", None))
    # retranslateUi

