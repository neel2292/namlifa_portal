// Copyright (c) 2020, ERP-X and contributors
// For license information, please see license.txt


frappe.ui.form.on('Namlifa Member', {
	"onload" : function(frm) {
		imasking('new_nric_no', ic_number);
        imasking('tel_hp', cell_number);
        imasking('tel_o', cell_number);
        imasking('tel_h', cell_number);
        imasking('tel_fax', cell_number);
        imasking('date_contracted_as_agent', month_year);
        imasking('join_date', date);
    },
    "refresh": function(frm) {
        upperCase();
	},
    "application_status": function(frm) {
          if (frm.doc.application_status == 'Rejected') { frm.set_value('membership_no', 'REJECTED-' + frm.docname); }
    }



});

frappe.ui.form.on('Namlifa Member Payment', {
	form_render: function(frm) {
	    imasking('credit_card_no', card_no, true);
	    upperCase();
	},
});