// Copyright (c) 2023, Nesscale Solutions Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('IndiaMART Settings', {
	fetch_now: function(frm) {
		frappe.call({
			method:"indiamart_connect.api.india_mart_api.india_mart_manually_sync",
			args:{},
			callback:function(r){
				
			}
		})
	}
});
