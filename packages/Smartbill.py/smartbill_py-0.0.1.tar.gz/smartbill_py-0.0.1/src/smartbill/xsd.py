from lxml import etree
from typing import Tuple


__all__ = ["validate", ]


class ValidationError(Exception):
    pass


def validate(xml: str, xsd: str) -> Tuple[bool, str]:
    parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
    # XSD
    xmlschema_doc = etree.fromstring(xsd.encode('utf-8'), parser=parser)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    # XML
    xml_doc = etree.fromstring(xml.encode('utf-8'), parser=parser)
    result = xmlschema.validate(xml_doc)

    # xmlschema.error_log.last_error => lxml.etree._LogEntry
    return result, str(xmlschema.error_log.last_error)

# language=XSD
generate_invoice = """<?xml version="1.0" encoding="UTF-8"?>
<tns:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:tns="http://www.w3.org/2001/XMLSchema">
  <tns:element name="invoice">
    <tns:complexType>
      <tns:sequence>
        <tns:element type="tns:string" name="companyVatCode"/>
        <tns:element name="client">
          <tns:complexType>
            <tns:sequence>
              <tns:element type="tns:string" name="name"/>
              <tns:element type="tns:string" name="vatCode"/>
              <tns:element type="tns:string" name="regCom" maxOccurs="1" minOccurs="0"/>
              <tns:element type="tns:string" name="address"/>
              <tns:element type="tns:string" name="isTaxPayer"/>
              <tns:element type="tns:string" name="city"/>
              <tns:element type="tns:string" name="county"/>
              <tns:element type="tns:string" name="country"/>
              <tns:element type="tns:string" name="email" maxOccurs="1" minOccurs="0"/>
              <tns:element type="tns:string" name="saveToDb"/>
            </tns:sequence>
          </tns:complexType>
        </tns:element>
        <tns:element type="tns:string" name="isDraft"/>
        <tns:element type="tns:date" name="issueDate"/>
        <tns:element type="tns:string" name="seriesName"/>
        <tns:element type="tns:string" name="currency"/>
        <tns:element type="tns:float" name="exchangeRate" maxOccurs="1" minOccurs="0"/>
        <tns:element type="tns:string" name="language"/>
        <tns:element type="tns:byte" name="precision"/>
        <tns:element type="tns:date" name="dueDate"/>
        <tns:element type="tns:string" name="useEstimateDetails"/>
        <tns:element name="estimate" maxOccurs="1" minOccurs="0">
          <tns:complexType>
            <tns:sequence>
              <tns:element type="tns:string" name="seriesName"/>
              <tns:element type="tns:short" name="number"/>
            </tns:sequence>
          </tns:complexType>
        </tns:element>
        <tns:element name="payment" maxOccurs="1" minOccurs="0">
          <tns:complexType>
            <tns:sequence>
              <tns:element type="tns:byte" name="value"/>
              <tns:element type="tns:string" name="type"/>
              <tns:element type="tns:string" name="isCash"/>
            </tns:sequence>
          </tns:complexType>
        </tns:element>
        <tns:element name="product" maxOccurs="999" minOccurs="1">
          <tns:complexType>
            <tns:sequence>
              <tns:element type="tns:string" name="name"/>
              <tns:element type="tns:string" name="code" maxOccurs="1" minOccurs="0"/>
              <tns:element type="tns:string" name="productDescription" maxOccurs="1" minOccurs="0"/>
              <tns:element type="tns:string" name="isDiscount"/>
              <tns:element type="tns:short" name="numberOfItems" maxOccurs="1" minOccurs="0"/>
              <tns:element type="tns:string" name="measuringUnitName"/>
              <tns:element type="tns:string" name="currency"/>
              <tns:element type="tns:float" name="quantity" maxOccurs="1" minOccurs="0"/>
              <tns:element type="tns:float" name="price" maxOccurs="1" minOccurs="0"/>
              <tns:element type="tns:string" name="isTaxIncluded"/>
              <tns:element type="tns:string" name="taxName"/>
              <tns:element type="tns:float" name="taxPercentage"/>
              <tns:element type="tns:string" name="saveToDb" maxOccurs="1" minOccurs="0"/>
              <tns:element type="tns:string" name="isService" maxOccurs="1" minOccurs="0"/>
              <tns:element type="tns:string" name="discountType" maxOccurs="1" minOccurs="0"/>
              <tns:element type="tns:string" name="discountPercentage" maxOccurs="1" minOccurs="0"/>
            </tns:sequence>
          </tns:complexType>
        </tns:element>
      </tns:sequence>
    </tns:complexType>
  </tns:element>
</tns:schema>"""

