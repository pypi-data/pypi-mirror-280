import base64
import logging
from pathlib import Path
from requests.models import Response
from typing import NamedTuple, Tuple
from urllib.parse import unquote
# noinspection PyPep8Naming
import xml.etree.ElementTree as ET


__all__ = ["Header", "Merchant", "Buyer", "Item", "Disbursement", "SmartBillResponse", "PdfDataMissingError", "EmailDetails", ]  # "WayBill"
logger = logging.getLogger(__name__)


class PdfDataMissingError(Exception):
    pass


class Header(NamedTuple):
    """<fejlec>"""
    creating_date: str = ""  # <keltDatum>2020-01-20</keltDatum>
    payment_date: str = ""  # <teljesitesDatum>2020-01-20</teljesitesDatum>
    due_date: str = ""  # <fizetesiHataridoDatum>2020-01-20</fizetesiHataridoDatum>
    payment_type: str = "Átutalás"  # <fizmod>Átutalás</fizmod>
    currency: str = "RON"  # <penznem>HUF</penznem>
    invoice_language: str = "ro"  # <szamlaNyelve>hu</szamlaNyelve> // can  be: de, en, it, hu, fr, ro, sk, hr
    invoice_comment: str = ""  # <megjegyzes>Invoice comment</megjegyzes>
    name_of_bank: str = "RNB"  # <arfolyamBank>MNB</arfolyamBank>
    exchange_rate: float = 0.0  # <arfolyam>0.0</arfolyam>
    order_number: str = ""  # <rendelesSzam></rendelesSzam>
    use_estimate: str = 'false'
    pro_forma_number_ref: str = ""
    pro_forma_serie_ref: str = ""
    deposit_invoice: bool = False  # <elolegszamla>false</elolegszamla>
    invoice_after_deposit_invoice: bool = False  # <vegszamla>false</vegszamla>
    down_payment_invoice_number: str = "" # <elolegSzamlaszam></elolegSzamlaszam>
    correction_invoice: bool = False  # <helyesbitoszamla>false</helyesbitoszamla>
    number_of_corrected_invoice: str = ""  # <helyesbitettSzamlaszam></helyesbitettSzamlaszam>
    proforma_invoice: bool = False  # <dijbekero>false</dijbekero>
    # szallitolevel
    # logoExtra
    invoice_prefix: str = ""  # <szamlaszamElotag></szamlaszamElotag>
    invoice_number: str = ""  # <szamlaszam>E-TST-2011-1</szamlaszam>  // needed for reverse_invoice|storno only
    invoice_template: str = ""  # <!-- Codomain: 'SzlaMost' | 'SzlaAlap' | 'SzlaNoEnv' | 'Szla8cm' | 'SzlaTomb' | 'SzlaFuvarlevelesAlap' -->


class Merchant(NamedTuple):
    """<elado>"""
    bank_name: str = ""  # <bank>BB</bank>
    bank_account_number: str = ""  # <bankszamlaszam>11111111-22222222-33333333</bankszamlaszam>
    reply_email_address: str = ""  # <emailReplyto> </emailReplyto>
    email_subject: str = ""  # <emailTargy>Invoice notification</emailTargy>
    email_text: str = ""  # <emailSzoveg>mail text</emailSzoveg>
    signatory_name: str = "" # <alairoNeve>Kovacs Peter</alairoNeve>
    VAT: str = "" # <alairoNeve>Kovacs Peter</alairoNeve>


