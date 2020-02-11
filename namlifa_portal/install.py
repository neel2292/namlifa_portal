from __future__ import print_function, unicode_literals

import frappe
from frappe import _
from frappe.desk.page.setup_wizard.setup_wizard import add_all_roles_to

def after_install():
    add_roles()

def add_roles():
    roles = ["Namlifa Member"]

    for role in roles:
        if not frappe.db.exists("Role", role):
            r = frappe.get_doc(dict(doctype="Role", role_name=role, desk_access=1))
            r.flags.ignore_mandatory = r.flags.ignore_permissions = True
            r.insert()

    add_all_roles_to("Administrator")
    frappe.db.commit()