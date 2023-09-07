import frappe
from indiamart_connect.api import get_india_mart_leads


def fetch_india_mart_leads(from_date, to_date):
    india_mart_leads = get_india_mart_leads(from_date, to_date)
