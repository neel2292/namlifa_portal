$(document).ready(function() {
	var $save = $("#save_edit"),
    $inputs = $('input'),
    $hint = $('.form-hint'),
    args = {};

  $('.update-form').on('submit', function (e) {
    var empty = false;

    $hint.text('');
    e.preventDefault();
    $inputs.each(function(index, ele) {
        var $input = $(ele),
            val = $input.val(),
            field = $input.attr('name');

        args[field] = val;
        if (!val) { $input.addClass('invalid'); }
        else { $input.removeClass('invalid'); }
        if (!empty && val === '') { empty = true; }
    });

    if (!empty) {
      if (args.old_password == args.new_password) {
        $hint.text('New password is same as old password!');
        $('#new-password').addClass('invalid');
      }
      else if (args.new_password != args.confirm_password) {
        $hint.text('Confirm password does not match new password!');
        $('#confirm-password').addClass('invalid');
      }
      else {
        $save.attr('disabled', true);
        window.erpx.call_method(
            'namlifa_portal.namlifa_members.doctype.namlifa_member.namlifa_member.update_password',
            'Namlifa Member',
            args
        ).then(function (res) {
            $save.attr('disabled', false);
            if (res && res.message) {
              if (res.message.error) {
                if (res.message.wrong_password) {
                  $('#old-password').addClass('invalid');
                }
                else {
                  $('#new-password').addClass('invalid');
                  $('#confirm-password').addClass('invalid');
                }
                $hint.text(res.message.text);
              }
              else {
                window.erpx.showMessage('<p>' + res.message.text + '</p>');
                $inputs.val('');
              }
            }
            else {
              $hint.text('<p>Something went wrong. Please try again.</p>');
            }
        }).catch(function (error) {
          console.log(error);
        });
      }
    }
    else {
      $hint.text('Please fill in the form!')
    }

    return false;
  });

});
