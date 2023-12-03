from bs4 import BeautifulSoup
from cfdiclient import Autenticacion, DescargaMasiva, Fiel, SolicitaDescarga, VerificaSolicitudDescarga
from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from login_ui import Ui_Login
from menu_ui import Ui_Menu
from OpenSSL import crypto
from pathlib import Path
from PySide6 import QtWidgets, QtGui
from PySide6.QtTest import QTest
from solicitud_ui import Ui_Solicitud
from util_ui import Ui_Util
from validar_ui import Ui_Validar
from zipfile import ZipFile
import atexit
import base64
import catalogo
import concurrent.futures
import httpx
import json
import locale
import os
import pandas as pd
import parsing_xml
import sys

locale.setlocale(locale.LC_TIME, "")

pocket_version = "3.2.1"
percentaje = 0
pocket_download = "https://eraro.mx/files/Pocket_CFDI/Pocket%20CFDI.zip"
url_version = "https://eraro.mx/files/Pocket_CFDI/Pocket%20CFDI%20version.txt"
annoucement_website = "https://eraro.mx/files/Pocket_CFDI/Annoucement.txt"
tc_website = "https://www.banxico.org.mx/tipcamb/tipCamIHAction.do"
ex_website = "https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadroAnalitico&idCuadro=CA113&locale=es"
inpc_website = "https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CP154&locale=es"
udi_website = "https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CP150&locale=es"
efo_website = "http://omawww.sat.gob.mx/cifras_sat/Documents/Listado_Completo_69-B.csv"

def tipo_cambio():
    try:
        website = httpx.get(url = tc_website, verify = False)
        soup = BeautifulSoup(website.text, "html.parser")
        exchange_df = pd.read_html(str(soup), skiprows = 1)[1]
        exchange_df[0] = exchange_df[0].str.split(" +")
        exchange_df[1] = exchange_df[1].str.split(" +")
        exchange_df[2] = exchange_df[2].str.split(" +")
        exchange_df[3] = exchange_df[3].str.split(" +")
        exchange_df = exchange_df.explode([0, 1, 2, 3])
        exchange_df[1] = pd.to_numeric(exchange_df[1], errors = "coerce")
        exchange_df[2] = pd.to_numeric(exchange_df[2], errors = "coerce")
        exchange_df[3] = pd.to_numeric(exchange_df[3], errors = "coerce")
        exchange_df[0] = pd.to_datetime(exchange_df[0], dayfirst = True, errors = "ignore").dt.date
        exchange_df.sort_values(by = 0, ascending = False, inplace = True)
        exchange_df.columns = ["Fecha", "Determinación", "Publicación DOF", "Para solventar obligaciones"]
        return exchange_df

    except:
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Sin internet.")
        return pd.DataFrame()

