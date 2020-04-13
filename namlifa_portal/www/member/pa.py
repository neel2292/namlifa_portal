import frappe
import json

fields = [
  {
   "fetch_from": "membership_id.membership_no",
   "fieldname": "membership_no",
   "fieldtype": "Data",
   "label": "Membership No",
   "unique": 1
  },
  {
   "fetch_from": "membership_id.expiry_date",
   "fieldname": "membership_expiry",
   "fieldtype": "Date",
   "in_list_view": 1,
   "in_standard_filter": 1,
   "label": "Membership Valid Till",
   "read_only": 1
  },
  {
   "fieldname": "gpa_joined",
   "fieldtype": "Date",
   "in_list_view": 1,
   "in_standard_filter": 1,
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
   "fieldname": "nomination",
   "fieldtype": "Table",
   "label": "NOMINATION",
   "options": "Namlifa PA Nomination"
  },
  {
   "fieldname": "section_details",
   "fieldtype": "Section Break",
   "label": "Details"
  },
  {
   "fieldname": "name_as_per_ic",
   "fieldtype": "Data",
   "label": "Name as per IC"
  },
  {
   "fieldname": "ic_number",
   "fieldtype": "Data",
   "label": "IC Number"
  },
  {
   "fieldname": "contact_number",
   "fieldtype": "Data",
   "label": "Contact Number"
  },
  {
   "fieldname": "gpa_joined_since",
   "fieldtype": "Date",
   "label": "GPA Joined Since"
  },
  {
   "fieldname": "sum_assured",
   "fieldtype": "Data",
   "label": "Sum Assured"
  },
  {
   "fieldname": "premium_incl_sst",
   "fieldtype": "Data",
   "label": "Premium Incl SST"
  },
  {
   "fieldname": "details_col1",
   "fieldtype": "Column Break"
  },
  {
   "collapsible": 1,
   "fieldname": "section_details_more",
   "fieldtype": "Section Break",
   "label": "More Details"
  },
  {
   "fieldname": "age",
   "fieldtype": "Data",
   "label": "Age"
  },
  {
   "fieldname": "email_address",
   "fieldtype": "Data",
   "label": "Email Address"
  },
  {
   "fieldname": "occupation",
   "fieldtype": "Data",
   "label": "Occupation"
  },
  {
   "fieldname": "address",
   "fieldtype": "Data",
   "label": "Address"
  },
  {
   "fieldname": "period_of_insurance",
   "fieldtype": "Data",
   "label": "Period of Insurance"
  },
  {
   "fieldname": "master_policy_number",
   "fieldtype": "Data",
   "label": "Master Policy Number"
  },
  {
   "fieldname": "certificate_number",
   "fieldtype": "Data",
   "label": "Certificate Number"
  },
  {
   "fieldname": "receipt_number",
   "fieldtype": "Data",
   "label": "Receipt Number"
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
   "fieldname": "credit_card_no",
   "fieldtype": "Data",
   "label": "Credit Card/Cheque"
  },
  {
   "fieldname": "more_details_col1",
   "fieldtype": "Column Break"
  },
  {
   "fieldname": "premium_excl_sst",
   "fieldtype": "Data",
   "label": "Premium Excl SST"
  },
  {
   "fieldname": "prorated_premium",
   "fieldtype": "Data",
   "label": "Pro-rated Premium"
  },
  {
   "fieldname": "membership_number",
   "fieldtype": "Data",
   "label": "Membership Number"
  },
  {
   "fieldname": "membership_branch",
   "fieldtype": "Data",
   "label": "Membership Branch"
  },
  {
   "fieldname": "application_branch",
   "fieldtype": "Data",
   "label": "Application Branch"
  },
  {
   "fieldname": "more_details_col2",
   "fieldtype": "Column Break"
  },
  {
   "fieldname": "membership_id",
   "fieldtype": "Link",
   "label": "Membership ID",
   "options": "Namlifa Member"
  },
  {
   "default": "0",
   "fieldname": "auto_renewal_pa",
   "fieldtype": "Check",
   "label": "Auto Renewal"
  },
  {
   "fieldname": "renewalnew_application",
   "fieldtype": "Select",
   "label": "Renewal/New Application",
   "options": "\nRENEWAL\nNEW APPLICATION"
  },
  {
   "fieldname": "spouse_child_nomination",
   "fieldtype": "Section Break"
  },
  {
   "fieldname": "spouse_child",
   "fieldtype": "Table",
   "label": "SPOUSE/CHILD",
   "options": "Namlifa PA Spouse"
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
   "label": "Relationship"
  },
  {
   "fieldname": "age",
   "fieldtype": "Data",
   "label": "Age"
  },
  {
   "fieldname": "occupation",
   "fieldtype": "Data",
   "label": "Occupation"
  },
  {
   "fieldname": "renewal_application",
   "fieldtype": "Data",
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
   "in_list_view": 1,
   "label": "Credit Card No/Cheque No"
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
   "fieldname": "premium_sst",
   "fieldtype": "Data",
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
nomination_fields = [
  {
   "fieldname": "name_of_proposer",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Name of Proposer",
   "reqd": 1
  },
  {
   "fieldname": "name_of_nominee",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Name of Nominee"
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
   "fieldname": "address",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Address"
  },
  {
   "fieldname": "share",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Share"
  }
 ]
spouse_fields = [
  {
   "fieldname": "full_name",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Name",
   "reqd": 1
  },
  {
   "fieldname": "new_nric_no",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "IC No"
  },
  {
   "fieldname": "contact_number",
   "fieldtype": "Data",
   "label": "Contact Number"
  },
  {
   "fieldname": "occupation",
   "fieldtype": "Data",
   "label": "Occupation"
  },
  {
   "fieldname": "sum_assured",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Sum Assured"
  },
  {
   "fieldname": "premium_include_sst",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Premium Include SST"
  },
  {
   "fieldname": "relationship",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Relationship"
  }
 ]

def get_context(context):
    member_id = frappe.db.get_value("Namlifa Member", {"email": frappe.session.user}, "name")
    member = frappe.db.get_value("Namlifa Member", {"email": frappe.session.user}, "*")
    pa = frappe.db.get_value("Namlifa PA", {"membership_id": member_id}, "*")
    pa_member = frappe.db.get_values("Namlifa PA Member", {"parent": pa.name}, "*")
    pa_spouse = frappe.db.get_values("Namlifa PA Spouse", {"parent": pa.name}, "*")
    pa_nominee = frappe.db.get_values("Namlifa PA Nomination", {"parent": pa.name}, "*")
    context.user = frappe.session.user
    context.user_doc = frappe.session
    context.csrf_token = frappe.sessions.get_csrf_token()
    context.fields = fields
    context.pa = pa
    context.members_fields = members_fields
    context.nomination_fields = nomination_fields
    context.spouse_fields = spouse_fields
    context.pa_member = pa_member
    context.pa_spouse = pa_spouse
    context.pa_nominee = pa_nominee
    context.member = member

    return context
