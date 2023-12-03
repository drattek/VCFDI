# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)
import login_rc

class Ui_Login(object):
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
        self.login_button = QPushButton(self.widget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(70, 280, 200, 35))
        self.login_button.setStyleSheet(u"QPushButton {\n"
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
        self.login_button.setAutoDefault(True)
        self.logo = QWidget(self.widget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(70, 100, 200, 100))
        self.logo.setStyleSheet(u"image: url(:/images/Pocket_CFDI.svg);")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(140, 410, 60, 30))
        self.widget_2.setStyleSheet(u"image: url(:/images/eraro.svg);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.login_button.setText(QCoreApplication.translate("Form", u"Iniciar", None))
    # retranslateUi

