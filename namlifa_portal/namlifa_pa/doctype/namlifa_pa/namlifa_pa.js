// Copyright (c) 2020, ERP-X and contributors
// For license information, please see license.txt
//

frappe.ui.form.on('Namlifa PA', {
        "onload" : function(frm) {
                loadScript('https://unpkg.com/imask').then(function () {
                        var $nric_input = $('input[data-fieldname="ic_number"]'),
                            $cell_number = $('input[data-fieldname="contact_number"]');

                        IMask($nric_input[0], {
                                mask: '000000\-00\-0000'
                        });

                        IMask($cell_number[0], {
                                mask: '{6\\0}00 000 00000'
                        });
                });
        },


        ic_number : function (frm) {
                frappe.call({
                        method: "namlifa_portal.namlifa_members.doctype.namlifa_member.namlifa_member.validate_new_nric_no",    
                        args: {
                                new_nric_no: frm.doc.ic_number
                        },
                        callback: function(r) {
                                if (!r.message){
                                        frappe.throw(__("Invalid value for NRIC number"));
                                }       
                        }
                });
        },

        contact_number : function (frm) {
                frappe.call({
                        method: "namlifa_portal.namlifa_members.doctype.namlifa_member.namlifa_member.validate_tel_hp",     
                        args: {
                                tel_hp: frm.doc.contact_number
                        },
                        callback: function(r) {
                                if (!r.message){
                                        frappe.throw(__("Invalid value for Mobile number"));
                                }
                        }
                });
        },

});


function loadScript(url){
    var script = document.createElement("script")
    script.type = "text/javascript";

    return new Promise(function (resolve) {
        if (script.readyState){  //IE
            script.onreadystatechange = function(){
                if (script.readyState == "loaded" || script.readyState == "complete"){
                    script.onreadystatechange = null;
                    resolve();
                }
            };
        } else {  //Others
            script.onload = resolve;
        }

        script.src = url;
        document.getElementsByTagName("head")[0].appendChild(script);
    });
}

