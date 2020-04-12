//$('div.ellipsis.title-text:last').text($('div.ellipsis.title-text:last').text().replace('Namlifa', 'NAMLIFA'));

console.log('List');

frappe.listview_settings['Namlifa Member'] = {
	onload: function(listview) {
		upperNamlifa();
	}
}


frappe.listview_settings['Namlifa PA'] = {
    onload: function(listview) {
            upperNamlifa();
    }
}

frappe.listview_settings['Namlifa PI'] = {
    onload: function(listview) {
            upperNamlifa();
    }
}

frappe.listview_settings['Namlifa Akard'] = {
    onload: function(listview) {
            upperNamlifa();
    }
}

frappe.listview_settings['Namlifa Training History'] = {
    onload: function(listview) {
        upperNamlifa();
    }
}
