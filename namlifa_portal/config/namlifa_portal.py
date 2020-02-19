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
                                },      
                                {
                                        "type": "doctype",
                                        "name": "Namlifa Akard",
                                },


				{
					"type": "doctype",
					"name": "Issue",
					"onboard": 1,
				},
			]
		},
	]
