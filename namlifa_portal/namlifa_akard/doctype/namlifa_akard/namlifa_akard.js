// Copyright (c) 2020, ERP-X and contributors
// For license information, please see license.txt

frappe.ui.form.on('Namlifa Akard', {
	// refresh: function(frm) {

	// }
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

var count_total_fee = function(frm){
    let fee = flt(frm.doc.fee);
    let member_fee = flt(frm.doc.member_fee);
    let akard_builders_award_fee = flt(frm.doc.akard_builders_award_fee);
    let late_fee = flt(frm.doc.late_fee);

    let total_fee = fee + member_fee + akard_builders_award_fee + late_fee
    frm.set_value("total_fee",total_fee)
}
