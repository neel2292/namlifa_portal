// Copyright (c) 2020, ERP-X and contributors
// For license information, please see license.txt

frappe.ui.form.on('Namlifa Akard Membership', {
        refresh: function(frm) {
        $('input[data-fieldname][type="text"], textarea[data-fieldname][type="text"]').each(function() {
            var $me = $(this),
                BLACKLIST = ['email', 'new_nric_no', 'tel_hp', 'user_id'];

            if (BLACKLIST.indexOf($me.attr('data-fieldname')) === -1) {
                $me.on('keyup', function() {
                    $me.val($me.val().toUpperCase());
                });
            }
        });
        },
});
