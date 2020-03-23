import frappe
import json
from frappe import throw, _

fields = [
  {
   "fieldname": "personal_details_section",
   "fieldtype": "Section Break",
   "label": "Personal Details"
  },
  {
   "fieldname": "namlifa_member_id",
   "fieldtype": "Link",
   "label": "Namlifa Membership No",
   "options": "Namlifa Member"
  },
  {
   "fieldname": "title",
   "fieldtype": "Data",
   "label": "Title"
  },
  {
   "fieldname": "full_name",
   "fieldtype": "Data",
   "label": "Full Name"
  },
  {
   "fieldname": "new_nric_no",
   "fieldtype": "Data",
   "label": "New NRIC No"
  },
  {
   "fieldname": "agent_code",
   "fieldtype": "Data",
   "label": "Agent Code"
  },
  {
   "fieldname": "company_name",
   "fieldtype": "Data",
   "label": "Company Name"
  },
  {
   "fieldname": "designation",
   "fieldtype": "Data",
   "label": "Designation"
  },
  {
   "fieldname": "agency_address",
   "fieldtype": "Data",
   "label": "Agency Address"
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
   "fieldname": "correspondence_address",
   "fieldtype": "Data",
   "label": "Correspondence Address"
  },
  {
   "fieldname": "correspondence_postcode",
   "fieldtype": "Data",
   "label": "Correspondence Postcode"
  },
  {
   "fieldname": "correspondence_city",
   "fieldtype": "Data",
   "label": "Correspondence City"
  },
  {
   "fieldname": "tel_o",
   "fieldtype": "Data",
   "label": "Tel (Office)"
  },
  {
   "fieldname": "tel_hp",
   "fieldtype": "Data",
   "label": "Mobile No"
  },
  {
   "fieldname": "tel_fax",
   "fieldtype": "Data",
   "label": "Fax No"
  },
  {
   "fieldname": "email",
   "fieldtype": "Data",
   "label": "Email"
  },
  {
   "fieldname": "branch",
   "fieldtype": "Data",
   "label": "Branch",
   "options": "KUALA LUMPUR\nJOHOR\nKUCHING\nMELAKA\nMIRI\nN.SEMBILAN\nKLANG\nPAHANG\nSABAH\nSIBU\nPENANG\nPERAK"
  },
  {
   "fieldname": "akard_plan",
   "fieldtype": "Data",
   "label": "AKARD Plan"
  },
  {
   "fieldname": "akard_builders_award",
   "fieldtype": "Data",
   "label": "AKARD Builders Award"
  },
  {
   "fieldname": "life_member",
   "fieldtype": "Data",
   "label": "AKARD Life Member"
  },
  {
   "fieldname": "payment_details",
   "fieldtype": "Section Break",
   "label": "Payment Details"
  },
  {
   "fieldname": "fee",
   "fieldtype": "Data",
   "label": "AKARD Fee"
  },
  {
   "fieldname": "member_fee",
   "fieldtype": "Data",
   "label": "Membership Fee"
  },
  {
   "fieldname": "total_payable",
   "fieldtype": "Section Break",
   "label": "Total Payable"
  },
  {
   "fieldname": "total_fee",
   "fieldtype": "Data",
   "label": "Total Fee"
  },
  {
   "fieldname": "method_payment",
   "fieldtype": "Section Break",
   "label": "Method of Payment"
  },
  {
   "fieldname": "payment_method",
   "fieldtype": "Data",
   "label": "Method of Payment"
  },
  {
   "fieldname": "amount",
   "fieldtype": "Data",
   "label": "Amount"
  },
  {
   "fieldname": "cheque_no",
   "fieldtype": "Data",
   "label": "Cheque No"
  },
  {
   "fieldname": "card_type",
   "fieldtype": "Data",
   "label": "Card Type"
  },
  {
   "fieldname": "card_bank",
   "fieldtype": "Data",
   "label": "Issuing Bank"
  },
  {
   "fieldname": "card_no",
   "fieldtype": "Data",
   "label": "Credit Card No"
  },
  {
   "fieldname": "expiry_date",
   "fieldtype": "Date",
   "label": "Expiry Date"
  },
  {
   "fieldname": "card_name",
   "fieldtype": "Data",
   "label": "Name"
  },
  {
   "fieldname": "date",
   "fieldtype": "Date",
   "label": "Date"
  }
 ]

def get_context(context):
    akard = frappe.db.get_value("Namlifa Akard", {"email": frappe.session.user}, "*")
    context.user = frappe.session.user
    context.akard = akard
    context.fields = fields
    context.csrf_token = frappe.sessions.get_csrf_token()
    context.mock = mock_data

    return context