class Login(QtWidgets.QWidget, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.login_button.clicked.connect(self.loginfunction)
    
    def loginfunction(self):

        widget.setCurrentIndex(menu_widget)
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Inicio de sesión.")

class Mainmenu(QtWidgets.QWidget, Ui_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.xml_v_button.clicked.connect(self.xml_to_excel)
        self.stop_button.clicked.connect(self.stop_xml_to_excel)
        self.solicitar_button.clicked.connect(self.solicitud_widget)
        self.validar_button.clicked.connect(self.validar_widget)
        self.file_button.clicked.connect(self.open_delimiter)
        self.return_button.clicked.connect(self.close_delimiter)
        self.util_button.clicked.connect(self.utilerias_widget)
        self.txt_button.clicked.connect(self.file_to_excel)
        self.export_button.clicked.connect(self.delim_to_excel)
        self.progressBar.setVisible(False)
        self.stop_button.setVisible(False)
        self.return_button.setVisible(False)
        self.delimiter_input.setVisible(False)
        self.export_button.setVisible(False)
        self.stop_button.setVisible(False)
        self.loop = False

    global percentaje

    def stop_xml_to_excel(self):
        if self.loop:
            self.loop = False
            self.stop_button.setVisible(False)
            self.progressBar.setVisible(False)
            messagebox.setText("Proceso cancelado.")
            messagebox.exec()

    def solicitud_widget(self):
        widget.setCurrentIndex(request_widget)

    def validar_widget(self):
        widget.setCurrentIndex(validate_widget)

    def open_delimiter(self):
        if self.progressBar.isVisible():
            return
        self.file_button.setVisible(False)
        self.return_button.setVisible(True)
        self.delimiter_input.setVisible(True)
        self.export_button.setVisible(True)

    def close_delimiter(self):
        self.file_button.setVisible(True)
        self.return_button.setVisible(False)
        self.delimiter_input.setVisible(False)
        self.export_button.setVisible(False)

    def utilerias_widget(self):
        if self.progressBar.isVisible():
            return
        widget.setCurrentIndex(util_widget)

    def Update_progress_bar(self, value, lenght):
        global percentaje
        percentaje += value/lenght
        self.progressBar.setValue(int(percentaje))
        QtWidgets.QApplication.processEvents()

    def xml_to_excel(self):
        global percentaje
        if self.progressBar.isVisible():
            return
        percentaje = 0
        self.file_button.setVisible(True)
        self.return_button.setVisible(False)
        self.delimiter_input.setVisible(False)
        self.export_button.setVisible(False)
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, caption = "Abrir")
        if not directory:
            return
        messagebox.setText("¿Desea validar el estatus de vigencia de los CFDI?")
        message = messagebox.setStandardButtons(messagebox.StandardButton.Ok | messagebox.StandardButton.No)
        message = messagebox.exec()
        if message == messagebox.StandardButton.Ok:
            cfdi_status = True
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Se validara la vigencia de los CFDIs")
        else:
            cfdi_status = False
        messagebox.setText("¿Definir los conceptos de nómina conforme a la clave agrupadora?")
        message = messagebox.exec()
        if message == messagebox.StandardButton.Ok:
            catalogo_nomina = True
        else:
            catalogo_nomina = False
        messagebox.setStandardButtons(messagebox.StandardButton.Ok)
        self.progressBar.setValue(0)
        self.progressBar.setVisible(True)
        self.stop_button.setVisible(True)
        self.loop = True
        directory_list = [
            os.path.join(dirpath, filename)
            for dirpath, _, filenames in os.walk(directory)
            for filename in filenames
            if filename.lower().endswith(".xml")
        ]
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso iniciado.")
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            files = [executor.submit(lambda dir: parsing_xml.parsing_xml(dir, cfdi_status, catalogo_nomina), data) for data in directory_list]
            dataframe = []
            for future in concurrent.futures.as_completed(files):
                if not (widget.isVisible() and self.loop):
                    for f in files:
                        f.cancel()
                    print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso cancelado.")
                    return
                dataframe.append(future.result())
                self.Update_progress_bar(100, len(directory_list))
        
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Lectura completada.")

        global_df = [invoice.get("global") for invoice in dataframe if invoice and "global" in invoice]
        concept_df = [invoice.get("concepto") for invoice in dataframe if invoice and "concepto" in invoice]
        payment_df = [invoice.get("pago") for invoice in dataframe if invoice and "pago" in invoice]
        payroll_df = [invoice.get("nomina") for invoice in dataframe if invoice and "nomina" in invoice]
        withhold_df = [invoice.get("retencion") for invoice in dataframe if invoice and "retencion" in invoice]
        error_df = [invoice.get("error") for invoice in dataframe if invoice and "error" in invoice]

        global_df = pd.DataFrame.from_dict(global_df).drop_duplicates(subset=["UUID"])
        concept_df = pd.DataFrame.from_dict(concept_df).drop_duplicates(subset=["UUID"])
        payment_df = pd.DataFrame.from_dict(payment_df).drop_duplicates(subset=["UUID"])
        payroll_df = pd.DataFrame.from_dict(payroll_df).drop_duplicates(subset=["UUID"])
        withhold_df = pd.DataFrame.from_dict(withhold_df).drop_duplicates(subset=["UUID"])
        error_df = pd.DataFrame.from_dict(error_df)
        
        if global_df.empty and concept_df.empty and payment_df.empty and payroll_df.empty and withhold_df.empty:
            messagebox.setText("No se encontró ningun CFDI.")
            messagebox.exec()
            self.stop_button.setVisible(False)
            self.progressBar.setVisible(False)
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "No se encontró ningun CFDI.")
            return

        exchange_df = tipo_cambio()
        
        if not global_df.empty:
            global_df[catalogo.global_numeric] = global_df[catalogo.global_numeric].apply(pd.to_numeric, errors = "ignore")
            global_df[catalogo.global_negative] *= -1
            global_df["Fecha"] = pd.to_datetime(global_df["Fecha"], errors = "ignore")
            global_df.loc[((global_df["Tipo"] == "E") | (global_df["Tipo"] == "egreso")),
                          catalogo.global_numeric[1:]] *= -1
            global_df.sort_values(by = "Fecha", inplace = True)
        
        if not concept_df.empty:
            concept_df = concept_df.explode(catalogo.concept_explode)
            concept_df[catalogo.concept_numeric] = concept_df[catalogo.concept_numeric].apply(pd.to_numeric, errors = "ignore")
            concept_df["Fecha"] = pd.to_datetime(concept_df["Fecha"], errors = "ignore")
            concept_df[catalogo.concept_negative] *= -1
            concept_df.loc[((concept_df["Tipo"] == "E") | (concept_df["Tipo"] == "egreso")),
                           catalogo.concept_numeric] *= -1
            concept_df.sort_values(by = ["Fecha", "UUID"], inplace = True)

        if not payment_df.empty:
            payment_df = payment_df.explode(catalogo.payment_explode)
            payment_df.loc[payment_df["UUID"].duplicated(), list(payment_df.columns)[15:27]] = None
            payment_df[catalogo.payment_numeric] = payment_df[catalogo.payment_numeric].apply(pd.to_numeric, errors = "ignore")
            payment_df[catalogo.payment_date] = payment_df[catalogo.payment_date].apply(pd.to_datetime, errors = "ignore")
            payment_df.sort_values(by = ["Fecha", "UUID"], inplace = True)

        if not payroll_df.empty:
            columns_to_update = list(payroll_df.columns)[40:]
            for col in columns_to_update:
                payroll_df[col] = payroll_df[col].apply(lambda x: [x] if (not isinstance(x, list) and x is not None) else (x if isinstance(x, list) else []))
            payroll_df = payroll_df.apply(lambda row: parsing_xml.equalize_dataframe(row, columns_to_update), axis = 1)
            payroll_df = payroll_df.explode([*catalogo.payroll_explode,*list(payroll_df.columns)[40:]])
            payroll_df.loc[payroll_df["UUID"].duplicated(), "Total"] = None
            payroll_df[catalogo.payroll_numeric] = payroll_df[catalogo.payroll_numeric].apply(pd.to_numeric, errors = "ignore")
            payroll_df[catalogo.payroll_date] = payroll_df[catalogo.payroll_date].apply(pd.to_datetime, errors = "ignore")
            payroll_df["Total de deducciones"] *= -1
            payroll_df.sort_values(by = ["Fecha", "UUID"], inplace = True)

        if not withhold_df.empty:
            withhold_df[list(withhold_df.columns)[18:]] = withhold_df[list(withhold_df.columns)[18:]].apply(pd.to_numeric, errors = "ignore")
            withhold_df["Fecha"] = pd.to_datetime(withhold_df["Fecha"], format = "mixed", errors = "ignore", utc = True).apply(lambda x: x.replace(tzinfo = None))
            withhold_df.sort_values(by = ["Fecha"], inplace = True)

        save_file = QtWidgets.QFileDialog.getSaveFileName(self, caption = "Guardar como", directory = os.path.join(directory, datetime.now().strftime("%Y %b %d, %I_%M_%S %p")+" XML_a_Excel"), filter = "Libro de Excel (*.xlsx)")[0]
        if save_file == "":
            self.stop_button.setVisible(False)
            self.progressBar.setVisible(False)
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso cancelado.")
            return
        
        xlwriter = pd.ExcelWriter(save_file, engine = "xlsxwriter")
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Reporte tipo cambio sin datos.") if exchange_df.empty else exchange_df.to_excel(xlwriter, sheet_name = "Tipo cambio", index = False, startrow = 1, startcol = 1, freeze_panes = (2, 0))
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Reporte global sin datos.") if global_df.empty else global_df.to_excel(xlwriter, sheet_name = "Global", index = False, startrow = 1, startcol = 1, freeze_panes = (2, 0))
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Reporte concepto sin datos.") if concept_df.empty else concept_df.to_excel(xlwriter, sheet_name = "Concepto", index = False, startrow = 1, startcol = 1, freeze_panes = (2, 0))
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Reporte pagos sin datos.") if payment_df.empty else payment_df.to_excel(xlwriter, sheet_name = "Pago", index = False, startrow = 1, startcol = 1, freeze_panes = (2, 0))
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Reporte nómina sin datos.") if payroll_df.empty else payroll_df.to_excel(xlwriter, sheet_name = "Nómina", index = False, startrow = 1, startcol = 1, freeze_panes = (2, 0))
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Reporte retenciones sin datos.") if withhold_df.empty else withhold_df.to_excel(xlwriter, sheet_name = "Retención", index = False, startrow = 1, startcol = 1, freeze_panes = (2, 0))
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Reporte error sin datos.") if error_df.empty else error_df.to_excel(xlwriter, sheet_name = "Error", index = False, startrow = 1, startcol = 1, freeze_panes = (2, 0))
        xlwriter.book.set_properties({"author": "Pocket CFDI"})
        workbook = xlwriter.book
        hformat = workbook.add_format({
                "border": 1,
                "valign": "vcenter",
                "align": "center",
                "font_color": "#ffffff",
                "bg_color": "#1F497D"
                })
        if not exchange_df.empty:
            for col_num, value in enumerate(exchange_df.columns.values):
                xlwriter.sheets["Tipo cambio"].write(1, col_num + 1, value, hformat)
        if not global_df.empty:
            for col_num, value in enumerate(global_df.columns.values):
                xlwriter.sheets["Global"].write(1, col_num + 1, value, hformat)
        if not concept_df.empty:
            for col_num, value in enumerate(concept_df.columns.values):
                xlwriter.sheets["Concepto"].write(1, col_num + 1, value, hformat)
        if not payment_df.empty:
            for col_num, value in enumerate(payment_df.columns.values):
                xlwriter.sheets["Pago"].write(1, col_num + 1, value, hformat)
        if not payroll_df.empty:
            for col_num, value in enumerate(payroll_df.columns.values):
                xlwriter.sheets["Nómina"].write(1, col_num + 1, value, hformat)
        if not withhold_df.empty:
            for col_num, value in enumerate(withhold_df.columns.values):
                xlwriter.sheets["Retención"].write(1, col_num + 1, value, hformat)
        if not error_df.empty:
            for col_num, value in enumerate(error_df.columns.values):
                xlwriter.sheets["Error"].write(1, col_num + 1, value, hformat)

        xlwriter.close()
        
        messagebox.setText(
f"""Proceso finalizado.
    Duplicados: {len(directory_list)-len(global_df)-len(withhold_df)-len(error_df):,}
    Errores: {len(error_df):,}
    Correctos: {len(global_df)+len(withhold_df):,}
    Total: {len(directory_list):,}
¿Desea abrir el documento?""")
        
        message = messagebox.setStandardButtons(messagebox.StandardButton.Ok | messagebox.StandardButton.No)
        message = messagebox.exec()
        if message == messagebox.StandardButton.Ok:
            os.startfile(save_file)
        messagebox.setStandardButtons(messagebox.StandardButton.Ok)
        self.stop_button.setVisible(False)
        self.progressBar.setVisible(False)
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso finalizado.")

    def file_to_excel(self):
        if self.progressBar.isVisible():
            return
        self.file_button.setVisible(True)
        self.return_button.setVisible(False)
        self.delimiter_input.setVisible(False)
        self.export_button.setVisible(False)
        directory = QtWidgets.QFileDialog.getOpenFileNames(self, caption = "Abrir", filter = "Todos los archivos (*)")[0]
        if not directory:
            return
        save_as = QtWidgets.QFileDialog.getSaveFileName(self, caption = "Guardar como", directory = os.path.join(Path(directory[0]).parent, datetime.now().strftime("%Y %b %d, %I_%M_%S %p")) + " Archivo_a_Excel", filter = "Libro de Excel (*.xlsx)")[0]
        if save_as == "":
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso cancelado.")
            return
        xlwriter = pd.ExcelWriter(save_as, engine = "xlsxwriter")
        for file in directory:
            if file.lower().endswith(".asc"):
                try:
                    pd.read_table(file, sep = "[|]", encoding = "latin-1", index_col = False, engine = "python").to_excel(xlwriter, sheet_name = catalogo.c_glosa.get(os.path.basename(file)[-7:], Path(file).stem)[:31], index = False, startrow = 1, startcol = 1, freeze_panes = (2, 0))
                except:
                    pass
            else:
                try:
                    pd.read_table(file, sep = "[~]", encoding = "latin-1", index_col = False, engine = "python").to_excel(xlwriter, sheet_name = Path(file).stem[:31], index = False, startrow = 1, startcol = 1, freeze_panes = (2, 0))
                except:
                    pass
        xlwriter.book.set_properties({"author": "Pocket CFDI"})
        xlwriter.close()
        messagebox.setText("Proceso finalizado.\n¿Desea abrir el documento?")
        message = messagebox.setStandardButtons(messagebox.StandardButton.Ok | messagebox.StandardButton.No)
        message = messagebox.exec()
        if message == messagebox.StandardButton.Ok:
            os.startfile(save_as)
        messagebox.setStandardButtons(messagebox.StandardButton.Ok)
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso finalizado.")

    def delim_to_excel(self):
        if self.progressBar.isVisible():
            return
        if self.delimiter_input.text() == "":
            messagebox.setText("Debes introducir un delimitador.")
            messagebox.exec()
            return
        directory = QtWidgets.QFileDialog.getOpenFileNames(self, caption = "Abrir", filter = "Todos los archivos (*)")[0]
        if not directory:
            return
        save_as = QtWidgets.QFileDialog.getSaveFileName(self, caption = "Guardar como", directory = os.path.join(Path(directory[0]).parent, datetime.now().strftime("%Y %b %d, %I_%M_%S %p")) + " Archivo_a_Excel", filter = "Libro de Excel (*.xlsx)")[0]
        if save_as == "":
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso cancelado.")
            self.file_button.setVisible(True)
            self.return_button.setVisible(False)
            self.delimiter_input.setVisible(False)
            self.export_button.setVisible(False)
            return
        xlwriter = pd.ExcelWriter(save_as, engine = "xlsxwriter")
        for file in directory:
            try:
                pd.read_table(file, sep = self.delimiter_input.text(), encoding = "latin-1", index_col = False, engine = "python").to_excel(xlwriter, sheet_name = Path(file).stem[:31], index = False, startrow = 1, startcol = 1, freeze_panes = (2, 0))
            except:
                pass
        xlwriter.book.set_properties({"author": "Pocket CFDI"})
        xlwriter.close()
        messagebox.setText("Proceso finalizado.\n¿Desea abrir el documento?")
        msg = messagebox.setStandardButtons(messagebox.StandardButton.Ok | messagebox.StandardButton.No)
        msg = messagebox.exec()
        if msg == messagebox.StandardButton.Ok:
            os.startfile(save_as)
        messagebox.setStandardButtons(messagebox.StandardButton.Ok)
        self.file_button.setVisible(True)
        self.return_button.setVisible(False)
        self.delimiter_input.setVisible(False)
        self.export_button.setVisible(False)
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso finalizado.")

