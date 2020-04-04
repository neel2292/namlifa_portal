$(document).ready(function() {
	var $edit = $("#edit"),
        $save = $("#save_edit"),
        $cancel =  $("#cancel");

	$save.hide();
	$cancel.hide();

    $edit.on("click", function(e) {
        e.preventDefault();
        $save.show();
        $cancel.show();
        $edit.hide();
    });

    $save.on("click", function(e) {
        e.preventDefault();
    });

    $cancel.on("click", function(e) {
        e.preventDefault();
        $save.hide();
        $cancel.hide();
        $edit.show();
    });

});