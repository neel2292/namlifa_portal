import frappe
import json

def get_context(context):

    context.user = frappe.session.user
    context.user_doc = frappe.session
    context.csrf_token = frappe.sessions.get_csrf_token()

    return context