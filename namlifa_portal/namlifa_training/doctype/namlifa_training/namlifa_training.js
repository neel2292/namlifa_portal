// Copyright (c) 2020, ERP-X and contributors
// For license information, please see license.txt

frappe.ui.form.on('Namlifa Training', {
    onload: function(frm) {
        loadScript('https://unpkg.com/imask').then(function () {
			var $nric_input = $('input[data-fieldname="new_nric_no"]'),
			    $cell_number = $('input[data-fieldname="tel_hp"]');

			IMask($nric_input[0], {
				mask: '000000\-00\-0000'
			});

			IMask($cell_number[0], {
				mask: '{6\\0}0000000000'
			});
        });
    },
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
