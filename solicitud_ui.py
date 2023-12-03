# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solicitud.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import solicitud_rc

class Ui_Solicitud(object):
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
        self.rfc.setGeometry(QRect(20, 100, 115, 30))
        self.rfc.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rfc.setText(u"RFC")
        self.rfc.setAlignment(Qt.AlignCenter)
        self.passw = QLabel(self.widget)
        self.passw.setObjectName(u"passw")
        self.passw.setGeometry(QRect(20, 140, 115, 30))
        self.passw.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.passw.setAlignment(Qt.AlignCenter)
        self.rfc_input = QLineEdit(self.widget)
        self.rfc_input.setObjectName(u"rfc_input")
        self.rfc_input.setGeometry(QRect(175, 100, 140, 30))
        self.rfc_input.setFocusPolicy(Qt.NoFocus)
        self.rfc_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(40, 40, 40);\n"
"	border: none;\n"
"	color: rgb(255,255,255);\n"
"}")
        self.rfc_input.setMaxLength(13)
        self.rfc_input.setAlignment(Qt.AlignCenter)
        self.rfc_input.setPlaceholderText(u"RFC")
        self.rfc_input.setClearButtonEnabled(False)
        self.pass_input = QLineEdit(self.widget)
        self.pass_input.setObjectName(u"pass_input")
        self.pass_input.setGeometry(QRect(175, 140, 140, 30))
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
        self.cer_button.setGeometry(QRect(20, 20, 115, 30))
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
        self.cer_input.setGeometry(QRect(175, 20, 140, 30))
        self.cer_input.setFocusPolicy(Qt.NoFocus)
        self.cer_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(40, 40, 40);\n"
"	border: none;\n"
"	color: rgb(255,255,255);\n"
"}")
        self.cer_input.setEchoMode(QLineEdit.Normal)
        self.cer_input.setAlignment(Qt.AlignCenter)
        self.cer_input.setReadOnly(True)
        self.cer_input.setPlaceholderText(u"cer")
        self.key_button = QPushButton(self.widget)
        self.key_button.setObjectName(u"key_button")
        self.key_button.setGeometry(QRect(20, 60, 115, 30))
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
        self.key_input.setGeometry(QRect(175, 60, 140, 30))
        self.key_input.setFocusPolicy(Qt.NoFocus)
        self.key_input.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(40, 40, 40);\n"
