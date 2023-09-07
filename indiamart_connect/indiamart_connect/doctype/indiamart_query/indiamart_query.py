# Copyright (c) 2023, Nesscale Solutions Private Limited and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class IndiaMARTQuery(Document):
    def after_insert(self):
        self.create_lead()

    def create_lead(self):
        lead_doc = frappe.get_doc(
            dict(
                doctype="Lead",
                indiamart_query_id=self.name,
                first_name=self.sender_name,
                source="IndiaMART",
                email_id=self.sender_email,
                mobile_no=self.sender_mobile,
                phone=self.sender_mobile_alt,
                company_name=self.sender_company,
                notes=[dict(note=self.get("query_message"))],
            )
        ).insert(ignore_permissions=True)
