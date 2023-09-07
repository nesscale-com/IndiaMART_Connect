import frappe
from frappe.utils import now_datetime, format_datetime, add_to_date
from frappe.integrations.utils import make_get_request
import json
from frappe import _


def get_india_mart_leads(from_datetime, to_datetime):
    india_mart_url = get_india_mart_url()
    # from_datetime = format_datetime(from_datetime, "dd-mm-yyyy hh:mm:ss")
    # to_datetime = format_datetime(to_datetime, "dd-mm-yyyy hh:mm:ss")
    india_mart_url = (
        f"{india_mart_url}&start_time={from_datetime}&end_time={to_datetime}"
    )
    results = make_get_request(india_mart_url)
    create_india_mart_logs(india_mart_url, results)
    frappe.db.commit()
    if results.get("CODE") == 200:
        create_india_mart_leads(results.get("RESPONSE"))
        update_last_fetch_time(to_datetime)


def get_india_mart_url():
    settings = frappe.get_doc("IndiaMART Settings", "IndiaMART Settings")
    return f"{settings.get('url')}?glusr_crm_key={settings.get_password('api_key')}"


def update_last_fetch_time(to_datetime):
    frappe.db.set_value(
        "IndiaMART Settings",
        "IndiaMART Settings",
        "last_fetch_updated_time",
        to_datetime,
    )


def create_india_mart_logs(url, results):
    frappe.get_doc(
        dict(
            doctype="IndiaMART API Logs",
            url=url,
            datetime=now_datetime(),
            status=results.get("STATUS"),
            failure_message=results.get("MESSAGE"),
            response=json.dumps(results.get("RESPONSE")),
        )
    ).insert(ignore_permissions=True)


def create_india_mart_leads(leads):
    for lead in leads:
        for key, value in lead.items():
            lead_data = {}
            if not frappe.db.exists("IndiaMART Query", value):
                lead_query_doc = frappe.new_doc("IndiaMART Query")
                lead_data[frappe.scrub(key)] = value
                lead_query_doc.update(lead_data)
                lead_query_doc.insert(ignore_permissions=True)


def india_mart_cron_job():
    from_time = frappe.db.get_value(
        "IndiaMART Settings", "IndiaMART Settings", "last_fetch_updated_time"
    )
    to_time = now_datetime()
    get_india_mart_leads(from_time, to_time)


@frappe.whitelist()
def india_mart_manually_sync():
    from_datetime = frappe.db.get_value(
        "IndiaMART Settings", "IndiaMART Settings", "last_fetch_updated_time"
    )
    if not from_datetime:
        frappe.throw(_("Last sync fetch time required to manually sync"))
    to_datetime = now_datetime()
    get_india_mart_leads(from_datetime, to_datetime)
    frappe.msgprint(_("Lead sync for IndiaMART added to the queue"))
