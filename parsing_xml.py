from lxml import etree
import catalogo
from zeep import Client, helpers
from pathlib import Path
import traceback

def equalize_dataframe(row, columns):
    max_len = max(len(row[col]) for col in columns)
    
    for col in columns:
        diff_len = max_len - len(row[col])
        row[col] = row[col] + [None] * diff_len
    
    return row

def flatten_dict(dict_list):
    result = {}

    all_keys = set().union(*dict_list)

    for d in dict_list:
        for key in all_keys:
            value = d.get(key, None)
            if key in result:
                result[key].append(value)
            else:
                result[key] = [value]

    return result

def get_nomina(nominas, node, child_node):
    nomina = nominas.get(node, {}).get(child_node, {})
    
    return nomina if isinstance(nomina, list) else [nomina]

def get_attribute_nomina(nominas, nomina_type, catalogo_nomina):
    nomina_dict = {}

    importes = [" importe exento", " importe gravado"] if nomina_type == "TipoPercepcion" else [" importe"]
    tipo_nomina = catalogo.c_nomina.get(nomina_type)

    for item in nominas:
        if item:
            concepto = item["_attributes"].get(nomina_type)
            if catalogo_nomina:
                key = f"{nomina_type[4]} {concepto} {tipo_nomina.get(concepto)}"
            else:
                key = f"{nomina_type[4]} {concepto} {item['_attributes'].get('Clave')} {item['_attributes'].get('Concepto')}"
            for importe in importes:
                if key + importe in nomina_dict:
                    nomina_dict[key + importe] += - float(
                        item["_attributes"].get(importe.title().replace(" ", ""), 0)
                        ) if nomina_type[4] == "D" else float(item["_attributes"].get(
                            importe.title().replace(" ", ""), 0))
                else:
                    nomina_dict[key + importe] = - float(
                        item["_attributes"].get(importe.title().replace(" ", ""), 0)
                        ) if nomina_type[4] == "D" else float(item["_attributes"].get(
                            importe.title().replace(" ", ""), 0))

    return nomina_dict

def get_attribute_taxes(item, node, child_node, tipo):
    impuesto = "ImpuestosDR" if tipo == "P" else "Impuestos"
    
    tax_data = item.get(impuesto, {}).get(node, {}).get(child_node, {})
    
    return tax_data if isinstance(tax_data, list) else [tax_data]

def join_tax_values(items, attribute, expected_value):
    
    return ", ".join(
        item["_attributes"].get(attribute, "")
        for item in items
        if "_attributes" in item and item["_attributes"].get("Impuesto") == expected_value
    )

def sum_tax_values(items, attribute, expected_value):
    
    values = [
        item["_attributes"].get(attribute, None)
        for item in items
        if "_attributes" in item and item["_attributes"].get("ImpuestoDR") == expected_value
    ]
    
    if all(val is None for val in values):
        return None
    
    return sum(float(val) for val in values if val is not None)

def get_tax_value(impuestos, value):

    tax_dict = {}

    impuesto_value = value.get("impuesto")
    importe_value = value.get("importe")

    for key, impuesto in impuestos.items():
        if impuesto:
            if isinstance(impuesto, dict):
                impuesto = [impuesto]
            for item in impuesto:
                if "_attributes" in item:
                    tax = item["_attributes"].get(impuesto_value)
                    tax = f"{key} {tax}"
                    if tax in tax_dict:
                        tax_dict[tax] += float(item["_attributes"].get(importe_value, 0))
                    elif item["_attributes"].get(importe_value) == None:
                        pass
                    else:
                        tax_dict[tax] = float(item["_attributes"].get(importe_value, 0))

    return tax_dict

def validate_uuid(emisor, receptor, total, uuid):

    values = "?re=" + emisor + "&rr=" + receptor + "&tt=" + total + "&id=" + uuid

    try:
        client = Client(wsdl = "https://consultaqr.facturaelectronica.sat.gob.mx/consultacfdiservice.svc")
        result = client.service.Consulta(values)
        result = helpers.serialize_object(result)
        
        return result["EsCancelable"], result["Estado"], result["EstatusCancelacion"], result["ValidacionEFOS"]
    
    except:
        
        return None

