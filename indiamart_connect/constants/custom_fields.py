import frappe

CUSTOM_FIELDS = {
    "Lead": [
        {
            "fieldname": "indiamart_query_id",
            "label": "IndiaMART Query Id",
            "fieldtype": "Data",
            "options": "",
            "insert_after": "request_type",
            "print_hide": 1,
            "read_only": 1,
            "translatable": 0,
        }
    ]
}
