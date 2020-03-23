import frappe
import json


fields = [
  {
   "fetch_from": "membership_no.full_name",
   "fieldname": "user_name",
   "fieldtype": "Read Only",
   "label": "Name"
  },
  {
   "fetch_from": "membership_no.new_nric_no",
   "fieldname": "new_nric_no",
   "fieldtype": "Read Only",
   "label": "IC No"
  },
  {
   "fetch_from": "membership_no.tel_hp",
   "fieldname": "tel_hp",
   "fieldtype": "Read Only",
   "label": "Mobile No"
  },
  {
   "fetch_from": "membership_no.email",
   "fieldname": "email",
   "fieldtype": "Read Only",
   "label": "Email"
  },
  {
   "fetch_from": "membership_no.company",
   "fieldname": "company",
   "fieldtype": "Read Only",
   "label": "Company"
  },
  {
   "fetch_from": "membership_no.agent_code",
   "fieldname": "agent_code",
   "fieldtype": "Read Only",
   "label": "Agent Code"
  },
  {
   "fieldname": "position",
   "fieldtype": "Data",
   "label": "Position"
  },
  {
   "fieldname": "date_lp101_completed",
   "fieldtype": "Date",
   "hidden": 1,
   "label": "Year of Completion LP101"
  },
  {
   "fieldname": "lp101_grade",
   "fieldtype": "Select",
   "label": "LP101 Grade Achieved",
   "options": "A\nB\nC\nF\nAB"
  },
  {
   "fieldname": "date_lp102_completed",
   "fieldtype": "Date",
   "hidden": 1,
   "label": "Year of Completion LP102"
  },
  {
   "fieldname": "lp102_grade",
   "fieldtype": "Select",
   "label": "LP102 Grade Achieved",
   "options": "A\nB\nC\nF\nAB"
  },
  {
   "fieldname": "date_lp103_completed",
   "fieldtype": "Date",
   "hidden": 1,
   "label": "Year of Completion LP103"
  },
  {
   "fieldname": "lp103_grade",
   "fieldtype": "Select",
   "label": "LP103 Grade",
   "options": "A\nB\nC\nF\nAB"
  },
  {
   "fieldname": "date_lp104_completed",
   "fieldtype": "Date",
   "hidden": 1,
   "label": "Year of Completion LP104"
  },
  {
   "fieldname": "lp104_grade",
   "fieldtype": "Select",
   "label": "LP104 Grade",
   "options": "A\nB\nC\nF\nAB"
  },
  {
   "fieldname": "date_chapm_completed",
   "fieldtype": "Date",
   "hidden": 1,
   "label": "Year of Completion ChAPM"
  },
  {
   "fieldname": "champ_grade",
   "fieldtype": "Select",
   "label": "ChAPM Grade",
   "options": "A\nB\nC\nF\nAB"
  },
  {
   "fieldname": "graduation_date",
   "fieldtype": "Date",
   "hidden": 1,
   "label": "Year of Graduation"
  },
  {
   "fieldname": "date_taken",
   "fieldtype": "Date",
   "label": "Date Taken"
  },
  {
   "fieldname": "membership_no",
   "fieldtype": "Link",
   "in_list_view": 1,
   "label": "Membership No",
   "options": "Namlifa Member"
  },
  {
   "fieldname": "chifp_grade",
   "fieldtype": "Select",
   "label": "ChIFP Grade",
   "options": "A\nB\nC\nF\nAB"
  },
  {
   "fieldname": "month_lp101_completed",
   "fieldtype": "Data",
   "label": "Month of Completion LP101"
  },
  {
   "fieldname": "year_lp101_completed",
   "fieldtype": "Data",
   "label": "Year of Completion LP101"
  },
  {
   "fieldname": "month_lp102_completed",
   "fieldtype": "Data",
   "label": "Month of Completion LP102"
  },
  {
   "fieldname": "year_lp102_completed",
   "fieldtype": "Data",
   "label": "Year of Completion LP102"
  },
  {
   "fieldname": "month_lp103_completed",
   "fieldtype": "Data",
   "label": "Month of Completion LP103"
  },
  {
   "fieldname": "year_lp103_completed",
   "fieldtype": "Data",
   "label": "Year of Completion LP103"
  },
  {
   "fieldname": "month_lp104_completed",
   "fieldtype": "Data",
   "label": "Month of Completion LP104"
  },
  {
   "fieldname": "year_lp104_completed",
   "fieldtype": "Data",
   "label": "Year of Completion LP104"
  },
  {
   "fieldname": "month_lpifp_completed",
   "fieldtype": "Data",
   "label": "Month of Completion LPIFP"
  },
  {
   "fieldname": "year_lpifp_completed",
   "fieldtype": "Data",
   "label": "Year of Completion LPIFP"
  },
  {
   "fieldname": "date_chifp_completed",
   "fieldtype": "Date",
   "hidden": 1,
   "label": "Year of Completion ChIFP"
  },
  {
   "fieldname": "month_chapm_completed",
   "fieldtype": "Data",
   "label": "Month of Completion ChAPM"
  },
  {
   "fieldname": "year_chapm_completed",
   "fieldtype": "Data",
   "label": "Year of Completion ChAPM"
  },
  {
   "fieldname": "month_graduation",
   "fieldtype": "Data",
   "label": "Month of Graduation"
  },
  {
   "fieldname": "year_graduation",
   "fieldtype": "Data",
   "label": "Year of Graduation"
  }




 ]

def get_context(context):
    member_id = frappe.db.get_value("Namlifa Member", {"email": frappe.session.user}, "name")
    member = frappe.db.get_value("Namlifa Member", {"email": frappe.session.user}, "*")
    training = frappe.db.get_value("Namlifa Training History", {"membership_no": member_id}, "*")
    context.user = frappe.session.user
    context.user_doc = frappe.session
    context.csrf_token = frappe.sessions.get_csrf_token()
    context.fields = fields
    context.training = training

    return context
