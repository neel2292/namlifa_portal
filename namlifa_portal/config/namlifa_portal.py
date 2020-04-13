from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Membership Management"),
			"items": [
				{
						"type": "doctype",
						"name": "Namlifa Member",
						"label": "NAMLIFA Member",
				},      
				{
						"type": "doctype",
						"name": "Namlifa Akard",
						"label": "NAMLIFA AKARD",
				},
				{
						"type": "doctype",
						"name": "Namlifa PA",
						"label": "NAMLIFA PA",
				},
				{
						"type": "doctype",
						"name": "Namlifa PI",
						"label": "NAMLIFA PI",
				},
				{
						"type": "doctype",
						"name": "Namlifa Training History",
						"label": "NAMLIFA Training History",
				},
			]
		},
		{
			"label": _("Fees"),
			"items": [
				{
						"type": "doctype",
						"name": "Namlifa Akard Membership",
						"label": "NAMLIFA AKARD Membership",
				},      
				{
						"type": "doctype",
						"name": "Namlifa Akard Plan",
						"label": "NAMLIFA AKARD Plan",
				},
				{
						"type": "doctype",
						"name": "Namlifa Akard Builder",
						"label": "NAMLIFA AKARD Builder",
				}
			]
		},
	]