# language=XSD
generate_proforma_invoice = """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="estimate" type="estimateType"/>
  <xs:complexType name="clientType">
    <xs:sequence>
      <xs:element type="xs:string" name="name"/>
      <xs:element type="xs:string" name="vatCode"/>
      <xs:element type="xs:string" name="regCom" maxOccurs="1" minOccurs="0"/>
      <xs:element type="xs:string" name="isTaxPayer"/>
      <xs:element type="xs:string" name="address"/>
      <xs:element type="xs:string" name="city"/>
      <xs:element type="xs:string" name="county"/>
      <xs:element type="xs:string" name="country"/>
      <xs:element type="xs:string" name="email" maxOccurs="1" minOccurs="0"/>
      <xs:element type="xs:string" name="saveToDb"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="productType">
    <xs:sequence>
      <xs:element type="xs:string" name="name"/>
      <xs:element type="xs:string" name="code" maxOccurs="1" minOccurs="0"/>
      <xs:element type="xs:string" name="productDescription" maxOccurs="1" minOccurs="0"/>
      <xs:element type="xs:string" name="isDiscount"/>
      <xs:element type="xs:short" name="numberOfItems" maxOccurs="1" minOccurs="0"/>
      <xs:element type="xs:string" name="measuringUnitName"/>
      <xs:element type="xs:string" name="currency"/>
      <xs:element type="xs:float" name="quantity" maxOccurs="1" minOccurs="0"/>
      <xs:element type="xs:float" name="price" maxOccurs="1" minOccurs="0"/>
      <xs:element type="xs:string" name="isTaxIncluded"/>
      <xs:element type="xs:string" name="taxName"/>
      <xs:element type="xs:float" name="taxPercentage"/>
      <xs:element type="xs:string" name="saveToDb" maxOccurs="1" minOccurs="0"/>
      <xs:element type="xs:string" name="isService" maxOccurs="1" minOccurs="0"/>
      <xs:element type="xs:string" name="discountType" maxOccurs="1" minOccurs="0"/>
      <xs:element type="xs:string" name="discountPercentage" maxOccurs="1" minOccurs="0"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="estimateType">
    <xs:sequence>
      <xs:element type="xs:string" name="companyVatCode"/>
      <xs:element type="clientType" name="client"/>
      <xs:element type="xs:date" name="issueDate"/>
      <xs:element type="xs:string" name="seriesName"/>
      <xs:element type="xs:string" name="currency"/>
      <xs:element type="xs:float" name="exchangeRate" maxOccurs="1" minOccurs="0"/>
      <xs:element type="xs:string" name="language"/>
      <xs:element type="xs:byte" name="precision"/>
      <xs:element type="xs:date" name="dueDate"/>
      <xs:element type="productType" name="product" maxOccurs="999" minOccurs="0"/>
    </xs:sequence>
  </xs:complexType>
</xs:schema>"""


# language=XSD
reverse_invoice = """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="invoice" type="invoiceType"/>
  <xs:complexType name="invoiceType">
    <xs:sequence>
      <xs:element type="xs:string" name="companyVatCode"/>
      <xs:element type="xs:string" name="seriesName"/>
      <xs:element type="xs:short" name="number"/>
      <xs:element type="xs:date" name="issueDate"/>
    </xs:sequence>
  </xs:complexType>
</xs:schema>
"""

