$(document).ready(function() {
	var $edit = $("#edit"),
        $save = $("#save_edit"),
        $cancel =  $("#cancel"),
	    $inputs = $('input:disabled'),
        name = $('#member_name').text(),
        ori = {};

	$save.hide();
	$cancel.hide();
	loadValidation();

    $inputs.each(function(index, ele) {
        var $input = $(ele),
            field = $input.attr('name');

        ori[field] = $input.val();
    });

    $inputs.on('keyup', function(evt) {
        var $input = $(evt.target),
			field = $input.attr('name');

        if (['tel_hp', 'tel_o', 'tel_h', 'tel_fax'].indexOf(field) === -1) {
            $input.val($input.val().toUpperCase());
        }
    });

    $edit.on("click", function(e) {
        e.preventDefault();
        $save.show();
        $cancel.show();
        $edit.hide();
        $inputs.removeAttr('disabled');
    });

    $save.on("click", function(e) {
        var data = {};

        data = packingFunction(data, $inputs);
        data['name'] = name;
        e.preventDefault();

        console.log(data);
        res = window.erpx.call_method(
                'namlifa_portal.namlifa_members.doctype.namlifa_member.namlifa_member.member_update',
                'Namlifa Member',
                data
            )
            .then(function (res) {
                console.log(res);
                $save.hide();
                $cancel.hide();
                $edit.show();
                window.erpx.showMessage("<p>Changes is saved successfully!</p>");
            });
    });

    $cancel.on("click", function(e) {
        e.preventDefault();
        $save.hide();
        $cancel.hide();
        $edit.show();

        //reset back the inputs
        $inputs.each(function(index, ele) {
            if (ori[ele.name]) {
                $(ele).val(ori[ele.name]);
            }
        });

        $inputs.prop('disabled', true);
    });

});

function loadValidation() {
    var $cell_number = $('input[name="tel_hp"]'),
			$office_number = $('input[name="tel_o"]'),
			$house_number = $('input[name="tel_h"]'),
			$fax_number = $('input[name="tel_fax"]');

		if ($cell_number[0]) {
			IMask($cell_number[0], {
				mask: '{6\\0}0000000000'
			});
		}

		if ($office_number[0]) {
			IMask($office_number[0], {
				mask: '{6\\0}0000000000'
			});
		}

		if ($house_number[0]) {
			IMask($house_number[0], {
				mask: '{6\\0}0000000000'
			});
		}

		if ($fax_number[0]) {
			IMask($fax_number[0], {
				mask: '{6\\0}0000000000'
			});
		}
}

const packingFunction = (data, $inputs) => {
    var dat = {};

    $inputs.each(function(index, ele) {
        var $input = $(ele),
            field = $input.attr('name');

        dat[field] = $input.val();
    });

    return dat;
};