def parsing_dict(dictionary, status, file, catalogo_nomina):

    invoice = {}
    
    version = dictionary.get("_attributes", {}).get("Version", dictionary.get("_attributes", {}).get("version"))
    clave_retencion = dictionary.get("_attributes", {}).get("CveRetenc")
    value = catalogo.c_retenciones(version) if clave_retencion else catalogo.c_invoice(version)
    tipo = None if clave_retencion else dictionary.get("_attributes", {}).get(value.get("tipo"))

    if tipo:

        emisor = dictionary.get("Emisor").get("_attributes").get(value.get("rfc"))
        nombre_emisor = dictionary.get("Emisor").get("_attributes").get(value.get("nombre"))
        receptor = dictionary.get("Receptor").get("_attributes").get(value.get("rfc"))
        nombre_receptor = dictionary.get("Receptor").get("_attributes").get(value.get("nombre"))
        total = dictionary.get("_attributes").get(value.get("total"))
        uuid = dictionary.get("Complemento", {}).get("TimbreFiscalDigital", {}).get("_attributes", {}).get("UUID")
        tipo = dictionary.get("_attributes").get(value.get("tipo"))
        fecha = dictionary.get("_attributes").get(value.get("fecha"))
        serie = dictionary.get("_attributes").get(value.get("serie"))
        folio = dictionary.get("_attributes").get(value.get("folio"))
        moneda = dictionary.get("_attributes").get("Moneda")
        domicilio = dictionary.get("Receptor").get("Domicilio", {}).get("_attributes", {}).get("codigoPostal")
        if not domicilio:
            domicilio = dictionary.get("Receptor").get("_attributes").get("DomicilioFiscalReceptor")

        cfdi_relacionados = dictionary.get("CfdiRelacionados", [])
        if isinstance(cfdi_relacionados, dict):
            cfdi_relacionados = [cfdi_relacionados]

        concepto = dictionary.get("Conceptos", {}).get("Concepto", [])
        if isinstance(concepto, dict):
            concepto = [concepto]

        impuestos = {
            "traslado": dictionary.get("Impuestos", {}).get("Traslados", {}).get("Traslado"),
            "retencion": dictionary.get("Impuestos", {}).get("Retenciones", {}).get("Retencion")
        }
        impuesto = get_tax_value(impuestos, value)

        invoice.update(
            {
                "global": {
                    "Documento": Path(file).stem,
                    "Fecha": fecha,
                    "Tipo": tipo,
                    "Versión": version,
                    "UUID": uuid,
                    "Serie": serie,
                    "Folio": folio,
                    "RFC de emisor": emisor,
                    "Nombre de emisor": nombre_emisor,
                    "Régimen fiscal de emisor": catalogo.c_RegimenFiscal.get(dictionary.get("Emisor").get("_attributes").get("RegimenFiscal")),
                    "Lugar de expedición": dictionary.get("_attributes").get("LugarExpedicion"),
                    "RFC de receptor": receptor,
                    "Nombre de receptor": nombre_receptor,
                    "Número de ID fiscal receptor": dictionary.get("Receptor").get("_attributes").get("NumRegIdTrib"),
                    "Residencia fiscal receptor": dictionary.get("Receptor").get("_attributes").get("ResidenciaFiscal"),
                    "Régimen fiscal del receptor": catalogo.c_RegimenFiscal.get(dictionary.get("Receptor").get("_attributes").get("RegimenFiscalReceptor")),
                    "Domicilio fiscal receptor": domicilio,
                    "UUID relacionado": " \n".join(
                        item["_attributes"].get("UUID")
                        for relacionado in cfdi_relacionados
                        for item in (
                        relacionado.get("CfdiRelacionado", [])
                        if isinstance(relacionado.get("CfdiRelacionado", []), list)
                        else [relacionado.get("CfdiRelacionado", {})]
                        )
                        if "_attributes" in item
                    ),
                    "Tipo de relación": " \n".join(
                        catalogo.c_TipoRelacion.get(
                        item["_attributes"]["TipoRelacion"],
                        item["_attributes"]["TipoRelacion"])
                        for item in cfdi_relacionados
                        if cfdi_relacionados
                    ),
                    "Exportación": catalogo.c_Exportacion.get(dictionary.get("_attributes").get("Exportacion")),
                    "Moneda": moneda,
                    "Tipo de cambio":  dictionary.get("_attributes").get("TipoCambio"),
                    "Uso": catalogo.c_UsoCFDI.get(dictionary.get("Receptor").get("_attributes").get("UsoCFDI")),
                    "Método de pago": dictionary.get("_attributes").get(value.get("metodo")),
                    "Forma de pago": catalogo.c_FormaPago.get(dictionary.get("_attributes").get(value.get("forma")), dictionary.get("_attributes").get(value.get("forma"))),
                    "Cuenta predial": " \n".join(
                        item["CuentaPredial"]["_attributes"]["Numero"]
                        for item in concepto if "CuentaPredial" in item
                    ),
                    "Clave de prodserv": " \n".join(
                        item["_attributes"]["ClaveProdServ"]
                        for item in concepto
                        if "ClaveProdServ" in item["_attributes"]
                    ),
                    "Tasa o cuota de IVA": ", ".join(
                        item["_attributes"].get("TasaOCuota")
                        or item["_attributes"].get("TipoFactor", "")
                        for item in (
                        impuestos.get("traslado")
                        if isinstance(impuestos.get("traslado"), list)
                        else [impuestos.get("traslado")]
                        if impuestos.get("traslado") is not None
                        else []
                        )
                        if "_attributes" in item
                        and item["_attributes"].get(value.get("impuesto")) == value.get("iva")
                    ),
                    "Concepto": " \n".join(
                        item["_attributes"][value.get("descripcion")]
                        for item in concepto
                    ),
                    "Subtotal": dictionary.get("_attributes").get(value.get("subtotal")),
                    "IVA trasladado": impuesto.get(f"traslado {value.get('iva')}"),
                    "IEPS trasladado": impuesto.get(f"traslado {value.get('ieps')}"),
                    "Impuesto local trasladado": dictionary.get("Complemento", {}).get("ImpuestosLocales", {}).get("_attributes", {}).get("TotaldeTraslados"),
                    "ISR retenido": impuesto.get(f"retencion {value.get('isr')}"),
                    "IVA retenido": impuesto.get(f"retencion {value.get('iva')}"),
                    "IEPS retenido": impuesto.get(f"retencion {value.get('ieps')}"),
                    "Impuesto local retenido": dictionary.get("Complemento", {}).get("ImpuestosLocales", {}).get("_attributes", {}).get("TotaldeRetenciones"),
                    "Descuento": dictionary.get("_attributes").get(value.get("descuento")),
                    "Total": total,
                    }
                }
            )

        if status:
            cancelable, estado, estatus, efos = validate_uuid(emisor, receptor, total, uuid)

            invoice_status = {
                "Es cancelable" : cancelable,
                "Estado": estado,
                "Estatus de cancelacion": estatus,
                "EFO": catalogo.c_efos.get(efos)
                }

            invoice.get("global").update(invoice_status)

        invoice.update(
            {
                "concepto": {
                    "Documento": Path(file).stem,
                    "Fecha": fecha,
                    "Tipo": tipo,
                    "Versión": version,
                    "UUID": uuid,
                    "Serie": serie,
                    "Folio": folio,
                    "RFC de emisor": emisor,
                    "Nombre de emisor": nombre_emisor,
                    "RFC de receptor": receptor,
                    "Nombre de receptor": nombre_receptor,
                    "Clave de prodserv": [
                        item["_attributes"].get("ClaveProdServ", "")
                        for item in concepto
                    ],
                    "Descripción": [
                        item["_attributes"][value.get("descripcion")]
                        for item in concepto
                    ],
                    "Número identificación": [
                        item["_attributes"].get(value.get("noidentificacion"), "")
                        for item in concepto
                    ],
                    "Clave de unidad": [
                        item["_attributes"].get("ClaveUnidad", "")
                        for item in concepto
                    ],
                    "Cantidad": [
                        item["_attributes"][value.get("cantidad")]
                        for item in concepto
                    ],
                    "Valor unitario": [
                        item["_attributes"][value.get("valor")]
                        for item in concepto
                    ],
                    "Importe": [
                        item["_attributes"][value.get("importe")]
                        for item in concepto
                    ],
                    "Descuento": [
                        item["_attributes"].get(value.get("descuento"), "")
                        for item in concepto
                    ]
                }
            }
        )

        concepto_impuesto = {}

        for tax, node, child_node, attribute in catalogo.list_impuesto:
            key = f"{tax.upper()} {attribute.lower()} {child_node.lower()}"
            concepto_impuesto[key] = [
                join_tax_values(
                    get_attribute_taxes(item, node, child_node, tipo),
                    attribute,
                    value.get(tax)
                )
                for item in concepto
            ]

        invoice.get("concepto").update(concepto_impuesto)
    
    if tipo == "P":

        pagos = dictionary.get("Complemento").get("Pagos", {}).get("Pago", [])
        if isinstance(pagos, dict):
            pagos = [pagos]
        
        doc_relacionado = []
        for item in [pago.get("DoctoRelacionado", {}) for pago in pagos]:
            if isinstance(item, list):
                doc_relacionado.extend(item)
            else:
                doc_relacionado.append(item)

        invoice.update(
            {
                "pago": {
                    "Documento": Path(file).stem,
                    "Fecha": fecha,
                    "Tipo": tipo,
                    "Versión": dictionary.get("Complemento").get("Pagos", {}).get("_attributes", {}).get("Version"),
                    "UUID": uuid,
                    "Serie": serie,
                    "Folio": folio,
                    "RFC de emisor": emisor,
                    "Nombre de emisor": nombre_emisor,
                    "RFC de receptor": receptor,
                    "Nombre de receptor": nombre_receptor,
                    "Fecha de pago": ", ".join(pago.get("_attributes", {}).get("FechaPago") for pago in pagos),
                    "Moneda": ", ".join(pago.get("_attributes", {}).get("MonedaP") for pago in pagos),
                    "Forma de pago": ", ".join(catalogo.c_FormaPago.get(pago["_attributes"].get("FormaDePagoP"), pago["_attributes"].get("FormaDePagoP")) for pago in pagos),
                    "Método de pago": [doc.get("_attributes", {}).get("MetodoDePagoDR") for doc in doc_relacionado],
                    "Monto": ", ".join(pago.get("_attributes", {}).get("Monto") for pago in pagos),
                    "Total pagos": dictionary.get("Complemento").get("Pagos", {}).get("Totales", {}).get("_attributes", {}).get("MontoTotalPagos"),
                    "Total base IVA exento": dictionary.get("Complemento").get("Pagos", {}).get("Totales", {}).get("_attributes", {}).get("TotalTrasladosBaseIVAExento"),
                    "Total base IVA 0% traslado": dictionary.get("Complemento").get("Pagos", {}).get("Totales", {}).get("_attributes", {}).get("TotalTrasladosBaseIVA0"),
                    "Total IVA 0% traslado": dictionary.get("Complemento").get("Pagos", {}).get("Totales", {}).get("_attributes", {}).get("TotalTrasladosImpuestoIVA0"),
                    "Total base IVA 8% traslado": dictionary.get("Complemento").get("Pagos", {}).get("Totales", {}).get("_attributes", {}).get("TotalTrasladosBaseIVA8"),
                    "Total IVA 8% traslado": dictionary.get("Complemento").get("Pagos", {}).get("Totales", {}).get("_attributes", {}).get("TotalTrasladosImpuestoIVA8"),
                    "Total base IVA 16% traslado": dictionary.get("Complemento").get("Pagos", {}).get("Totales", {}).get("_attributes", {}).get("TotalTrasladosBaseIVA16"),
                    "Total IVA 16% traslado": dictionary.get("Complemento").get("Pagos", {}).get("Totales", {}).get("_attributes", {}).get("TotalTrasladosImpuestoIVA16"),
                    "Total retenciones ISR": dictionary.get("Complemento").get("Pagos", {}).get("Totales", {}).get("_attributes", {}).get("TotalRetencionesISR"),
                    "Total retenciones IVA": dictionary.get("Complemento").get("Pagos", {}).get("Totales", {}).get("_attributes", {}).get("TotalRetencionesIVA"),
                    "Total retenciones IEPS": dictionary.get("Complemento").get("Pagos", {}).get("Totales", {}).get("_attributes", {}).get("TotalRetencionesIEPS"),
                    "Serie de documento": [doc.get("_attributes", {}).get("Serie") for doc in doc_relacionado],
                    "Folio de documento": [doc.get("_attributes", {}).get("Folio") for doc in doc_relacionado],
                    "UUID de documento": [doc.get("_attributes", {}).get("IdDocumento") for doc in doc_relacionado],
                    "Número de parcialidad": [doc.get("_attributes", {}).get("NumParcialidad") for doc in doc_relacionado],
                    "Moneda de documento": [doc.get("_attributes", {}).get("MonedaDR") for doc in doc_relacionado],
                    "Equivalencia de documento": [doc.get("_attributes", {}).get("EquivalenciaDR") for doc in doc_relacionado],
                    "Saldo anterior": [doc.get("_attributes", {}).get("ImpSaldoAnt") for doc in doc_relacionado],
                    "Importe pagado": [doc.get("_attributes", {}).get("ImpPagado") for doc in doc_relacionado],
                    "Saldo insoluto": [doc.get("_attributes", {}).get("ImpSaldoInsoluto") for doc in doc_relacionado]
                }
            }
        )

        pago_impuesto = {}

        seen = set()
        for tax, node, child_node, attribute in catalogo.list_impuesto:
            if (tax, node, child_node) not in seen:
                seen.add((tax, node, child_node))
                key = f"{tax.upper()} {child_node.lower()}"
                pago_impuesto[key] = [
                    sum_tax_values(
                        get_attribute_taxes(item, node + "DR", child_node + "DR", tipo),
                        "ImporteDR",
                        value.get(tax)
                    )
                    for item in doc_relacionado
                ]

            invoice.get("pago").update(pago_impuesto)

    if tipo == "N":

        nominas = dictionary.get("Complemento").get("Nomina", {})
        if isinstance(nominas, dict):
            nominas = [nominas]

        invoice.update(
            {
                "nomina": {
                    "Documento": Path(file).stem,
                    "Fecha": fecha,
                    "Tipo": tipo,
                    "Versión": [nomina["_attributes"].get("Version") for nomina in nominas],
                    "UUID": uuid,
                    "Serie": serie,
                    "Folio": folio,
                    "RFC de emisor": emisor,
                    "Nombre de emisor": nombre_emisor,
                    "Registro patronal": [nomina.get("Emisor", {}).get("_attributes", {}).get("RegistroPatronal") for nomina in nominas],
                    "Subcontratación RFC": [nomina["Receptor"].get("SubContratacion", {}).get("_attributes", {}).get("RfcLabora") for nomina in nominas],
                    "Subcontratación porcentaje": [nomina["Receptor"].get("SubContratacion", {}).get("_attributes", {}).get("PorcentajeTiempo") for nomina in nominas],
                    "RFC de receptor": receptor,
                    "CURP": [nomina["Receptor"].get("_attributes").get("Curp") for nomina in nominas],
                    "Nombre de receptor": nombre_receptor,
                    "Tipo de nómina": [nomina["_attributes"].get("TipoNomina") for nomina in nominas],
                    "Moneda": moneda,
                    "Número de seguridad social": [nomina["Receptor"].get("_attributes").get("NumSeguridadSocial") for nomina in nominas],
                    "Fecha de inicio de relación laboral": [nomina["Receptor"].get("_attributes").get("FechaInicioRelLaboral") for nomina in nominas],
                    "Antigüedad": [nomina["Receptor"].get("_attributes").get("Antigüedad") for nomina in nominas],
                    "Sindicalizado": [nomina["Receptor"].get("_attributes").get("Sindicalizado") for nomina in nominas],
                    "Número de empleado": [nomina["Receptor"].get("_attributes").get("NumEmpleado") for nomina in nominas],
                    "Departamento":[nomina["Receptor"].get("_attributes").get("Departamento") for nomina in nominas],
                    "Puesto":[nomina["Receptor"].get("_attributes").get("Puesto") for nomina in nominas],
                    "Riesgo de puesto": [catalogo.c_RiesgoPuesto.get(nomina["Receptor"].get("_attributes").get("RiesgoPuesto")) for nomina in nominas],
                    "Tipo de contrato": [catalogo.c_TipoContrato.get(nomina["Receptor"].get("_attributes").get("TipoContrato")) for nomina in nominas],
                    "Tipo de régimen": [catalogo.c_TipoRegimen.get(nomina["Receptor"].get("_attributes").get("TipoRegimen")) for nomina in nominas],
                    "Tipo de jornada":[catalogo.c_TipoJornada.get(nomina["Receptor"].get("_attributes").get("TipoJornada")) for nomina in nominas],
                    "Periodicidad de pago": [catalogo.c_PeriodicidadPago.get(nomina["Receptor"].get("_attributes").get("PeriodicidadPago")) for nomina in nominas],
                    "Salario base de cot apor": [nomina["Receptor"].get("_attributes").get("SalarioBaseCotApor") for nomina in nominas],
                    "Salario diario integrado": [nomina["Receptor"].get("_attributes").get("SalarioDiarioIntegrado") for nomina in nominas],
                    "Clave entidad federativa": [nomina["Receptor"].get("_attributes").get("ClaveEntFed") for nomina in nominas],
                    "Número de días pagados": [nomina["_attributes"].get("NumDiasPagados") for nomina in nominas],
                    "Fecha inicial de pago": [nomina["_attributes"].get("FechaInicialPago") for nomina in nominas],
                    "Fecha final de pago": [nomina["_attributes"].get("FechaFinalPago") for nomina in nominas],
                    "Fecha de pago": [nomina["_attributes"].get("FechaPago") for nomina in nominas],
                    "Total de percepciones": [nomina["_attributes"].get("TotalPercepciones") for nomina in nominas],
                    "Total de deducciones": [nomina["_attributes"].get("TotalDeducciones") for nomina in nominas],
                    "Total de otros pagos": [nomina["_attributes"].get("TotalOtrosPagos") for nomina in nominas],
                    "Total": total
                }
            }
        )

        for node, child_node, nomina_type in catalogo.nomina_types:
            invoice.get("nomina").update(flatten_dict([
                get_attribute_nomina(get_nomina(nomina, node, child_node), nomina_type, catalogo_nomina) for nomina in nominas
                ]))

    if clave_retencion:
        
        retenciones = dictionary.get("Totales").get("ImpRetenidos", {})
        if isinstance(retenciones, dict):
            retenciones = [retenciones]

        invoice.update(
            {
                "retencion": {
                    "Documento": Path(file).stem,
                    "Fecha": dictionary.get("_attributes").get("FechaExp"),
                    "Clave de retención": catalogo.c_retencion.get(dictionary.get("_attributes").get("CveRetenc")),
                    "Versión": version,
                    "UUID": dictionary.get("Complemento").get("TimbreFiscalDigital", {}).get("_attributes", {}).get("UUID"),
                    "Folio": dictionary.get("_attributes").get("FolioInt"),
                    "RFC de emisor": dictionary.get("Emisor").get("_attributes").get(value.get("rfc_emisor")),
                    "CURP de emisor": dictionary.get("Emisor").get("_attributes").get("CURPE"),
                    "Nombre de emisor": dictionary.get("Emisor").get("_attributes").get("NomDenRazSocE"),
                    "Régimen fiscal del emisor": catalogo.c_RegimenFiscal.get(dictionary.get("Emisor").get("_attributes").get("RegimenFiscalE")),
                    "Lugar de expedición": dictionary.get("_attributes").get("LugarExpRetenc"),
                    "RFC o ID fiscal de receptor": dictionary.get("Receptor").get("Nacional", {}).get("_attributes", {}).get(value.get("rfc_receptor"), dictionary.get("Receptor").get("Nacional", {}).get("_attributes", {}).get(value.get("tax_id"))),
                    "CURP de receptor": dictionary.get("Receptor").get("Nacional", {}).get("_attributes", {}).get(value.get("curp")),
                    "Nombre de receptor": dictionary.get("Receptor").get("Nacional", {}).get("_attributes", {}).get("NomDenRazSocR", dictionary.get("Receptor").get("Extranjero", {}).get("_attributes", {}).get("NomDenRazSocR")),
                    "Domicilio fiscal de receptor": dictionary.get("Receptor").get("Nacional", {}).get("_attributes", {}).get("DomicilioFiscalR"),
                    "UUID relacionado": dictionary.get("CfdiRetenRelacionados", {}).get("_attributes", {}).get("UUID"),
                    "Tipo de relación": catalogo.c_TipoRelacion.get(dictionary.get("CfdiRetenRelacionados", {}).get("_attributes", {}).get("TipoRelacion"), dictionary.get("CfdiRetenRelacionados", {}).get("_attributes", {}).get("TipoRelacion")),
                    "Descripción de retención": dictionary.get("_attributes").get("DescRetenc"),
                    "Mes inicial": dictionary.get("Periodo").get("_attributes").get("MesIni"),
                    "Mes final": dictionary.get("Periodo").get("_attributes").get("MesFin"),
                    "Ejercicio": dictionary.get("Periodo").get("_attributes").get(value.get("ejercicio")),
                    "Total de la operacion": dictionary.get("Totales").get("_attributes").get(value.get("total")),
                    "Total gravado": dictionary.get("Totales").get("_attributes").get(value.get("total_gravado")),
                    "Total exento": dictionary.get("Totales").get("_attributes").get(value.get("total_exento")),
                    "Total retenido": dictionary.get("Totales").get("_attributes").get(value.get("total_retenido")),
                    "Utilidad bimestral": dictionary.get("Totales").get("_attributes").get("UtilidadBimestral"),
                    "ISR bimestral": dictionary.get("Totales").get("_attributes").get("ISRCorrespondiente"),
                }
            }
        )

        tax_withheld = {}
        for tax in retenciones:
            if tax:
                tax_withheld[f"{catalogo.c_impuesto.get(float(tax.get('_attributes').get(value.get('impuesto_retenido'))))} base de retención"] = tax.get("_attributes").get("BaseRet")
                tax_withheld[f"{catalogo.c_impuesto.get(float(tax.get('_attributes').get(value.get('impuesto_retenido'))))} monto retenido"] = tax.get("_attributes").get(value.get("monto_retenido"))
                tax_withheld[f"{catalogo.c_impuesto.get(float(tax.get('_attributes').get(value.get('impuesto_retenido'))))} tipo de pago"] = catalogo.c_pago.get(tax.get("_attributes").get("TipoPagoRet"))

        invoice.get("retencion").update(tax_withheld)

    return invoice

def iter_xml(xml):

    xml_dict = {
        "_attributes": xml.attrib
    }

    for child in xml.iterchildren():
        if child.tag is None or not isinstance(child.tag, str):
            continue
        child_dict = iter_xml(child)
        key = child.tag.rsplit('}', 1)[-1]
        if key in xml_dict:
            if not isinstance(xml_dict[key], list):
                xml_dict[key] = [xml_dict[key]]
            xml_dict[key].append(child_dict)
        else:
            xml_dict[key] = child_dict

    return xml_dict

def parsing_xml(file, status, catalogo_nomina):

    try:

        xml = etree.parse(file).getroot()
        return parsing_dict(iter_xml(xml), status, file, catalogo_nomina)
    
    except Exception as e:
        
        traceback.print_exc()
        error_message = str(e)
        current_traceback = traceback.extract_tb(e.__traceback__)
        filename, line_number, function_name, _ = current_traceback[-1]
        error_details = f"File: {filename}, Line: {line_number}, Function: {function_name}, Error: {error_message}"

        return {
                "error": {
                    "Documento": Path(file).stem,
                    "Extensión": Path(file).suffix,
                    "Directorio": Path(file).parent,
                    "Error": error_details
                }
            }