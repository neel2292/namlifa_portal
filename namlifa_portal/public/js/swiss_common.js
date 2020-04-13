function hihihi() {
	console.log('hihihih');
}

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


function upperCase(){
	$('input[data-fieldname][type="text"], textarea[data-fieldname][type="text"]').each(function() {
		var $me = $(this),
			BLACKLIST = ['email', 'new_nric_no', 'tel_hp', 'user_id'];

		if (BLACKLIST.indexOf($me.attr('data-fieldname')) === -1) {
			$me.on('keyup', function() {
				$me.val($me.val().toUpperCase());
			});
		}
	});
}

var ic_number = '000000\-00\-0000',
    date = '00-00-0000',
	month_year = '00/0000'
    card_no = '0000 0000 0000 0000',
    cell_number = '{6\\0}0000000000';

function imasking(fieldname, mask_type, table=false){
	loadScript('https://unpkg.com/imask').then(function () {
		if (table) {
			var $form = $('.grid-row-open'),
			    $field = $form.find('input[data-fieldname="' + fieldname + '"]');
		} else {
			var $field = $('input[data-fieldname="' + fieldname + '"]');

		};

		IMask($field[0], {
			mask: mask_type
		});
	});

}

function upperNamlifa(){
	var $text_ele = $('div.ellipsis.title-text:last');
	$text_ele.text($text_ele.text().replace('Namlifa', 'NAMLIFA'));
}
