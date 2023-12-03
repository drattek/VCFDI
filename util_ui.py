# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'util.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Util(object):
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
        self.dolar_button = QPushButton(self.widget)
        self.dolar_button.setObjectName(u"dolar_button")
        self.dolar_button.setGeometry(QRect(50, 80, 240, 30))
        self.dolar_button.setFocusPolicy(Qt.StrongFocus)
        self.dolar_button.setStyleSheet(u"QPushButton {\n"
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
        self.inpc_button = QPushButton(self.widget)
        self.inpc_button.setObjectName(u"inpc_button")
        self.inpc_button.setGeometry(QRect(50, 220, 110, 30))
        self.inpc_button.setFocusPolicy(Qt.StrongFocus)
        self.inpc_button.setStyleSheet(u"QPushButton {\n"
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
        self.inpc_button.setAutoRepeatInterval(100)
        self.currency_button = QPushButton(self.widget)
        self.currency_button.setObjectName(u"currency_button")
        self.currency_button.setGeometry(QRect(50, 150, 240, 30))
        self.currency_button.setFocusPolicy(Qt.StrongFocus)
        self.currency_button.setStyleSheet(u"QPushButton {\n"
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
        self.indicadores = QLabel(self.widget)
        self.indicadores.setObjectName(u"indicadores")
        self.indicadores.setGeometry(QRect(70, 20, 200, 50))
        self.indicadores.setFocusPolicy(Qt.NoFocus)
        self.indicadores.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	font: bold;\n"
"	font-size: 14pt;\n"
"}")
        self.indicadores.setAlignment(Qt.AlignCenter)
        self.udi_button = QPushButton(self.widget)
        self.udi_button.setObjectName(u"udi_button")
        self.udi_button.setGeometry(QRect(180, 220, 110, 30))
        self.udi_button.setFocusPolicy(Qt.StrongFocus)
        self.udi_button.setStyleSheet(u"QPushButton {\n"
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
        self.page_button = QPushButton(self.widget)
        self.page_button.setObjectName(u"page_button")
        self.page_button.setGeometry(QRect(152, 365, 35, 35))
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
        self.blacklist_button = QPushButton(self.widget)
        self.blacklist_button.setObjectName(u"blacklist_button")
        self.blacklist_button.setGeometry(QRect(50, 290, 240, 30))
        self.blacklist_button.setFocusPolicy(Qt.StrongFocus)
        self.blacklist_button.setStyleSheet(u"QPushButton {\n"
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
        QWidget.setTabOrder(self.dolar_button, self.currency_button)
        QWidget.setTabOrder(self.currency_button, self.inpc_button)
        QWidget.setTabOrder(self.inpc_button, self.udi_button)
        QWidget.setTabOrder(self.udi_button, self.blacklist_button)
        QWidget.setTabOrder(self.blacklist_button, self.page_button)

        self.retranslateUi(Form)

        self.dolar_button.setDefault(True)
        self.inpc_button.setDefault(True)
        self.currency_button.setDefault(True)
        self.udi_button.setDefault(True)
        self.blacklist_button.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.dolar_button.setText(QCoreApplication.translate("Form", u"Tipo de cambio del d\u00f3lar DOF a Excel", None))
#if QT_CONFIG(shortcut)
        self.dolar_button.setShortcut(QCoreApplication.translate("Form", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.inpc_button.setText(QCoreApplication.translate("Form", u"INPC", None))
#if QT_CONFIG(shortcut)
        self.inpc_button.setShortcut(QCoreApplication.translate("Form", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.currency_button.setText(QCoreApplication.translate("Form", u"Tipos de cambio de otras divisas", None))
#if QT_CONFIG(shortcut)
        self.currency_button.setShortcut(QCoreApplication.translate("Form", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.indicadores.setText(QCoreApplication.translate("Form", u"Indicadores fiscales", None))
        self.udi_button.setText(QCoreApplication.translate("Form", u"UDI", None))
#if QT_CONFIG(shortcut)
        self.udi_button.setShortcut(QCoreApplication.translate("Form", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.page_button.setText(QCoreApplication.translate("Form", u"\u2ba8", None))
#if QT_CONFIG(shortcut)
        self.page_button.setShortcut(QCoreApplication.translate("Form", u"Shift+Esc", None))
#endif // QT_CONFIG(shortcut)
        self.blacklist_button.setText(QCoreApplication.translate("Form", u"Listado 69-B del CFF a Excel", None))
#if QT_CONFIG(shortcut)
        self.blacklist_button.setShortcut(QCoreApplication.translate("Form", u"5", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

