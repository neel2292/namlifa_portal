import frappe
import json

fields = [
  {
   "fieldname": "membership_no",
   "fieldtype": "Link",
   "label": "Membership No",
   "options": "Namlifa Member"
  },
  {
   "fieldname": "membership_expiry",
   "fieldtype": "Data",
   "label": "Membership Valid Till"
  },
  {
   "fieldname": "pi_join_date",
   "fieldtype": "Data",
   "label": "PI Joined Since"
  },
  {
   "fieldname": "receipt_number",
   "fieldtype": "Data",
   "label": "Receipt Number"
  },
  {
   "fieldname": "branch",
   "fieldtype": "Data",
   "label": "Branch"
  },
  {
   "fieldname": "namlifa_pi_members",
   "fieldtype": "Table",
   "label": "Namlifa PI Members",
   "options": "Namlifa PI Member"
  }
 ]
members_fields = [
  {
   "fieldname": "full_name",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Name"
  },
  {
   "fieldname": "new_nric_no",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "IC No"
  },
  {
   "fieldname": "relationship",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Relationship"
  },
  {
   "fieldname": "age",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Age"
  },
  {
   "fieldname": "occupation",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Occupation"
  },
  {
   "fieldname": "renewal_application",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Renewal/New Application"
  },
  {
   "fieldname": "agent",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Agent/Leader"
  },
  {
   "fieldname": "sum_assured",
   "fieldtype": "Data",
   "label": "Sum Assured"
  },
  {
   "fieldname": "address",
   "fieldtype": "Data",
   "label": "Address"
  },
  {
   "fieldname": "postcode",
   "fieldtype": "Data",
   "label": "Postcode"
  },
  {
   "fieldname": "city",
   "fieldtype": "Data",
   "label": "City"
  },
  {
   "fieldname": "state",
   "fieldtype": "Data",
   "label": "State"
  },
  {
   "fieldname": "tel_o",
   "fieldtype": "Data",
   "label": "Tel No(O)"
  },
  {
   "fieldname": "tel_hp",
   "fieldtype": "Data",
   "label": "Tel H/P"
  },
  {
   "fieldname": "company",
   "fieldtype": "Data",
   "label": "Company"
  },
  {
   "fieldname": "email",
   "fieldtype": "Data",
   "label": "Email"
  },
  {
   "fieldname": "insurance_validity",
   "fieldtype": "Data",
   "label": "Period Of Insurance"
  },
  {
   "fieldname": "credit_card_no",
   "fieldtype": "Data",
   "label": "Credit Card No"
  },
  {
   "fieldname": "payment_mode",
   "fieldtype": "Data",
   "label": "Payment Mode"
  },
  {
   "fieldname": "bank",
   "fieldtype": "Data",
   "label": "Bank"
  },
  {
   "fieldname": "sst_charge",
   "fieldtype": "Data",
   "label": "Premium Exclude SST 6%"
  },
  {
   "fieldname": "total_premium",
   "fieldtype": "Data",
   "label": "Total Premium Include SST 6%"
  },
  {
   "fieldname": "premium",
   "fieldtype": "Data",
   "label": "Premium"
  },
  {
   "fieldname": "over_premium",
   "fieldtype": "Data",
   "label": "Over Premium"
  },
  {
   "fieldname": "auto_renewal",
   "fieldtype": "Data",
   "label": "Auto Renewal"
  },
  {
   "fieldname": "certificate_number",
   "fieldtype": "Data",
   "label": "Certificate Number"
  }
 ]

def get_context(context):
    member_id = frappe.db.get_value("Namlifa Member", {"email": frappe.session.user}, "name")
    member = frappe.db.get_value("Namlifa Member", {"email": frappe.session.user}, "*")
    pi = frappe.db.get_value("Namlifa PI", {"membership_id": member_id}, "*")
    pi_member = frappe.db.get_values("Namlifa PI Member", {"parent": pi.name}, "*")
    context.user = frappe.session.user
    context.user_doc = frappe.session
    context.csrf_token = frappe.sessions.get_csrf_token()
    context.fields = fields
    context.pi = pi
    context.members_fields = members_fields
    context.members = pi_member
    context.member = member

    return context
