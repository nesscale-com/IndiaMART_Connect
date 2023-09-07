import frappe
from frappe.custom.doctype.custom_field.custom_field import (
    create_custom_fields as _create_custom_fields,
)
from sanad.constants.custom_fields import CUSTOM_FIELDS


def after_install():
    create_custom_fields()
    create_lead_source()


def create_custom_fields():
    print("Creating custom fields")
    _create_custom_fields(get_all_custom_fields(), ignore_validate=True)
    print("Custom fields added")


def get_all_custom_fields():
    result = {}

    # for custom_fields in CUSTOM_FIELDS:
    for doctypes, fields in CUSTOM_FIELDS.items():
        if isinstance(fields, dict):
            fields = [fields]

        result.setdefault(doctypes, []).extend(fields)
    return result


def create_lead_source():
    if not frappe.db.exists("Lead Source", "IndiaMART"):
        frappe.get_doc(dict(doctype="Lead Source", source_name="IndiaMART")).insert(
            ignore_permissions=True
        )
