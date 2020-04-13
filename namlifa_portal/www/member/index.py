import frappe
import json

def get_context(context):
    if frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/'
        raise frappe.Redirect

    member = frappe.db.get_value("Namlifa Member", {"email": frappe.session.user}, "*")

    try:
        member
    except NameError:
        print("well, it WASN'T defined after all!")
    else:
        try:
            if member.membership_type == 'AFFILIATE' or member.membership_type == 'PROVISIONAL':
                member.membership_type = 'ORDINARY'
        except ValueError:
            member.membership_type = member.membership_type

        akard = frappe.db.get_value("Namlifa Akard", {"namlifa_member_id": member.name}, "*")
        # pa = frappe.db.get_value("Namlifa PA", {"membership_no": membership_no}, "*")
        # pa_member = frappe.db.get_values("Namlifa PA Member", {"parent": pa.name}, "*")
        # pi = frappe.db.get_value("Namlifa PI", {"membership_no": member.name}, "*")
        # pi_member = frappe.db.get_values("Namlifa PI Member", {"parent": pi.name}, "*")
        # training = frappe.db.get_value("Namlifa Akard", {"email": frappe.session.user}, "*")

        context.user = frappe.session.user
        context.user_doc = frappe.session
        context.csrf_token = frappe.sessions.get_csrf_token()
        context.member = member
        context.akard = akard
        # context.training = training
        # context.pa = pa
        # context.pa_members = pa_member
        # context.pi = pi
        # context.pi_members = pi_member


    return context