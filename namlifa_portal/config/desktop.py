# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Namlifa Portal",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Namlifa Portal")
		},
		{
			"module_name": "Namlifa Members",
			"color": "red",
			"icon": "octicon octicon-organization",
			"type": "module",
			"label": _("Namlifa Members")
		},
		{
			"module_name": "Namlifa Member",
			"color": "red",
			"icon": "octicon octicon-person",
			"_doctype": "Namlifa Member",
			"type": "list",
			"link": "List/Namlifa Member",
			"label": _("Namlifa Member")
		}
	]
