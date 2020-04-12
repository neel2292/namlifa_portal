console.log('PI');

frappe.ui.form.on('Namlifa PI', {
        "onload" : function(frm) {
    		imasking('new_nric_no', ic_number);
    		imasking('tel_hp', cell_number);
    		imasking('tel_o', cell_number);
    		imasking('pi_joined_since', date);
    		imasking('credit_card_no', card_no);
        },
        "refresh" : function(frm) {
                upperCase();
        },
})

