console.log('TH');

frappe.ui.form.on('Namlifa Training History', {
        "onload" : function(frm) {
    		imasking('new_nric_no', ic_number);
    		imasking('tel_hp', cell_number);
        },
        "refresh" : function(frm) {
                upperCase();
        },
})

frappe.ui.form.on('Namlifa CPD Workshop Programme', {
        "form_render" : function(frm) {
                upperCase();
        },
})