class Solicitud(QtWidgets.QWidget, Ui_Solicitud):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cer_button.clicked.connect(self.cer_directory)
        self.key_button.clicked.connect(self.key_directory)
        self.page_button.clicked.connect(self.return_to_menu)
        self.pass_input.returnPressed.connect(self.request)
        self.request_button.clicked.connect(self.request)
        self.in_date_input.setDate(datetime.now() - relativedelta(day = 1, months = 1))
        self.in_date_input.setMaximumDate(datetime.now())
        self.in_date_input.setMinimumDate(datetime(2018, 1, 1))
        self.en_date_input.setDate(datetime.now())
        self.en_date_input.setMaximumDate(datetime.now())
        self.en_date_input.setMinimumDate(datetime(2018, 1, 1))

    def return_to_menu(self):
        widget.setCurrentIndex(menu_widget)

    def cer_directory(self):
        cer_dir = QtWidgets.QFileDialog.getOpenFileName(self, caption = "Abrir", filter = "Archivo CER (*.cer)")[0]
        self.cer_input.setText(cer_dir)
        if cer_dir:
            self.rfc_input.setText(dict(crypto.load_certificate(crypto.FILETYPE_ASN1, open(cer_dir, "rb").read()).get_subject().get_components()).get(b"x500UniqueIdentifier").decode().split(" / ")[0].upper())

    def key_directory(self):
        key_dir = QtWidgets.QFileDialog.getOpenFileName(self, caption = "Abrir", filter = "Archivo KEY (*.key);; Todos los archivos (*)")[0]
        self.key_input.setText(key_dir)

    def request(self):
        if self.in_date_input.date().toPyDate() > self.en_date_input.date().toPyDate():
            messagebox.setText("La fecha inicial no puede ser mayor a la fecha final.")
            messagebox.exec()
            return

        rfc = self.rfc_input.text()
        e_firma = self.pass_input.text()
        cer = self.cer_input.text()
        key = self.key_input.text()
        tipo_datos = self.tipo_datos_input.currentText()
        tipo_consulta = self.tipo_consulta_input.currentText()
        tipo_cfdi = self.tipo_comprobante_input.currentText()
        in_date = self.in_date_input.date().toPyDate()
        en_date = self.en_date_input.date().toPyDate()
        in_date = datetime.combine(in_date, time.min)
        en_date = datetime.combine(en_date, time.max)
        txt_directory = os.path.join(os.getcwd(), "Solicitudes Pocket CFDI")
        txt_save_as = os.path.join(txt_directory, str(int(datetime.now().strftime("%y%m%#d"))) + " " + tipo_consulta[0] + " " + tipo_datos[0] + " " + tipo_cfdi[:2] + " " + rfc[6:] + " " + in_date.strftime("%#d %b %y") + " - " + en_date.strftime("%#d %b %y") + ".txt")
        
        if os.path.isfile(txt_save_as):
            messagebox.setText("Ya existe una solicitud con los mismos parámetros,\n¿Desea reemplazarla?")
            message = messagebox.setStandardButtons(messagebox.StandardButton.Ok | messagebox.StandardButton.No)
            message = messagebox.exec()
            if message == messagebox.StandardButton.Ok:
                self.request1(rfc, e_firma, cer, key, tipo_datos, tipo_consulta, tipo_cfdi, in_date, en_date, txt_directory, txt_save_as)
            else:
                messagebox.setStandardButtons(messagebox.StandardButton.Ok)
                print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso cancelado.")
        else:
            self.request1(rfc, e_firma, cer, key, tipo_datos, tipo_consulta, tipo_cfdi, in_date, en_date, txt_directory, txt_save_as)

    def request1(self, rfc, e_firma, cer, key, tipo_datos, tipo_consulta, tipo_cfdi, in_date, en_date, txt_directory, txt_save_as):
        if tipo_cfdi != "Todos":
            tipo_cfdi = tipo_cfdi[0]
        else:
            tipo_cfdi = None
        try:
            cer_der = open(cer, "rb").read()
            key_der = open(key, "rb").read()
            fiel = Fiel(cer_der, key_der , e_firma)
            auth = Autenticacion(fiel)
            token = auth.obtener_token()
            descarga = SolicitaDescarga(fiel)
        except:
            import traceback
            traceback.print_exc()
            messagebox.setText("Los datos de acceso son incorrectos.")
            messagebox.exec()
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Los datos de acceso son incorrectos.")
            return
        if tipo_consulta == "Emitidos":
            solicitud = descarga.solicitar_descarga(token, rfc, in_date, en_date, rfc_emisor = rfc, tipo_solicitud = tipo_datos, tipo_comprobante = tipo_cfdi)
        elif tipo_consulta == "Recibidos":
            solicitud = descarga.solicitar_descarga(token, rfc, in_date, en_date, rfc_receptor = rfc, tipo_solicitud = tipo_datos, tipo_comprobante = tipo_cfdi)
        else:
            messagebox.setText("Error en los datos ingresados.")
            messagebox.exec()
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Error en los datos ingresados.")
            return
        if solicitud["id_solicitud"] == None:
            messagebox.setText("Error al realizar la solicitud.")
            messagebox.exec()
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Error al realizar la solicitud.")
            return
        request_dict = {"id_solicitud":solicitud["id_solicitud"], "Fecha_inicial": in_date, "Fecha_final": en_date, "Tipo_de_datos": tipo_datos, "Tipo_de_consulta": tipo_consulta, "Tipo_de_comprobante": tipo_cfdi}
        if not os.path.exists(txt_directory):
            os.mkdir(txt_directory)
            print(datetime.now().strftime("%d %b %Y, %I:%M:%S %p"), "Directorio creado.")
        else:
            print(datetime.now().strftime("%d %b %Y, %I:%M:%S %p"), "Ya existe el directorio.")
        json.dump(request_dict, open(txt_save_as, "w"), default = str)
        messagebox.setText("La solicitud se ha guardado, podrá validar el estatus en cualquier\nmomento, aunque la rapidez para obtener la descarga dependerá\ndel servicio web del SAT.")
        messagebox.setStandardButtons(messagebox.StandardButton.Ok)
        messagebox.exec()
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Solicitud enviada.")