# language=XSD
credit_entry = """<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.szamlazz.hu/xmlszamlakifiz" xmlns:tns="http://www.szamlazz.hu/xmlszamlakifiz" elementFormDefault="qualified">
<complexType name="beallitasokTipus">
  <sequence>
    <element name="felhasznalo" type="string" maxOccurs="1" minOccurs="0"></element>
    <element name="jelszo" type="string" maxOccurs="1" minOccurs="0"></element>
    <element name="szamlaagentkulcs" type="string" maxOccurs="1" minOccurs="0"></element>
    <element name="szamlaszam" type="string" maxOccurs="1" minOccurs="1"></element>
    <element name="additiv" type="boolean" maxOccurs="1" minOccurs="1"></element>
  </sequence>
</complexType>
<complexType name="kifizetesTipus">
  <sequence>
    <element name="datum" type="date" maxOccurs="1" minOccurs="1"></element>
    <element name="jogcim" type="string" maxOccurs="1" minOccurs="1"></element>
    <element name="osszeg" type="double" maxOccurs="1" minOccurs="1"></element>
    <element name="leiras" type="string" maxOccurs="1" minOccurs="0"></element>
  </sequence>
</complexType>
<complexType name="szamlaKifizTipus">
  <sequence>
    <element name="beallitasok" type="tns:beallitasokTipus" maxOccurs="1" minOccurs="1"></element>
    <element name="kifizetes" type="tns:kifizetesTipus" maxOccurs="5" minOccurs="0"></element>
  </sequence>
</complexType>
<element name="xmlszamlakifiz" type="tns:szamlaKifizTipus"></element>
</schema>"""


# language=XSD
query_invoice_pdf = """<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.szamlazz.hu/xmlszamlapdf"
xmlns:tns="http://www.szamlazz.hu/xmlszamlapdf" elementFormDefault="qualified">
  <complexType name="beallitasokTipus">
    <sequence>
      <element name="felhasznalo" type="string" maxOccurs="1" minOccurs="0"></element>
      <element name="jelszo" type="string" maxOccurs="1" minOccurs="0"></element>
      <element name="szamlaagentkulcs" type="string" maxOccurs="1" minOccurs="0"></element>      
      <element name="szamlaszam" type="string" maxOccurs="1" minOccurs="1"></element>
      <element name="valaszVerzio" type="int" maxOccurs="1" minOccurs="1"></element>
    </sequence>
  </complexType>
  <element name="xmlszamlapdf" type="tns:beallitasokTipus"></element>
</schema>
"""


# language=XSD
query_invoice_xml = """<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.szamlazz.hu/xmlszamlaxml" xmlns:tns="http://www.szamlazz.hu/xmlszamlaxml" elementFormDefault="qualified">
    <element name="xmlszamlaxml">
        <complexType>
            <sequence>
                <element name="felhasznalo" type="string" maxOccurs="1" minOccurs="0"></element>
                <element name="jelszo" type="string" maxOccurs="1" minOccurs="0"></element>
                <element name="szamlaagentkulcs" type="string" maxOccurs="1" minOccurs="0"></element>
                <element name="szamlaszam" type="string" maxOccurs="1" minOccurs="0"></element>
                <element name="rendelesSzam" type="string" maxOccurs="1" minOccurs="0"></element>
                <element name="pdf" type="boolean" maxOccurs="1" minOccurs="0"></element>
            </sequence>
        </complexType>
    </element>
</schema>"""


# language=XML
delete_pro_forma_invoice = """<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.szamlazz.hu/xmlszamladbkdel" xmlns:tns="http://www.szamlazz.hu/xmlszamladbkdel" elementFormDefault="qualified">
    <complexType name="beallitasokTipus">
        <sequence>
            <element name="felhasznalo" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="jelszo" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="szamlaagentkulcs" type="string" maxOccurs="1" minOccurs="0"></element>
        </sequence>
    </complexType>
    <complexType name="fejlecTipus">
        <sequence>
            <element name="szamlaszam" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="rendelesszam" type="string" maxOccurs="1" minOccurs="0"></element>
        </sequence>
    </complexType>
    <element name="xmlszamladbkdel">
      <complexType>
     <sequence>
        <element name="beallitasok" type="tns:beallitasokTipus" maxOccurs="1" minOccurs="1"></element>
        <element name="fejlec" type="tns:fejlecTipus" maxOccurs="1" minOccurs="1"></element>
     </sequence>
      </complexType>
    </element>
</schema>"""


