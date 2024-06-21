__all__ = ["generate_invoice", "reverse_invoice", "credit_entry", "generate_proforma_invoice"]


# language=XML
generate_invoice: str = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
  <companyVatCode>{{ merchant.VAT }}</companyVatCode>
  <client>
    <name>{{ buyer.name }}</name>
    <vatCode>{{ buyer.tax_number_eu }}</vatCode>
    <regCom>{{ buyer.tax_number}}</regCom>
    <address>{{ buyer.address }}</address>
    <isTaxPayer>false</isTaxPayer>
    <city>{{ buyer.city }}</city>
    <county>{{ buyer.county }}</county>
    <country>{{ buyer.country }}</country>
    <saveToDb>false</saveToDb>
  </client>
  <isDraft>false</isDraft>
  <issueDate>{{ header.creating_date }}</issueDate>
  <seriesName>{{ header.invoice_prefix }}</seriesName>
  <currency>{{ header.currency }}</currency>
  <exchangeRate>{{ header.exchange_rate }}</exchangeRate>
  <language>{{ header.language }}</language>
  <precision>3</precision>
  <dueDate>{{ header.due_date }}</dueDate>
  <useEstimateDetails>{{ header.use_estimate }}</useEstimateDetails>
  {%- if header.use_estimate == 'true' %}
  <estimate>
    <seriesName>{{ header.pro_forma_serie_ref }}</seriesName>
    <number>{{ header.pro_forma_number_ref }}</number>
  </estimate>
  {% endif -%}
  {%- if False %}
  <payment>
    <value>100</value>
    <type>Ordin plata</type>
    <isCash>false</isCash>
  </payment>
  {% endif -%}
  {%- for item in items %}
  <product>
    <name>{{ item.name }}</name>
  {%- if item.isdiscount == 'false' %}
    <code>ccd1</code>
  {% endif -%}
      
  {%- if False %}
    <productDescription>produse de papetarie</productDescription>
  {% endif -%}
    <isDiscount>{{item.isdiscount}}</isDiscount>
  {%- if item.isdiscount == 'true' %}
    <numberOfItems>{{item.quantity}}</numberOfItems>
  {% endif -%}
    <measuringUnitName>{{item.quantity_unit}}</measuringUnitName>
    <currency>{{ header.currency }}</currency>
  {%- if item.isdiscount == 'false' %}
    <quantity>{{item.quantity}}</quantity>
  {% endif -%}
  {%- if item.isdiscount == 'false' %}
    <price>{{item.unit_price}}</price>
  {% endif -%}
    <isTaxIncluded>false</isTaxIncluded>
    <taxName>{{item.vat_name}}</taxName>
    <taxPercentage>{{item.vat_rate}}</taxPercentage>
  {%- if item.isdiscount == 'false' %}
    <saveToDb>false</saveToDb>
    <isService>true</isService>
  {% endif -%}
  {%- if item.isdiscount == 'true' %}
    <discountType>{{item.discount_type}}</discountType>
    <discountPercentage>{{item.discount_percentage}}</discountPercentage>
  {% endif -%}

  </product>
  {% endfor -%}
</invoice>
"""

# language=XML
generate_proforma_invoice: str = """<?xml version="1.0" encoding="UTF-8"?>
<estimate>
  <companyVatCode>{{ merchant.VAT }}</companyVatCode>
  <client>
    <name>{{ buyer.name }}</name>
    <vatCode>{{ buyer.tax_number_eu }}</vatCode>
    <regCom>{{ buyer.tax_number}}</regCom>
    <isTaxPayer>false</isTaxPayer>
    <address>{{ buyer.address }}</address>
    <city>{{ buyer.city }}</city>
    <county>{{ buyer.county }}</county>
    <country>{{ buyer.country }}</country>
    <saveToDb>false</saveToDb>
  </client>
  <issueDate>{{ header.creating_date }}</issueDate>
  <seriesName>{{ header.invoice_prefix }}</seriesName>
  <currency>{{ header.currency }}</currency>
  <exchangeRate>{{ header.exchange_rate }}</exchangeRate>
  <language>{{ header.language }}</language>
  <precision>3</precision>
  <dueDate>{{ header.due_date }}</dueDate>
  {%- for item in items %}
  <product>
    <name>{{ item.name }}</name>
  {%- if item.isdiscount == 'false' %}
    <code>ccd1</code>
  {% endif -%}
      
  {%- if False %}
    <productDescription>produse de papetarie</productDescription>
  {% endif -%}
    <isDiscount>{{item.isdiscount}}</isDiscount>
  {%- if item.isdiscount == 'true' %}
    <numberOfItems>{{item.quantity}}</numberOfItems>
  {% endif -%}
    <measuringUnitName>{{item.quantity_unit}}</measuringUnitName>
    <currency>{{ header.currency }}</currency>
  {%- if item.isdiscount == 'false' %}
    <quantity>{{item.quantity}}</quantity>
  {% endif -%}
  {%- if item.isdiscount == 'false' %}
    <price>{{item.unit_price}}</price>
  {% endif -%}
    <isTaxIncluded>false</isTaxIncluded>
    <taxName>{{item.vat_name}}</taxName>
    <taxPercentage>{{item.vat_rate}}</taxPercentage>
  {%- if item.isdiscount == 'false' %}
    <saveToDb>false</saveToDb>
    <isService>true</isService>
  {% endif -%}
  {%- if item.isdiscount == 'true' %}
    <discountType>{{item.discount_type}}</discountType>
    <discountPercentage>{{item.discount_percentage}}</discountPercentage>
  {% endif -%}

  </product>
  {% endfor -%}
</estimate>"""


# language=XML
reverse_invoice: str = """<?xml version="1.0" encoding="UTF-8"?>
<invoice>
    <companyVatCode>{{ merchant.VAT }}</companyVatCode>
    <seriesName>{{ header.invoice_prefix }}</seriesName>
    <number>{{ header.invoice_number }}</number>
    <issueDate>{{ header.creating_date }}</issueDate>
</invoice>
"""

# language=XML
credit_entry: str = """

"""

# language=XML
cancel_invoice: str = """

"""
