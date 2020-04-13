
frappe.ui.form.on('Namlifa PA', {
        "onload" : function(frm) {
            imasking('ic_number', ic_number);
            imasking('contact_number', cell_number);
        },
        "refresh" : function(frm) {
            upperCase();
        },
})


frappe.ui.form.on('Namlifa PA Spouse', {
	"form_render" : function(frm) {
	    imasking('new_nric_no', ic_number, true);
        imasking('contact_number', cell_number, true);
		upperCase();
	},
})

frappe.ui.form.on('Namlifa PA Nomination', {
	"form_render" : function(frm) {
	    imasking('new_nric_no', ic_number, true);
        imasking('contact_number', cell_number, true);
		upperCase();
	},
})