# language=XML
generate_receipt = """<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.szamlazz.hu/xmlnyugtacreate" xmlns:tns="http://www.szamlazz.hu/xmlnyugtacreate" elementFormDefault="qualified">
    <complexType name="beallitasokTipus">
        <all>
            <element name="felhasznalo" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="jelszo" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="szamlaagentkulcs" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="pdfLetoltes" type="boolean" maxOccurs="1" minOccurs="1"></element>
        </all>
    </complexType>
    <complexType name="fejlecTipus">
        <all>
            <element name="hivasAzonosito" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="elotag" type="string" maxOccurs="1" minOccurs="1"></element>
            <element name="fizmod" type="string" maxOccurs="1" minOccurs="1"></element>
            <element name="penznem" type="string" maxOccurs="1" minOccurs="1"></element>
            <element name="devizaarf" type="double" maxOccurs="1" minOccurs="0"></element>
            <element name="devizabank" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="megjegyzes" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="pdfSablon" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="fokonyvVevo" type="string" maxOccurs="1" minOccurs="0"></element>
        </all>
    </complexType>
    <complexType name="tetelTipus">
        <all>
            <element name="megnevezes" type="string" maxOccurs="1" minOccurs="1"></element>
            <element name="azonosito" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="mennyiseg" type="double" maxOccurs="1" minOccurs="1"></element>
            <element name="mennyisegiEgyseg" type="string" maxOccurs="1" minOccurs="1"></element>
            <element name="nettoEgysegar" type="double" maxOccurs="1" minOccurs="1"></element>
            <element name="afakulcs" type="string" maxOccurs="1" minOccurs="1"></element>
            <element name="netto" type="double" maxOccurs="1" minOccurs="1"></element>
            <element name="afa" type="double" maxOccurs="1" minOccurs="1"></element>
            <element name="brutto" type="double" maxOccurs="1" minOccurs="1"></element>
            <element name="fokonyv" type="tns:tetelFokonyvTipus" maxOccurs="1" minOccurs="0"></element>
        </all>
    </complexType>
    <complexType name="tetelFokonyvTipus">
        <all>
            <element name="arbevetel" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="afa" type="string" maxOccurs="1" minOccurs="0"></element>
        </all>
    </complexType>
    <complexType name="tetelekTipus">
        <sequence>
            <element name="tetel" type="tns:tetelTipus" maxOccurs="unbounded" minOccurs="1"></element>
        </sequence>
    </complexType>
    <!-- jóváírások -->
    <complexType name="kifizetesTipus">
        <all>
            <element name="fizetoeszkoz" type="string" maxOccurs="1" minOccurs="1"></element>
            <element name="osszeg" type="double" maxOccurs="1" minOccurs="1"></element>
            <element name="leiras" type="string" maxOccurs="1" minOccurs="0"></element>
        </all>
    </complexType>
    <complexType name="kifizetesekTipus">
        <sequence>
            <element name="kifizetes"             type="tns:kifizetesTipus"   maxOccurs="unbounded" minOccurs="1"></element>
        </sequence>
    </complexType>
    <element name="xmlnyugtacreate">
        <complexType>
            <all>
                <element name="beallitasok" type="tns:beallitasokTipus" maxOccurs="1" minOccurs="1"></element>
                <element name="fejlec" type="tns:fejlecTipus" maxOccurs="1" minOccurs="1"></element>
                <element name="tetelek" type="tns:tetelekTipus" maxOccurs="1" minOccurs="1"></element>
                <element name="kifizetesek" type="tns:kifizetesekTipus" maxOccurs="1" minOccurs="0"></element>
            </all>
        </complexType>
    </element>
</schema>"""


