import frappe
import json

fields = [
  {
   "fieldname": "user_name",
   "fieldtype": "Data",
   "label": "Name",
    "fieldvalue": "Neel Singh"
  },
  {
   "fieldname": "new_nric_no",
   "fieldtype": "Data",
   "label": "IC No",
    "fieldvalue": "880808-88-8888"
  },
  {
   "fieldname": "tel_hp",
   "fieldtype": "Data",
   "label": "Mobile No",
    "fieldvalue": "0123456789"
  },
  {
   "fieldname": "email",
   "fieldtype": "Data",
   "label": "Email",
    "fieldvalue": "test@gmail.com"
  },
  {
   "fieldname": "company",
   "fieldtype": "Data",
   "label": "Company",
    "fieldvalue": "Company XXX"
  },
  {
   "fieldname": "agent_code",
   "fieldtype": "Data",
   "label": "Agent Code",
    "fieldvalue": "XXX-007"
  },
  {
   "fieldname": "position",
   "fieldtype": "Data",
   "label": "Position",
    "fieldvalue": "Manager"
  },
  {
   "fieldname": "date_lp101_completed",
   "fieldtype": "Date",
   "label": "Year of Completion LP101",
    "fieldvalue": "2016"
  },
  {
   "fieldname": "lp101_grade",
   "fieldtype": "Data",
   "label": "LP101 Grade Achieved",
    "fieldvalue": "A"
  },
  {
   "fieldname": "date_lp102_completed",
   "fieldtype": "Date",
   "label": "Year of Completion LP102",
    "fieldvalue": "2017"
  },
  {
   "fieldname": "lp102_grade",
   "fieldtype": "Data",
   "label": "LP102 Grade Achieved",
    "fieldvalue": "A"
  },
  {
   "fieldname": "date_lp103_completed",
   "fieldtype": "Date",
   "label": "Year of Completion LP103",
    "fieldvalue": "2018"
  },
  {
   "fieldname": "lp103_grade",
   "fieldtype": "Data",
   "label": "LP103 Grade",
    "fieldvalue": "A"
  },
  {
   "fieldname": "date_lp104_completed",
   "fieldtype": "Date",
   "label": "Year of Completion LP104",
    "fieldvalue": "2019"
  },
  {
   "fieldname": "lp104_grade",
   "fieldtype": "Data",
   "label": "LP104 Grade",
    "fieldvalue": "A"
  },
  {
   "fieldname": "date_ch1fp_completed",
   "fieldtype": "Date",
   "label": "Year of Completion Ch1FP",
    "fieldvalue": "2020"
  },
  {
   "fieldname": "ch1fp_grade",
   "fieldtype": "Data",
   "label": "Ch1FP Grade",
    "fieldvalue": "A"
  },
  {
   "fieldname": "date_chapm_completed",
   "fieldtype": "Date",
   "label": "Year of Completion ChAPM",
    "fieldvalue": "2020"
  },
  {
   "fieldname": "champ_grade",
   "fieldtype": "Data",
   "label": "ChAPM Grade",
    "fieldvalue": "A"
  },
  {
   "fieldname": "date_rfp_completed",
   "fieldtype": "Date",
   "label": "Year of Completion RFP",
    "fieldvalue": "2018"
  },
  {
   "fieldname": "rfp_grade",
   "fieldtype": "Data",
   "label": "RFP Grade",
    "fieldvalue": "A"
  },
  {
   "fieldname": "graduation_date",
   "fieldtype": "Date",
   "label": "Year of Graduation",
    "fieldvalue": "2020"
  },
  {
   "fieldname": "date_taken",
   "fieldtype": "Date",
   "label": "Date Taken",
    "fieldvalue": "08-08-2020"
  }
 ]

def get_context(context):

    context.user = frappe.session.user
    context.user_doc = frappe.session
    context.csrf_token = frappe.sessions.get_csrf_token()
    context.fields = fields

    return context