class Buyer(NamedTuple):
    """<vevo>"""
    name: str = ""  # <nev>Kovacs Bt.</nev>
    country: str = ""  # <orszag>Hungary</orszag>
    county: str = ""  # Sibiu
    zip_code: str = ""  # <irsz>2030</irsz>
    city: str = ""  # <telepules>Érd</telepules>
    address: str = ""  # <cim>Tárnoki út 23.</cim>
    email: str = ""  # <email>buyer@example.com</email>
    send_email: bool = False  # <sendEmail>false</sendEmail>
    tax_subject: int = 0 # <adoalany>-1</adoalany> <!-- Possible values are 7:business is based outside of the European Union, 6:business is based in the Europen Union, 1: has a hungarian tax number, 0: we don't know, if the buyer has a tax number, -1: no tax number -->
    tax_number: str = ""  # <adoszam>12345678-1-42</adoszam>
    group_id: str = "" # <csoportazonosito>?</csoportazonosito>
    tax_number_eu: str = ""  # <adoszamEU>HU55555555</adoszamEU>
    delivery_name: str = ""  # <postazasiNev>Kovács Bt. mailing name</postazasiNev>
    delivery_country: str = ""  # <postazasiOrszag>Hungary</postazasiOrszag>
    delivery_zip: str = ""  # <postazasiIrsz>2040</postazasiIrsz>
    delivery_city: str = ""  # <postazasiTelepules>Budaörs</postazasiTelepules>
    delivery_address: str = ""  # <postazasiCim>Szivárvány utca 8.</postazasiCim>
    # vevoFokonyv TODO: to be implemented if needed
    identification: str = ""  # <azonosito>1234</azonosito>
    signatory_name: str = "" # <alairoNeve>Kovacs Peter</alairoNeve>
    phone_number: str = ""  # <telefonszam>Tel:+3630-555-55-55, Fax:+3623-555-555</telefonszam>
    comment: str = ""  # <megjegyzes>Call extension 214 from the reception</megjegyzes>


# class WayBill(NamedTuple):
#     """<fuvarlevel>"""
#      <!-- waybill/confinement note, you do not need this: omit the entire tag -->
#     uticel: str = ""  #
#     futarSzolgalat: str = ""  #


class ItemLedger(NamedTuple):
    # language=XML
    """
    <sequence>
        <element name="gazdasagiEsem" type="string" maxOccurs="1" minOccurs="0"></element>
        <element name="gazdasagiEsemAfa" type="string" maxOccurs="1" minOccurs="0"></element>
        <element name="arbevetelFokonyviSzam" type="string" maxOccurs="1" minOccurs="0"></element>
        <element name="afaFokonyviSzam" type="string" maxOccurs="1" minOccurs="0"></element>
        <element name="elszDatumTol" type="date" maxOccurs="1" minOccurs="0"></element>
        <element name="elszDatumIg" type="date" maxOccurs="1" minOccurs="0"></element>
    </sequence>
    """
    economic_event: str = ""  # <gazdasagiesemeny></gazdasagiesemeny>
    economic_event_tax: str = ""  # <gazdasagiesemenyafa></gazdasagiesemenyafa>
    sales_ledger_number: str = ""
    vat_ledger_number: str = ""
    settlement_date_from: str = ""
    settlement_date_to: str = ""


class Item(NamedTuple):
    name: str = ""  # <megnevezes>Elado izé</megnevezes>
    identifier: str = ""  # <azonosito>ASD-123</azonosito>
    quantity: str = ""  # <mennyiseg>1.0</mennyiseg>
    quantity_unit: str = ""  # <mennyisegiEgyseg>db</mennyisegiEgyseg>
    unit_price: str = ""  # <nettoEgysegar>10000</nettoEgysegar>
    vat_rate: str = ""  # <afakulcs>27</afakulcs>
    vat_name: str = ""  # SFDD, Normala
    margin_tax_base: float = ""  # <arresAfaAlap>10.25</arresAfaAlap>
    net_price: str = ""  # <nettoErtek>10000.0</nettoErtek>
    vat_amount: str = ""  # <afaErtek>2700.0</afaErtek>
    gross_amount: str = ""  # <bruttoErtek>12700.0</bruttoErtek>
    comment_for_item: str = ""  # <megjegyzes>lorem ipsum</megjegyzes>
    item_ledger: ItemLedger = ""  # <element name="tetelFokonyv" type="tns:tetelFokonyvTipus" maxOccurs="1" minOccurs="0"></element>
    discount_type: str = ""
    discount_percentage: str = ""
    isdiscount: str = "false"