# language=XML
reverse_receipt = """<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.szamlazz.hu/xmlnyugtast" xmlns:tns="http://www.szamlazz.hu/xmlnyugtast" elementFormDefault="qualified">
    <complexType name="beallitasokTipus">
        <sequence>
            <element name="felhasznalo" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="jelszo" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="szamlaagentkulcs" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="pdfLetoltes" type="boolean" maxOccurs="1" minOccurs="1"></element>
        </sequence>
    </complexType>
    <complexType name="fejlecTipus">
        <sequence>
            <element name="nyugtaszam" type="string" maxOccurs="1" minOccurs="1"></element>
            <element name="pdfSablon" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="hivasAzonosito" type="string" maxOccurs="1" minOccurs="0"></element>
        </sequence>
    </complexType>
    <element name="xmlnyugtast">
        <complexType>
            <sequence>
                <element name="beallitasok" type="tns:beallitasokTipus" maxOccurs="1" minOccurs="1"></element>
                <element name="fejlec" type="tns:fejlecTipus" maxOccurs="1" minOccurs="1"></element>
            </sequence>
        </complexType>
    </element>
</schema>"""


# language=XML
query_receipt = """<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.szamlazz.hu/xmlnyugtaget" xmlns:tns="http://www.szamlazz.hu/xmlnyugtaget" elementFormDefault="qualified">
    <complexType name="beallitasokTipus">
        <all>
            <element name="felhasznalo" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="jelszo" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="szamlaagentkulcs" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="pdfLetoltes" type="boolean" maxOccurs="1" minOccurs="1"></element>
        </all>
    </complexType>
    <complexType name="fejlecTipus">
        <all>
            <element name="nyugtaszam" type="string" maxOccurs="1" minOccurs="1"></element>
            <element name="hivasAzonosito" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="pdfSablon" type="string" maxOccurs="1" minOccurs="0"></element>
        </all>
    </complexType>
    <element name="xmlnyugtaget">
        <complexType>
            <all>
                <element name="beallitasok" type="tns:beallitasokTipus" maxOccurs="1" minOccurs="1"></element>
                <element name="fejlec" type="tns:fejlecTipus" maxOccurs="1" minOccurs="1"></element>
            </all>
        </complexType>
    </element>
</schema>"""


# language=XML
send_receipt = """<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.szamlazz.hu/xmlnyugtasend" xmlns:tns="http://www.szamlazz.hu/xmlnyugtasend" elementFormDefault="qualified">
    <complexType name="beallitasokTipus">
        <sequence>
            <element name="felhasznalo" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="jelszo" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="szamlaagentkulcs" type="string" maxOccurs="1" minOccurs="0"></element>
        </sequence>
    </complexType>
    <complexType name="fejlecTipus">
        <sequence>
            <element name="nyugtaszam" type="string" maxOccurs="1" minOccurs="1"></element>
        </sequence>
    </complexType>
    <complexType name="emailKuldes">
        <sequence>
            <element name="email" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="emailReplyto" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="emailTargy" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="emailSzoveg" type="string" maxOccurs="1" minOccurs="0"></element>
        </sequence>
    </complexType>
    <element name="xmlnyugtasend">
        <complexType>
            <sequence>
                <element name="beallitasok" type="tns:beallitasokTipus" maxOccurs="1" minOccurs="1"></element>
                <element name="fejlec" type="tns:fejlecTipus" maxOccurs="1" minOccurs="1"></element>
                <element name="emailKuldes" type="tns:emailKuldes" maxOccurs="1" minOccurs="0"></element>
            </sequence>
        </complexType>
    </element>
</schema>"""


# language=XML
tax_payer = """<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.szamlazz.hu/xmltaxpayer" xmlns:tns="http://www.szamlazz.hu/xmltaxpayer" elementFormDefault="qualified">
    <complexType name="beallitasokTipus">
        <sequence>
            <element name="felhasznalo" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="jelszo" type="string" maxOccurs="1" minOccurs="0"></element>
            <element name="szamlaagentkulcs" type="string" maxOccurs="1" minOccurs="0"></element>
        </sequence>
    </complexType>
    <simpleType name="torszszamTipus">
        <restriction base="string">
            <length value="8" />
            <pattern value="[0-9]{8}" />
        </restriction>
    </simpleType>
    <element name="xmltaxpayer">
        <complexType>
            <sequence>
                <element name="beallitasok" type="tns:beallitasokTipus" maxOccurs="1" minOccurs="1"></element>
                <element name="torzsszam" type="tns:torszszamTipus" maxOccurs="1" minOccurs="1"></element>
            </sequence>
        </complexType>
    </element>
</schema>"""
