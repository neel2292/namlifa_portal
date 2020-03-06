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
   "fieldname": "gpa_joined",
   "fieldtype": "Data",
   "label": "GPA Joined Since"
  },
  {
   "fieldname": "receipt_no",
   "fieldtype": "Data",
   "label": "Receipt No"
  },
  {
   "fieldname": "branch",
   "fieldtype": "Data",
   "label": "Branch"
  },
  {
   "fieldname": "namlifa_pa_members",
   "fieldtype": "Table",
   "label": "Namlifa PA Members",
   "options": "Namlifa PA Member"
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
   "fieldname": "sum_assured",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Sum Assured"
  },
  {
   "fieldname": "address",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Address"
  },
  {
   "fieldname": "postcode",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Postcode"
  },
  {
   "fieldname": "city",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "City"
  },
  {
   "fieldname": "state",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "State"
  },
  {
   "fieldname": "tel_o",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Tel No(O)"
  },
  {
   "fieldname": "tel_hp",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Tel H/P"
  },
  {
   "fieldname": "company",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Company"
  },
  {
   "fieldname": "email",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Email"
  },
  {
   "fieldname": "insurance_validity",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Period Of Insurance"
  },
  {
   "fieldname": "credit_card_no",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Credit Card No/Cheque No"
  },
  {
   "fieldname": "payment_mode",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Payment Mode"
  },
  {
   "fieldname": "bank",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Bank"
  },
  {
   "fieldname": "premium_sst",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Premium Exclude SST 6%"
  },
  {
   "fieldname": "total_premium",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Total Premium Include SST 6%"
  },
  {
   "fieldname": "premium",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Premium"
  },
  {
   "fieldname": "over_premium",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Over Premium"
  },
  {
   "fieldname": "auto_renewal",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Auto Renewal"
  },
  {
   "fieldname": "certificate_number",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Certificate Number"
  },
  {
   "fieldname": "nominee_one",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Nominee 1"
  },
  {
   "fieldname": "nominee_one_relationship",
   "fieldtype": "Data",
   "label": "Nominee Relationship 1"
  },
  {
   "fieldname": "nominee_one_ic_no",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Nominee's IC No 1"
  },
  {
   "fieldname": "nominee_one_share",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Share % 1"
  },
  {
   "fieldname": "nominee_two",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Nominee 2"
  },
  {
   "fieldname": "nominee_two_relationship",
   "fieldtype": "Data",
   "label": "Nominee Relationship 2"
  },
  {
   "fieldname": "nominee_two_ic_no",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Nominee's IC No 2"
  },
  {
   "fieldname": "nominee_two_share",
   "fieldtype": "Data",
   "label": "Share % 2"
  },
  {
   "fieldname": "nominee_three",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Nominee 3"
  },
  {
   "fieldname": "nominee_three_relationship",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Nominee Relationship 3"
  },
  {
   "fieldname": "nominee_three_ic_no",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Nominee's IC No 3"
  },
  {
   "fieldname": "nominee_three_share",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Share % 3"
  }
 ]

def get_context(context):
    member_id = frappe.db.get_value("Namlifa Member", {"email": frappe.session.user}, "name")
    pa = frappe.db.get_value("Namlifa PA", {"membership_no": member_id}, "*")
    pa_member = frappe.db.get_values("Namlifa PA Member", {"parent": pa.name}, "*")
    context.user = frappe.session.user
    context.user_doc = frappe.session
    context.csrf_token = frappe.sessions.get_csrf_token()
    context.fields = fields
    context.pa = pa
    context.members_fields = members_fields
    context.members = pa_member

    return context