class Disbursement(NamedTuple):
    date: str
    title: str
    amount: float
    description: str = ""


class EmailDetails(NamedTuple):
    addresses: str
    reply_to_address: str
    subject: str
    body_text: str = ""


class SmartBillResponse:
    def __init__(self,
                 response: Response,
                 xml_namespace: str,
                 ):
        self.xml_namespace = xml_namespace
        self.__response = response
        self.__action_success: bool = False
        content_type = response.headers.get("Content-Type")
        if content_type == "application/octet-stream":
            # Parse XML and map into class members
            root = ET.fromstring(self.__response.text)
            self.__pdf: str = self.__get_tag_text(root, "pdf")
            self.__pdf_bytes: bytes = b""
            self.__action_success: bool = True if (self.__get_tag_text(root, "sikeres") == "true") else False
        else:
            self.__pdf_bytes: bytes = response.content
            self.__pdf: str = base64.b64encode(self.__pdf_bytes).decode("ascii")

        # Error Handling
        self.__has_errors = False
        self.error_code: int = response.status_code
        self.error_message: str = ''
        if self.error_code != 200:
            root = ET.fromstring(response.text)

            if root.find('errorText') is not None:
                self.error_message = root.find('errorText').text
            else:
                self.error_message = response.text

            self.error_message = unquote(self.error_message)
            logger.error(f"Error Code: {self.error_code}")
            logger.error(f"Error Message: {self.error_message}")
            self.__has_errors = True
        self.http_request_success: str = "false" if self.error_code != 200 else "true"

        # Extract Details
        if self.error_code == 200:
            root = ET.fromstring(response.text)

            self.invoice_number: str = ''
            self.invoice_prefix: str = ''
            if root.find('number').text:
                if root.find('series').text:
                    self.invoice_number = root.find('number').text
                    self.invoice_prefix = root.find('series').text

        # invoice url
        self.buyer_account_url : str = ''
        if root.find('url') is not None:
            self.buyer_account_url = root.find('url').text

    @property
    def action_success(self) -> bool:
        return self.__action_success

    @property
    def has_errors(self):
        return self.__has_errors

    @property
    def ok(self):
        """
        Shortcut to the original response's attribute with the same name
        """
        return self.__response.ok

    @property
    def response(self) -> Response:
        """
        Original HTTP Response object returned by the requests package
        :return: requests.models.Response
        """
        return self.__response

    @property
    def text(self) -> str:
        """
        Shortcut to the original response's attribute with the same name
        """
        return self.__response.text

    def get_pdf_base64(self) -> str:
        """
        Get PDF from response in Base64 format
        :return: PDF (in Base64 format)
        :rtype: str
        """
        if (not self.__pdf) and (not self.__pdf_bytes):
            raise PdfDataMissingError("No PDF was returned. Check the value of szamlaLetoltes|invoice_download")
        return self.__pdf

    def get_pdf_bytes(self) -> bytes:
        pdf_base64 = self.get_pdf_base64()
        return base64.b64decode(pdf_base64) if pdf_base64 else self.__pdf_bytes

    def write_pdf_to_disk(self, pdf_output_path: Path):
        if not pdf_output_path.parent.exists():
            raise FileNotFoundError(f"Output file's parent folder is missing: {pdf_output_path.parent.as_posix()}")
        data = self.get_pdf_bytes()
        with open(pdf_output_path, "wb+") as f:
            f.write(data)

    def print_errors(self) -> Tuple[str, str]:
        """
        Prints the returned error_code and error_message
        :return: Tuple[error_code, error_message]
        """
        if self.has_errors:
            print("error_code:", self.error_code)
            print("error_message:", self.error_message)
        return self.error_code, self.error_message

    def __get_tag_text(self, root: ET.Element, tag_name):
        tag = root.find(f"{self.xml_namespace}{tag_name}")
        return tag.text if tag is not None else None