class Validar(QtWidgets.QWidget, Ui_Validar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cer_button.clicked.connect(self.cer_directory)
        self.key_button.clicked.connect(self.key_directory)
        self.refresh_button.clicked.connect(self.refresh)
        self.delete_button.clicked.connect(self.delete_request)
        self.page_button.clicked.connect(self.return_to_menu)
        self.pass_input.returnPressed.connect(lambda: self.valitade_request(False))
        self.request_button.clicked.connect(lambda: self.valitade_request(False))
        self.requestloop_button.clicked.connect(lambda: self.valitade_request(True))
        self.stop_button.clicked.connect(self.stop)
        self.stop_button.setVisible(False)
        self.loop = False

    def close_loop(self):
        self.pass_input.setEnabled(True)
        self.listWidget.setEnabled(True)
        self.stop_button.setVisible(False)
        self.requestloop_button.setVisible(True)

    def return_to_menu(self):
        widget.setCurrentIndex(menu_widget)

    def refresh(self):
        
        if self.loop:
            return

        try:
            self.listWidget.clear()
            request_list = os.listdir(os.path.join(os.getcwd(), "Solicitudes Pocket CFDI"))
            request_list = [x.strip(".txt") for x in [x for x in request_list if self.rfc_input.text()[6:] in x]]
            request_list.sort(reverse = True)
            self.listWidget.addItems(request_list)
            self.listWidget.setCurrentRow(0)
        
        except:
            pass

    def cer_directory(self):
        
        if self.loop:
            return
        
        cer_dir = QtWidgets.QFileDialog.getOpenFileName(self, caption = "Abrir", filter = "Archivo CER (*.cer)")[0]
        self.cer_input.setText(cer_dir)
        
        if cer_dir:
            self.rfc_input.setText(dict(crypto.load_certificate(crypto.FILETYPE_ASN1, open(cer_dir, "rb").read()).get_subject().get_components()).get(b"x500UniqueIdentifier").decode().split(" / ")[0].upper())
            self.listWidget.clear()
            
            try:
                request_list = os.listdir(os.path.join(os.getcwd(), "Solicitudes Pocket CFDI"))
                request_list = [x.strip(".txt") for x in [x for x in request_list if self.rfc_input.text()[6:] in x]]
                request_list.sort(reverse = True)
                self.listWidget.addItems(request_list)
                self.listWidget.setCurrentRow(0)
            
            except:
                pass
        
        else:
            self.rfc_input.setText("")
            self.listWidget.clear()

    def key_directory(self):
        
        if self.loop:
            return
        
        key_dir = QtWidgets.QFileDialog.getOpenFileName(self, caption = "Abrir", filter = "Archivo KEY (*.key);; Todos los archivos (*)")[0]
        self.key_input.setText(key_dir)

    def stop(self):
        
        if self.loop:
            self.loop = False
            self.status.setText("Selecciona la solicitud")
            self.close_loop()
            messagebox.setText("Validación detenida.")
            messagebox.exec()
            
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Validación detenida.")

    def delete_request(self):
        
        if self.loop:
            return
        
        if self.listWidget.currentItem() is not None:
            request = self.listWidget.currentItem().text()
            messagebox.setText(f"¿Estás seguro de eliminar la solicitud: {request}?")
            msg = messagebox.setStandardButtons(messagebox.StandardButton.Ok | messagebox.StandardButton.No)
            msg = messagebox.exec()
            
            if msg == messagebox.StandardButton.Ok:
                
                try:
                    os.remove(os.path.join(os.getcwd(), "Solicitudes Pocket CFDI", request + ".txt"))
                    print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), f"La solicitud {request} se ha eliminado.") 
                except:
                    pass
                
                self.listWidget.takeItem(self.listWidget.currentRow())
            
            messagebox.setStandardButtons(messagebox.StandardButton.Ok)

    def valitade_request(self, activate_loop):
        
        if self.loop == True:
                    return

        rfc = self.rfc_input.text()
        e_firma = self.pass_input.text()
        cer = self.cer_input.text()
        key = self.key_input.text()
        txt = "" if self.listWidget.currentItem() is None else self.listWidget.currentItem().text() + ".txt"

        try:
            cer_der = open(cer, "rb").read()
            key_der = open(key, "rb").read()
            up_dict = dict(json.loads(open(os.path.join(os.getcwd(), "Solicitudes Pocket CFDI", txt), "r").read()))
            fiel = Fiel(cer_der, key_der, e_firma)
            v_descarga = VerificaSolicitudDescarga(fiel)
            auth = Autenticacion(fiel)
        
        except:
            messagebox.setText("Los datos de acceso son incorrectos.")
            messagebox.exec()
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Los datos de acceso son incorrectos.")
            return
        
        if activate_loop:
            self.loop = True
            self.pass_input.setEnabled(False)
            self.listWidget.setEnabled(False)
            self.requestloop_button.setVisible(False)
            self.stop_button.setVisible(True)
            messagebox.setText("Se validará la solicitud cada 30 segundos, por tiempo indefinido.")
            messagebox.exec()
            
        
        while True:
            
            if not widget.isVisible():
                break
            
            try:
                token = auth.obtener_token()
                verificacion = v_descarga.verificar_descarga(token, rfc, up_dict.get("id_solicitud"))
            
            except:
                self.loop = False
                messagebox.setText("Error al subir la información contenida en el txt.")
                messagebox.exec()
                print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Error al subir la información contenida en el txt.")
                break
            
            status_error = f"""La Solicitud fue rechazada.
    Estado de la solicitud: {catalogo.d_solicitud.get(verificacion["estado_solicitud"])}
    Código de estatus: {catalogo.d_estatus.get(verificacion["cod_estatus"])}
    Código de estado de solicitud: {catalogo.d_estado.get(verificacion["codigo_estado_solicitud"])}"""
            
            status_process = f"""La solicitud sigue en proceso.
    Estado de la solicitud: {catalogo.d_solicitud.get(verificacion["estado_solicitud"])}
    Código de estatus: {catalogo.d_estatus.get(verificacion["cod_estatus"])}
    Código de estado de solicitud: {catalogo.d_estado.get(verificacion["codigo_estado_solicitud"])}
    Mensaje: {verificacion["mensaje"]}"""

            status_succes = f"""Proceso finalizado con éxito.
    Número de CFDI: {int(verificacion["numero_cfdis"]):,}"""
            
            status_download = f"""La descarga esta disponible.
    Número de CFDI: {int(verificacion["numero_cfdis"]):,}
    Número de paquetes: {len(verificacion["paquetes"]):,}
¿Desea realizar la descarga?"""

            status_request = int(verificacion["estado_solicitud"])

            if status_request <=2 and status_request > 0:
                print(verificacion)
                print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Solicitud en proceso.")
                
                if not self.loop:
                    self.close_loop()
                    self.status.setText("Selecciona la solicitud")
                    messagebox.setText(status_process)
                    messagebox.exec()
                    break
                
                self.status.setText(
                    f"Solicitud: {catalogo.d_solicitud.get(verificacion['estado_solicitud'])}"
                    )
                QTest.qWait(30000)
                continue
            
            elif status_request >=4 or status_request == 0:
                self.loop = False
                self.close_loop()
                self.status.setText("Selecciona la solicitud")
                messagebox.setText(status_error)
                messagebox.setStandardButtons(messagebox.StandardButton.Ok)
                messagebox.exec()
                print(verificacion)
                print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Solicitud rechazada.")
                break
            
            else:
                messagebox.setText(status_download)
                message = messagebox.setStandardButtons(messagebox.StandardButton.Ok | messagebox.StandardButton.No)
                message = messagebox.exec()
                
                if message == messagebox.StandardButton.Ok:
                    self.status.setText("Descargando...")
                    messagebox.setStandardButtons(messagebox.StandardButton.Ok)
                    save_as = QtWidgets.QFileDialog.getExistingDirectory(self, caption = "Guardar en")
                    
                    if save_as == "":
                        self.loop = False
                        self.close_loop()
                        self.status.setText("Selecciona la solicitud")
                        messagebox.setText("No se ha seleccionado un directorio.")
                        messagebox.exec()
                        break
                    
                    try:
                        
                        for paquete in verificacion["paquetes"]:
                            descarga = DescargaMasiva(fiel)
                            descarga = descarga.descargar_paquete(token, rfc, paquete)
                            exfile = os.path.join(save_as, paquete)
                            with open(exfile + ".zip", "wb") as fp:
                                fp.write(base64.b64decode(descarga["paquete_b64"]))
                    
                    except:
                        self.loop = False
                        self.close_loop()
                        self.status.setText("Selecciona la solicitud")
                        messagebox.setText("La descarga no se completó con éxito. Asegúrate de que\ntu conexión a internet esté activa. Este problema puede\npresentarse si la solicitud ya ha sido descargada\nanteriormente o si el servicio web del SAT no está\noperando correctamente.")
                        messagebox.exec()
                        print(verificacion)
                        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "No se pudo realizar la descarga.")
                        break
                    
                    try:
                        self.status.setText("Descomprimiendo...")
                        
                        for paquete in verificacion["paquetes"]:
                            exfile = os.path.join(save_as, paquete)
                            with ZipFile(exfile + ".zip", "r") as zipex:
                                zipex.extractall(path = os.path.join(save_as, txt.rsplit(".", 1)[0]))
                            os.remove(exfile + ".zip")
                    
                    except:
                        self.loop = False
                        self.close_loop()
                        self.status.setText("Selecciona la solicitud")
                        messagebox.setText("Error al descomprimir.")
                        messagebox.exec()
                        print(verificacion)
                        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "No se pudo realizar la descarga.")
                        break
                    
                    self.loop = False
                    self.close_loop()
                    self.status.setText("Selecciona la solicitud")
                    messagebox.setText(status_succes)
                    messagebox.exec()
                    print(verificacion)
                    print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Descarga exitosa.")
                    break
                
                else:
                    self.loop = False
                    self.close_loop()
                    self.status.setText("Selecciona la solicitud")
                    messagebox.setStandardButtons(messagebox.StandardButton.Ok)
                    print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Solicitud cancelada.")
                    break

