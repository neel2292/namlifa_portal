// Copyright (c) 2020, ERP-X and contributors
// For license information, please see license.txt

frappe.ui.form.on('Namlifa Akard', {
    "onload" : function(frm) {
        imasking('expiry_date', month_year);
        imasking('card_no', card_no);
        imasking('received_date', date);
        imasking('date', date);
    },
	refresh: function(frm) {
       upperCase();
	},
    fee: function (frm) {
        count_total_fee(frm);
    },
    member_fee: function (frm) {
        count_total_fee(frm);
    },
    akard_builders_award_fee: function (frm) {
        count_total_fee(frm);
    },
    late_fee: function (frm) {
        count_total_fee(frm);
    }
});

frappe.ui.form.on('Namlifa Akard Builder', {
	refresh: function(frm) {
       upperCase();
	},
});

frappe.ui.form.on('Namlifa Akard Membership', {
	refresh: function(frm) {
        upperCase();
	},
});

frappe.ui.form.on('Namlifa Akard Plan', {
	refresh: function(frm) {
       upperCase();
	},
});

var count_total_fee = function(frm){
    let fee = flt(frm.doc.fee);
    let member_fee = flt(frm.doc.member_fee);
    let akard_builders_award_fee = flt(frm.doc.akard_builders_award_fee);
    let late_fee = flt(frm.doc.late_fee);

    let total_fee = fee + member_fee + akard_builders_award_fee + late_fee
    frm.set_value("total_fee",total_fee)
}


