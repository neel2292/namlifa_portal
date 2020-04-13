# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "namlifa_portal"
app_title = "Namlifa Portal"
app_publisher = "ERP-X"
app_description = "Namlifa Portal by ERP-X"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "dev.erpx@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/namlifa_portal/css/namlifa_portal.css"
# app_include_js = "/assets/namlifa_portal/js/namlifa_portal.js"
app_include_js = [
    "/assets/namlifa_portal/js/swiss_common.js"
    ]

# include js, css files in header of web template
# web_include_css = "/assets/namlifa_portal/css/namlifa_portal.css"
# web_include_js = "/assets/namlifa_portal/js/namlifa_portal.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
doctype_js = {
    "Namlifa Member": "customization/namlifa_member.js",
    "Namlifa Akard": "customization/namlifa_akard.js",
	"Namlifa PA": "customization/namlifa_pa.js",
	"Namlifa PI": "customization/namlifa_pi.js",
	"Namlifa Training History": "customization/namlifa_th.js",
}
doctype_list_js = {
        "Namlifa Member" : "customization/upper_namlifa.js",
        "Namlifa PA" : "customization/upper_namlifa.js",
        "Namlifa PI" : "customization/upper_namlifa.js",
        "Namlifa Akard" : "customization/upper_namlifa.js",
        "Namlifa Training History" : "customization/upper_namlifa.js",
}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "namlifa_portal.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "namlifa_portal.install.before_install"
# after_install = "namlifa_portal.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "namlifa_portal.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"namlifa_portal.tasks.all"
# 	],
# 	"daily": [
# 		"namlifa_portal.tasks.daily"
# 	],
# 	"hourly": [
# 		"namlifa_portal.tasks.hourly"
# 	],
# 	"weekly": [
# 		"namlifa_portal.tasks.weekly"
# 	]
# 	"monthly": [
# 		"namlifa_portal.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "namlifa_portal.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "namlifa_portal.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "namlifa_portal.task.get_dashboard_data"
# }

