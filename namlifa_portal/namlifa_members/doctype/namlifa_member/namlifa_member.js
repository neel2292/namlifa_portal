// Copyright (c) 2020, ERP-X and contributors
// For license information, please see license.txt


frappe.ui.form.on('Namlifa Member', {
	// refresh: function(frm) {

	// }

	"new_nric_no" : function(frm) {
	
		console.log('hijuju')
		loadScript('https://unpkg.com/imask').then(function () {

			var $nric_input = $('input[data-fieldname="new_nric_no"]')
			if ($nric_input[0]) {
                        	IMask($nric_input[0], {
				mask: '000000-00-0000'
                        });
                }
	        });
	



	}
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

