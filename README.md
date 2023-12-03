# Pocket-CFDI
Software gratuito de descarga masiva de CFDI y generación de reportes en Excel para contadores 🤓

## Versión compilada en formato exe
https://eraro.mx/

## Uso de otras librerias
from bs4 import BeautifulSoup
from cfdiclient import Autenticacion, DescargaMasiva, Fiel, SolicitaDescarga, VerificaSolicitudDescarga
from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from OpenSSL import crypto
from pathlib import Path
from PySide6 import QtWidgets, QtGui
from PySide6.QtTest import QTest
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
