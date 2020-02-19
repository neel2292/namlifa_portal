import frappe
import json


fields = [
  {
   "fieldname": "user_name",
   "fieldtype": "Data",
   "label": "Name"
  },
  {
   "fieldname": "new_nric_no",
   "fieldtype": "Data",
   "label": "IC No"
  },
  {
   "fieldname": "tel_hp",
   "fieldtype": "Data",
   "label": "Mobile No"
  },
  {
   "fieldname": "email",
   "fieldtype": "Data",
   "label": "Email"
  },
  {
   "fieldname": "company",
   "fieldtype": "Data",
   "label": "Company"
  },
  {
   "fieldname": "agent_code",
   "fieldtype": "Data",
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
   "label": "Year of Completion LP101"
  },
  {
   "fieldname": "lp101_grade",
   "fieldtype": "Data",
   "label": "LP101 Grade Achieved"
  },
  {
   "fieldname": "date_lp102_completed",
   "fieldtype": "Date",
   "label": "Year of Completion LP102"
  },
  {
   "fieldname": "lp102_grade",
   "fieldtype": "Data",
   "label": "LP102 Grade Achieved"
  },
  {
   "fieldname": "date_lp103_completed",
   "fieldtype": "Date",
   "label": "Year of Completion LP103"
  },
  {
   "fieldname": "lp103_grade",
   "fieldtype": "Data",
   "label": "LP103 Grade"
  },
  {
   "fieldname": "date_lp104_completed",
   "fieldtype": "Date",
   "label": "Year of Completion LP104"
  },
  {
   "fieldname": "lp104_grade",
   "fieldtype": "Data",
   "label": "LP104 Grade"
  },
  {
   "fieldname": "date_ch1fp_completed",
   "fieldtype": "Date",
   "label": "Year of Completion Ch1FP"
  },
  {
   "fieldname": "ch1fp_grade",
   "fieldtype": "Data",
   "label": "Ch1FP Grade"
  },
  {
   "fieldname": "date_chapm_completed",
   "fieldtype": "Date",
   "label": "Year of Completion ChAPM"
  },
  {
   "fieldname": "champ_grade",
   "fieldtype": "Data",
   "label": "ChAPM Grade"
  },
  {
   "fieldname": "date_rfp_completed",
   "fieldtype": "Date",
   "label": "Year of Completion RFP"
  },
  {
   "fieldname": "rfp_grade",
   "fieldtype": "Data",
   "label": "RFP Grade"
  },
  {
   "fieldname": "graduation_date",
   "fieldtype": "Date",
   "label": "Year of Graduation"
  },
  {
   "fieldname": "date_taken",
   "fieldtype": "Date",
   "label": "Date Taken"
  }
 ]

def get_context(context):
    training = frappe.db.get_value("Namlifa Training", {"email": frappe.session.user}, "*")
    context.user = frappe.session.user
    context.user_doc = frappe.session
    context.csrf_token = frappe.sessions.get_csrf_token()
    context.fields = fields
    context.training = training

    return context