class Util(QtWidgets.QWidget, Ui_Util):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dolar_button.clicked.connect(self.tipo_cambio)
        self.currency_button.clicked.connect(self.otras_divisas)
        self.inpc_button.clicked.connect(self.inpc)
        self.udi_button.clicked.connect(self.udi)
        self.page_button.clicked.connect(self.return_to_menu)
        self.blacklist_button.clicked.connect(self.blacklist)

    def return_to_menu(self):
        widget.setCurrentIndex(menu_widget)

    def tipo_cambio(self):
        
        try:
            
            exchange_df = tipo_cambio()
            
            if exchange_df.empty:
                messagebox.setText("Error de conexión.")
                messagebox.exec()
                return
            
            save_as = QtWidgets.QFileDialog.getSaveFileName(self, caption = "Guardar como", directory = datetime.now().strftime("%Y %b %d") + " Tipo de cambio", filter = "Libro de Excel (*.xlsx)")[0]
            if save_as == "":
                print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso cancelado.")
                return
            
            xlwriter = pd.ExcelWriter(save_as, engine = "xlsxwriter")
            exchange_df.to_excel(xlwriter, sheet_name = "Tipo cambio", index = False, startrow = 1, startcol = 1, freeze_panes = (2, 0))
            xlwriter.book.set_properties({"author": "Pocket CFDI"})
            workbook = xlwriter.book
            hformat = workbook.add_format({
                    "border": 1,
                    "valign": "vcenter",
                    "align": "center",
                    "font_color": "#ffffff",
                    "bg_color": "#1F497D"
                    })
            for col_num, value in enumerate(exchange_df.columns.values):
                xlwriter.sheets["Tipo cambio"].write(1, col_num + 1, value, hformat)
            xlwriter.close()
            messagebox.setText("Proceso finalizado.\n¿Desea abrir el documento?")
            message = messagebox.setStandardButtons(messagebox.StandardButton.Ok | messagebox.StandardButton.No)
            message = messagebox.exec()
            
            if message == messagebox.StandardButton.Ok:
                os.startfile(save_as)
            messagebox.setStandardButtons(messagebox.StandardButton.Ok)
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso finalizado.")
        
        except:
            messagebox.setText("Error de conexión.")
            messagebox.exec()
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Error de conexión.")

    def blacklist(self):
        
        try:
            df_69B = pd.read_csv(efo_website, encoding = "latin-1", index_col = False, engine = "python", skiprows = 2)
            save_as = QtWidgets.QFileDialog.getSaveFileName(self, caption = "Guardar como", directory = datetime.now().strftime("%Y %b %d") + " Listado 69B del CFF", filter = "Libro de Excel (*.xlsx)")[0]
            
            if save_as == "":
                print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso cancelado.")
                return
            
            xlwriter = pd.ExcelWriter(save_as, engine = "xlsxwriter")
            df_69B.to_excel(xlwriter, sheet_name = "69B", index = False, startrow = 1, startcol = 1, freeze_panes = (2, 0))
            xlwriter.book.set_properties({"author": "Pocket CFDI"})
            workbook = xlwriter.book
            hformat = workbook.add_format({
                    "border": 1,
                    "valign": "vcenter",
                    "align": "center",
                    "font_color": "#ffffff",
                    "bg_color": "#1F497D"
                    })
            for col_num, value in enumerate(df_69B.columns.values):
                xlwriter.sheets["69B"].write(1, col_num + 1, value, hformat)
            xlwriter.close()
            messagebox.setText("Proceso finalizado.\n¿Desea abrir el documento?")
            message = messagebox.setStandardButtons(messagebox.StandardButton.Ok | messagebox.StandardButton.No)
            message = messagebox.exec()
            
            if message == messagebox.StandardButton.Ok:
                os.startfile(save_as)
            messagebox.setStandardButtons(messagebox.StandardButton.Ok)
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Proceso finalizado.")
        
        except:
            messagebox.setText("Error de conexión.")
            messagebox.exec()
            print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Error de conexión.")
    
    def otras_divisas(self):
        os.startfile(ex_website)

    def inpc(self):
        os.startfile(inpc_website)
    
    def udi(self):
        os.startfile(udi_website)