"	border: none;\n"
"	color: rgb(255,255,255);\n"
"}")
        self.key_input.setEchoMode(QLineEdit.Normal)
        self.key_input.setAlignment(Qt.AlignCenter)
        self.key_input.setReadOnly(True)
        self.key_input.setPlaceholderText(u"key")
        self.tipo_consulta = QLabel(self.widget)
        self.tipo_consulta.setObjectName(u"tipo_consulta")
        self.tipo_consulta.setGeometry(QRect(20, 220, 115, 30))
        self.tipo_consulta.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tipo_consulta.setAlignment(Qt.AlignCenter)
        self.tipo_consulta_input = QComboBox(self.widget)
        self.tipo_consulta_input.addItem("")
        self.tipo_consulta_input.addItem("")
        self.tipo_consulta_input.setObjectName(u"tipo_consulta_input")
        self.tipo_consulta_input.setGeometry(QRect(175, 220, 140, 30))
        self.tipo_consulta_input.setFocusPolicy(Qt.StrongFocus)
        self.tipo_consulta_input.setStyleSheet(u"QComboBox {\n"
"	outline: none;\n"
"	background-color: rgb(40, 40, 40);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: none;\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/images/arrow.png);\n"
"	width: 8px;\n"
"	height: 8px;\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"QComboBox QListView::item { \n"
"	height: 30px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"	outline: none;\n"
"	background-color: rgb(90, 90, 90);\n"
"}")
        self.tipo_comprobante = QLabel(self.widget)
        self.tipo_comprobante.setObjectName(u"tipo_comprobante")
        self.tipo_comprobante.setGeometry(QRect(20, 260, 115, 30))
        self.tipo_comprobante.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tipo_comprobante.setAlignment(Qt.AlignCenter)
        self.tipo_comprobante_input = QComboBox(self.widget)
        self.tipo_comprobante_input.addItem("")
        self.tipo_comprobante_input.addItem("")
        self.tipo_comprobante_input.addItem("")
        self.tipo_comprobante_input.addItem("")
        self.tipo_comprobante_input.addItem("")
        self.tipo_comprobante_input.addItem("")
        self.tipo_comprobante_input.setObjectName(u"tipo_comprobante_input")
        self.tipo_comprobante_input.setGeometry(QRect(175, 260, 140, 30))
        self.tipo_comprobante_input.setFocusPolicy(Qt.StrongFocus)
        self.tipo_comprobante_input.setStyleSheet(u"QComboBox {\n"
"	outline: none;\n"
"	background-color: rgb(40, 40, 40);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: none;\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/images/arrow.png);\n"
"	width: 8px;\n"
"	height: 8px;\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"QComboBox QListView::item { \n"
"	height: 30px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"	outline: none;\n"
"	background-color: rgb(90, 90, 90);\n"
"}")
        self.request_button = QPushButton(self.widget)
        self.request_button.setObjectName(u"request_button")
        self.request_button.setGeometry(QRect(115, 390, 185, 35))
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
        self.page_button.setGeometry(QRect(40, 390, 35, 35))
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
        self.in_date_input = QDateEdit(self.widget)
        self.in_date_input.setObjectName(u"in_date_input")
        self.in_date_input.setGeometry(QRect(175, 300, 140, 30))
        self.in_date_input.setStyleSheet(u"QDateEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	background-color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView:enabled {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(65, 65, 65);\n"
"	alternate-background-color: rgb(65, 65, 65);\n"
"	selection-background-color: rgb(34, 62, 85);\n"
"	outline: none;\n"
"	font-size: 11px;\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView:disabled {\n"
"	color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"	border: none;\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QDateEdit::drop-down:hover {\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"	image: url(:/images/arrow.png);\n"
"	width: 8px;\n"
"	height: 8px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth, \n"
"#qt_calendar_nextmonth {\n"
"    border: none;  \n"
"	qproperty-icon: none; \n"
"	\n"
"    min-width: 8px;\n"
"    max-width: 8px;\n"
"    min-height: 8px;\n"
"    max-height: 8px;\n"
"\n"
"    background-color: transparent; \n"
"	pa"
                        "dding: 5px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth {\n"
"	margin-left:5px;\n"
"	image: url(:/images/arrow.png);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth {\n"
"	margin-right:5px;\n"
"	image: url(:/images/arrow.png);\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:hover, \n"
"#qt_calendar_nextmonth:hover {\n"
"    background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:pressed, \n"
"#qt_calendar_nextmonth:pressed {\n"
"    background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover {\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover, \n"
"#qt_calendar_monthbutton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(90, 90, 90);\n"
"	border: none;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:pressed, \n"
"#qt_calendar_monthbutton:pressed {\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"#qt_calendar_yearedit {\n"
"    min-width: 55px;\n"
" 	color: rgb(255, 255, 255);\n"
"    background: transparent;\n"
"}\n"
"\n"
"#qt_calendar_yearbu"
                        "tton {\n"
"	width: 70px;\n"
"	font-size: 11px;\n"
"}\n"
"\n"
" #qt_calendar_monthbutton {\n"
"	width: 70px;\n"
"	font-size: 11px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button {\n"
"	subcontrol-position: left\n"
"}\n"
"\n"
"#qt_calendar_yearedit::up-button {\n"
"	subcontrol-position: right\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button, \n"
"#qt_calendar_yearedit::up-button {\n"
"	width:15px;\n"
"	padding: 0px 5px;\n"
"}")
        self.in_date_input.setAlignment(Qt.AlignCenter)
        self.in_date_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.in_date_input.setCalendarPopup(True)
        self.en_date_input = QDateEdit(self.widget)
        self.en_date_input.setObjectName(u"en_date_input")
        self.en_date_input.setGeometry(QRect(175, 340, 140, 30))
        self.en_date_input.setStyleSheet(u"QDateEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	background-color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView:enabled {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(65, 65, 65);\n"
"	alternate-background-color: rgb(65, 65, 65);\n"
"	selection-background-color: rgb(34, 62, 85);\n"
"	outline: none;\n"
"	font-size: 11px;\n"
"}\n"
"\n"
"QDateEdit QAbstractItemView:disabled {\n"
"	color: rgb(205, 205, 205);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"	border: none;\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QDateEdit::drop-down:hover {\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"	image: url(:/images/arrow.png);\n"
"	width: 8px;\n"
"	height: 8px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth, \n"
"#qt_calendar_nextmonth {\n"
"    border: none;  \n"
"	qproperty-icon: none; \n"
"	\n"
"    min-width: 8px;\n"
"    max-width: 8px;\n"
"    min-height: 8px;\n"
"    max-height: 8px;\n"
"\n"
"    background-color: transparent; \n"
"	pa"
                        "dding: 5px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth {\n"
"	margin-left:5px;\n"
"	image: url(:/images/arrow.png);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth {\n"
"	margin-right:5px;\n"
"	image: url(:/images/arrow.png);\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:hover, \n"
"#qt_calendar_nextmonth:hover {\n"
"    background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:pressed, \n"
"#qt_calendar_nextmonth:pressed {\n"
"    background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover {\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover, \n"
"#qt_calendar_monthbutton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(90, 90, 90);\n"
"	border: none;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:pressed, \n"
"#qt_calendar_monthbutton:pressed {\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"#qt_calendar_yearedit {\n"
"    min-width: 55px;\n"
" 	color: rgb(255, 255, 255);\n"
"    background: transparent;\n"
"}\n"
"\n"
"#qt_calendar_yearbu"
                        "tton {\n"
"	width: 70px;\n"
"	font-size: 11px;\n"
"}\n"
"\n"
" #qt_calendar_monthbutton {\n"
"	width: 70px;\n"
"	font-size: 11px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button {\n"
"	subcontrol-position: left\n"
"}\n"
"\n"
"#qt_calendar_yearedit::up-button {\n"
"	subcontrol-position: right\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button, \n"
"#qt_calendar_yearedit::up-button {\n"
"	width:15px;\n"
"	padding: 0px 5px;\n"
"}")
        self.en_date_input.setAlignment(Qt.AlignCenter)
        self.en_date_input.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.en_date_input.setCalendarPopup(True)
        self.in_date = QLabel(self.widget)
        self.in_date.setObjectName(u"in_date")
        self.in_date.setGeometry(QRect(20, 300, 115, 30))
        self.in_date.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.in_date.setAlignment(Qt.AlignCenter)
        self.en_date = QLabel(self.widget)
        self.en_date.setObjectName(u"en_date")
        self.en_date.setGeometry(QRect(20, 340, 115, 30))
        self.en_date.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.en_date.setAlignment(Qt.AlignCenter)
        self.tipo_datos = QLabel(self.widget)
        self.tipo_datos.setObjectName(u"tipo_datos")
        self.tipo_datos.setGeometry(QRect(20, 180, 115, 30))
        self.tipo_datos.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tipo_datos.setAlignment(Qt.AlignCenter)
        self.tipo_datos_input = QComboBox(self.widget)
        self.tipo_datos_input.addItem("")
        self.tipo_datos_input.addItem("")
        self.tipo_datos_input.setObjectName(u"tipo_datos_input")
        self.tipo_datos_input.setGeometry(QRect(175, 180, 140, 30))
        self.tipo_datos_input.setFocusPolicy(Qt.StrongFocus)
        self.tipo_datos_input.setStyleSheet(u"QComboBox {\n"
"	outline: none;\n"
"	background-color: rgb(40, 40, 40);\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	border: none;\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QComboBox::drop-down:hover {\n"
"	background-color: rgb(90, 90, 90);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/images/arrow.png);\n"
"	width: 8px;\n"
"	height: 8px;\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(40, 40, 40);\n"
"}\n"
"\n"
"QComboBox QListView::item { \n"
"	height: 30px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"	outline: none;\n"
"	background-color: rgb(90, 90, 90);\n"
"}")
        QWidget.setTabOrder(self.cer_button, self.key_button)
        QWidget.setTabOrder(self.key_button, self.pass_input)
        QWidget.setTabOrder(self.pass_input, self.tipo_datos_input)
        QWidget.setTabOrder(self.tipo_datos_input, self.tipo_consulta_input)
        QWidget.setTabOrder(self.tipo_consulta_input, self.tipo_comprobante_input)
        QWidget.setTabOrder(self.tipo_comprobante_input, self.in_date_input)
        QWidget.setTabOrder(self.in_date_input, self.en_date_input)
        QWidget.setTabOrder(self.en_date_input, self.request_button)
        QWidget.setTabOrder(self.request_button, self.page_button)

        self.retranslateUi(Form)

        self.cer_button.setDefault(False)
        self.key_button.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.passw.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.pass_input.setPlaceholderText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.cer_button.setText(QCoreApplication.translate("Form", u"Archivo .cer", None))
        self.key_button.setText(QCoreApplication.translate("Form", u"Archivo .key", None))
        self.tipo_consulta.setText(QCoreApplication.translate("Form", u"Tipo de consulta", None))
        self.tipo_consulta_input.setItemText(0, QCoreApplication.translate("Form", u"Emitidos", None))
        self.tipo_consulta_input.setItemText(1, QCoreApplication.translate("Form", u"Recibidos", None))

        self.tipo_comprobante.setText(QCoreApplication.translate("Form", u"Tipo de comprobante", None))
        self.tipo_comprobante_input.setItemText(0, QCoreApplication.translate("Form", u"Todos", None))
        self.tipo_comprobante_input.setItemText(1, QCoreApplication.translate("Form", u"Ingreso", None))
        self.tipo_comprobante_input.setItemText(2, QCoreApplication.translate("Form", u"Egreso", None))
        self.tipo_comprobante_input.setItemText(3, QCoreApplication.translate("Form", u"Pago", None))
        self.tipo_comprobante_input.setItemText(4, QCoreApplication.translate("Form", u"N\u00f3mina", None))
        self.tipo_comprobante_input.setItemText(5, QCoreApplication.translate("Form", u"Traslado", None))

        self.request_button.setText(QCoreApplication.translate("Form", u"Enviar", None))
        self.page_button.setText(QCoreApplication.translate("Form", u"\u2ba8", None))
#if QT_CONFIG(shortcut)
        self.page_button.setShortcut(QCoreApplication.translate("Form", u"Shift+Esc", None))
#endif // QT_CONFIG(shortcut)
        self.in_date_input.setDisplayFormat(QCoreApplication.translate("Form", u"dd/MM/yyyy", None))
        self.en_date_input.setDisplayFormat(QCoreApplication.translate("Form", u"dd/MM/yyyy", None))
        self.in_date.setText(QCoreApplication.translate("Form", u"Fecha inicial", None))
        self.en_date.setText(QCoreApplication.translate("Form", u"Fecha final", None))
        self.tipo_datos.setText(QCoreApplication.translate("Form", u"Tipo de datos", None))
        self.tipo_datos_input.setItemText(0, QCoreApplication.translate("Form", u"CFDI", None))
        self.tipo_datos_input.setItemText(1, QCoreApplication.translate("Form", u"Metadata", None))

    # retranslateUi

