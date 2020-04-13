$(document).ready(function() {
    // var elems = document.querySelectorAll('.datepicker');
    // var instances = M.Datepicker.init(elems, {format: 'dd/mm/yyyy'});
    // var agent_date = document.querySelectorAll('#date_contracted_as_agent');
    // var agent_date_instance = M.Datepicker.init(agent_date, {format: 'mm/yyyy'});
    var signatures = {};
    var photo, receipt;
    var $inputs = $('input[name], textarea[name]');

    $inputs.on('keyup', function(evt) {
        var $input = $(evt.target),
			field = $input.attr('name');

        if (['tel_hp', 'tel_o', 'tel_h', 'tel_fax', 'new_nric_no', 'email', 'date_contracted_as_agent'].indexOf(field) === -1) {
            $input.val($input.val().toUpperCase());
        }
    });

    //mobile view remove materialize select and use native select
    // console.log(window.outerWidth);
    // if (window.outerWidth < 601) {
    //     var $material_select = $('.select-wrapper'),
    //         $select = $('select');
    //
    //     $material_select.remove();
    //     $.each($select, function (key, ele) {
    //         var $ele = $(ele),
    //             $parent = $ele.closest('.input-field'),
    //             $label = $parent.find('label');
    //
    //         $label.css('position', 'static');
    //     });
	// }
    // else { // non-mobile view remove native select
    //     $('.browser-default').remove();
    // }

    loadSignPad();
    // $('.jSignature').addClass('border-blue-sign');

    var validation = {
        new_nric_no: function (val) {
            var match,
                dob = '';

            if (/\d{6}-\d{2}-\d{4}/.test(val)) {
                match = val.slice(0, 6).match(/.{2}/g).reverse();
                dob = match[0] + '/' + match[1] + '/' + (parseInt(match[2]) > 40 ? '19' + match[2] : '20' + match[2]); // limitation: can handle up to 2040 only
                $('#date_of_birth').val(dob);
                return true;
            }
            else { return 'Invalid value for NRIC number' }
        },
        full_name: function (val) {
          if (val !== '') {
              $('#card_owner_name').val(val);
              $('#renewal_name').val(val);
              return true;
          }
          else { return 'Name cannot be empty'}
        },
        company: function (val) {
           if (val !== '') {
               $('#renewal_company').val(val);
               return true;
           }
           else { return 'Name cannot be empty'}
       },
        tel_hp: function (val) {
            if (/60\d{9,}/.test(val)) {
                return true;
            }
            else { return 'Invalid value for Mobile number' }
        },
        tel_o: function (val) {
            if (/60\d{9,}/.test(val)) {
                return true;
            }
            else { return 'Invalid value for Office number' }
        },
        tel_h: function (val) {
            if (/60\d{9,}/.test(val)) {
                return true;
            }
            else { return 'Invalid value for House number' }
        },
        tel_fax: function (val) {
            if (/60\d{9,}/.test(val)) {
                return true;
            }
            else { return 'Invalid value for Fax number' }
        },
        email: function (val) {
            if (/.+@.+\..+/.test(val)) {
                return true;
            }
            else { return 'Invalid value for email' }
        },
        date_contracted_as_agent: function (val) {
            var match,
                date = '';

            if (/\d{2,}\/\d{4,}/.test(val)) {
                return true;
            }
            else { return 'Invalid value for date contracted as Agent number' }
        },
        agents_code: function (val) {
            if (val !== '') {
                return true;
            }
            else { return false; }
        }
    };

	$('body').focusout(function (evt) {
		var $input = $(evt.target),
			field = $input.attr('name'),
			valid,
            BLACKLIST = ['new_nric_no', 'full_name', 'tel_hp', 'email', 'date_contracted_as_agent', 'agents_code'];

		if (validation[field]) {
			valid = validation[field]($input.val(), $input);
			if (valid !== true && BLACKLIST.indexOf(field) > -1) {
				$input.addClass('invalid');
			}
		}
    });

    $("#submitApplication").on("click", function(e) {
        var $invalid = $('.invalid'),
            errLine,
            data = {},
            elements,
            res;

        $(e.target).prop('disabled', true);
        e.preventDefault();
        if ($invalid.length) {
            console.log($invalid);
            errLine = "<p>Field  <strong style='font-weight: bold'>"+ $($invalid[0]).closest('div').find('label').text() +"</strong> is not a valid value. Please check.</p>";

            window.erpx.showError(errLine);
            $(e.target).prop('disabled', false);
        }
        else if (Object.keys(signatures).length !== 2) {
            errLine = "<p>Plese sign on signature fields</p>";

            window.erpx.showError(errLine);
            $(e.target).prop('disabled', false);
        }
        else {
            elements = [].slice.call(document.forms[0].elements);
            data = packingFunction(data, elements);
            data['photo'] = photo;
            data['receipt'] = receipt;
            data['terms_signature'] = signatures['terms_signature'];
            data['payment_signature'] = signatures['payment_signature'];

            res = window.erpx.call_method(
                'namlifa_portal.namlifa_members.doctype.namlifa_member.namlifa_member.registered',
                'Namlifa Member',
                data
            )
            .then(function (res) {
                console.log(res);
                if (Object.keys(res).length > 0) {
                     window.erpx.showMessage("<p>There is already an account registered using  <strong style='font-weight: bold'>" + data['email'] + "</strong> </p>");
                     $(e.target).prop('disabled', false);
                }
                else {
                    res2 = window.erpx.call_method(
                        'namlifa_portal.namlifa_members.doctype.namlifa_member.namlifa_member.member_registration',
                        'Namlifa Member', data).then(function (res) {
                        console.log(res);
                        window.erpx.showMessage("<p>Thank you for your application</p>" +
                            "<p>We will send you the login credential to your email " + data['email']+ " once has been approved</p>" +
                            "<p>You will be redirected in <span id=\"countdown\">5</span> seconds</p>"
                        );

                        var count = 5;
                        var interval = setInterval(function() {
                          count--;
                          $('#countdown').text(count);
                          if (count == 0) {
                            clearInterval(interval);
                            // redirect to home page
                            window.location.replace(window.location.origin);
                          }
                        }, 1000);
                    });
                }
            });
        }
    });

    $("#photo").on("change", function() {
        photoFileURL(this, "#photoPreview");
    });

    $("#receipt").on("change", function() {
        receiptFileURL(this, "#receiptPreview");
    });

    // $(document).on("keyup", ".cnf", function() {
    //     var strval = this.value;
    //     if(strval === "603") {
    //         this.value = "603-";
    //     } else if(strval === "6021") {
    //         this.value = "6021-";
    //     }
    // });
    //
    // $("#new_nric_no").on("keyup", function() {
    //     //XXXXXX-XX-XXXX
    //     var strval = this.value;
    //     if (strval.length == 6 || strval.length == 9) {
    //         this.value = strval+"-";
    //     }
    // });
    //
    // $("#new_nric_no").on("change", function() {
    //     var strval = this.value;
    //     if (strval.length == 12) {
    //         this.value = strval.substr(0, 7) + "-" + strval.substr(7, 9) + "-" + strval.substr(9);
    //     }
    // });

    function loadSignPad() {
        setTimeout(() => {
            signPadLoaded = true;
            $(".signature-widget").empty();
            $(".signature-widget").jSignature().bind('change', function(e){
                var $target = $(e.target),
                    base64_img = $target.jSignature("getData"),
                    id = $target.attr('id'),
                    signFile = dataURLtoFile(base64_img, id + '.png');

                signatures[id] = {
                    img: base64_img
                };
            });

            $(".reset-signature").on("click", function(e){
                var $target = $(e.target),
                    id = $target.attr('id');

                $target.parent('p').next('.signature-widget').jSignature('reset');
                delete signatures[id];
                //$("#signatureWidget").jSignature("reset");
            });
        }, 200);
    }

    function photoFileURL(input, imgId) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function(e) {
                var file = dataURLtoFile(e.target.result, 'photo_image');

                console.log(e);

                $(imgId).attr('src', e.target.result);
                photo = e.target.result;
            };

            reader.readAsDataURL(input.files[0]);
        }
    }

    function receiptFileURL(input, imgId) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function(e) {
                var file = dataURLtoFile(e.target.result, 'photo_image');

                console.log(e);

                $(imgId).attr('src', e.target.result);
                receipt = e.target.result;
            };

            reader.readAsDataURL(input.files[0]);
        }
    }
});

function dataURLtoFile(dataurl, filename) {
    try{
      var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
          bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
      while(n--){
          u8arr[n] = bstr.charCodeAt(n);
      }
      return new File([u8arr], filename, {type:mime});
    }catch(error){
      try{
        var blobObject = new Blob([u8arr], {type: 'mime'});
        return "";
      }catch(error){
        return "";
      }
    }
}

const packingFunction = (data, elements) => {
    elements.map(function(x){
        if(x.name) data[x.name] = x.value;
    });
    return data;
};