def exitf():
    print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Sesión terminada.")

if __name__ == '__main__':
    
    atexit.register(exitf)

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    messagebox = QtWidgets.QMessageBox()
    messagebox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
    messagebox.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "Pocket.ico")))
    messagebox.setContentsMargins(0, 0, 18, 0)
    messagebox.setStyleSheet("font-size: 11px;")
    messagebox.button(messagebox.StandardButton.Ok).setText("Aceptar")

    try:
        latest_version = httpx.get(url_version).text
    except:
        latest_version = pocket_version
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Error de conexión al validar la versión.")
    if latest_version.strip() > pocket_version.strip():
        message = messagebox.setWindowTitle("Actualización")
        message = messagebox.setText(f"Actualización disponible a la versión {latest_version}")
        message = messagebox.setStandardButtons(messagebox.StandardButton.Ok | messagebox.StandardButton.No)
        messagebox.button(messagebox.StandardButton.Ok).setText("Actualizar")
        messagebox.button(messagebox.StandardButton.No).setText("Cancelar")
        message = messagebox.exec()
        if message == messagebox.StandardButton.Ok:
            messagebox.setStandardButtons(messagebox.StandardButton.Ok)
            try:
                pocket = httpx.get(pocket_download).content
            except:
                pocket = False
                messagebox.setWindowTitle("Error de conexión")
                messagebox.setText("Ocurrió un error al realizar la descarga.")
                messagebox.exec()
                print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Error al realizar la descarga.")
                sys.exit()
            if pocket:
                Pocket_CFDI = f"Pocket CFDI {latest_version}.exe"
                with open(os.path.join(os.getcwd(), Pocket_CFDI), "wb") as fp:
                    fp.write(pocket)
                messagebox.setWindowTitle("Actualización")
                messagebox.setText(f"La versión {latest_version} ha sido descargada exitosamente\ny se abrirá a continuación.")
                messagebox.exec()
                print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), f"La versión {latest_version} se ha descargado.")
                os.startfile(Pocket_CFDI)
                sys.exit()
        else:
            sys.exit()
    else:
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "No hay actualizaciones.")

    try:
        annoucement = httpx.get(annoucement_website).text
    except:
        annoucement = None
        print(datetime.now().strftime("%Y %b %d, %I:%M:%S %p"), "Sin annoucement.")
    if annoucement:
        messagebox.setWindowTitle("Notifcación")
        messagebox.setText(annoucement)
        messagebox.exec()

    messagebox.setWindowTitle("Estatus")

    login_widget = widget.addWidget(Login())
    menu_widget = widget.addWidget(Mainmenu())
    request_widget = widget.addWidget(Solicitud())
    validate_widget = widget.addWidget(Validar())
    util_widget = widget.addWidget(Util())

    widget.setCurrentIndex(login_widget)
    widget.setFixedSize(340, 450)
    widget.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "Pocket.ico")))
    widget.setWindowTitle(f"Pocket CFDI. Versión {pocket_version}")
    widget.show()

    app.exec()