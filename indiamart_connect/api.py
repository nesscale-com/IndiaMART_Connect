import frappe
from frappe.integrations.utils import create_request_log, make_get_request


@frappe.whitelist()
def get_leads():
    url = "https://mapi.indiamart.com/wservce/crm/crmListing/v2/?glusr_crm_key=mR26E7hr5HjCSfet5XaM7liPpFvDlDRiVA==&start_time=04-08-2023&end_time=06-08-2023"
    indiamart_leads = make_get_request(url)
    frappe.log_error(title="9",message=indiamart_leads)
    frappe.log_error(title="9",message=type(indiamart_leads))

    if indiamart_leads.get("STATUS") == "SUCCESS":
        frappe.log_error(title="indiamart",message=indiamart_leads.get("RESPONSE"))
        create_request_log(data={},integration_type="IndiaMART",url=url,output=indiamart_leads.get("RESPONSE"),status="Completed")
    else:
        create_request_log(data={},integration_type="IndiaMART",url=url,error=indiamart_leads.get("RESPONSE"),status="Failed")