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
   "fieldname": "akard_id",
   "fieldtype": "Data",
   "label": "AKARD ID",
  },
  {
   "fieldname": "title",
   "fieldtype": "Data",
   "label": "Title"
  },
  {
   "fetch_from": "namlifa_member_id.full_name",
   "fieldname": "full_name",
   "fieldtype": "Read Only",
   "in_list_view": 1,
   "in_standard_filter": 1,
   "label": "Full Name"
  },
  {
   "fetch_from": "namlifa_member_id.new_nric_no",
   "fieldname": "new_nric_no",
   "fieldtype": "Read Only",
   "label": "New NRIC No"
  },
  {
   "fetch_from": "namlifa_member_id.agent_code",
   "fieldname": "agent_code",
   "fieldtype": "Read Only",
   "label": "Agent Code"
  },
  {
   "fetch_from": "namlifa_member_id.company",
   "fieldname": "company_name",
   "fieldtype": "Read Only",
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
   "fetch_from": "namlifa_member_id.correspondence_address",
   "fieldname": "correspondence_address",
   "fieldtype": "Read Only",
   "label": "Correspondence Address"
  },
  {
   "fetch_from": "namlifa_member_id.postcode",
   "fieldname": "correspondence_postcode",
   "fieldtype": "Read Only",
   "label": "Correspondence Postcode"
  },
  {
   "fieldname": "correspondence_city",
   "fieldtype": "Data",
   "label": "Correspondence City"
  },
  {
   "fetch_from": "namlifa_member_id.tel_o",
   "fieldname": "tel_o",
   "fieldtype": "Read Only",
   "label": "Tel (Office)"
  },
  {
   "fetch_from": "namlifa_member_id.tel_hp",
   "fieldname": "tel_hp",
   "fieldtype": "Read Only",
   "label": "Mobile No"
  },
  {
   "fetch_from": "namlifa_member_id.tel_fax",
   "fieldname": "tel_fax",
   "fieldtype": "Read Only",
   "label": "Fax No"
  },
  {
   "fetch_from": "namlifa_member_id.email",
   "fieldname": "email",
   "fieldtype": "Read Only",
   "label": "Email"
  },
  {
   "fieldname": "branch",
   "fieldtype": "Select",
   "label": "Branch",
   "options": "KUALA LUMPUR\nJOHOR\nKUCHING\nMELAKA\nMIRI\nN.SEMBILAN\nKLANG\nPAHANG\nSABAH\nSIBU\nPENANG\nPERAK"
  },
  {
   "fieldname": "akard_builders_award",
   "fieldtype": "Link",
   "label": "AKARD Builders Award",
   "options": "Namlifa Akard Builder"
  },
  {
   "fieldname": "life_member",
   "fieldtype": "Select",
   "label": "AKARD Life Member",
   "options": "10 YEARS - 15 YEARS\n16 YEARS\n17 YEARS"
  },
  {
   "fieldname": "payment_details",
   "fieldtype": "Section Break",
   "label": "Payment Details"
  },
  {
   "fetch_from": "akard_plan.fee",
   "fieldname": "fee",
   "fieldtype": "Currency",
   "label": "AKARD Fee"
  },
  {
   "fetch_from": "member.fee",
   "fieldname": "member_fee",
   "fieldtype": "Currency",
   "label": "Membership Fee"
  },
  {
   "fieldname": "total_payable",
   "fieldtype": "Section Break",
   "label": "Total Payable"
  },
  {
   "fieldname": "total_fee",
   "fieldtype": "Currency",
   "label": "Total Fee",
   "read_only": 1
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
   "fieldtype": "Data",
   "label": "Expiry Date"
  },
  {
   "fieldname": "card_name",
   "fieldtype": "Data",
   "label": "Credit Card Showing Name"
  },
  {
   "fieldname": "date",
   "fieldtype": "Date",
   "label": "Date"
  },
  {
   "fieldname": "late_fee",
   "fieldtype": "Currency",
   "label": "Late Filing Fee"
  },
  {
   "fieldname": "member",
   "fieldtype": "Link",
   "label": "Membership",
   "options": "Namlifa Akard Membership"
  },
  {
   "fetch_from": "akard_builders_award.fee",
   "fieldname": "akard_builders_award_fee",
   "fieldtype": "Currency",
   "label": "Akard Builders Award Fee"
  },
  {
   "fetch_from": "namlifa_member_id.membership_no",
   "fieldname": "membership_no",
   "fieldtype": "Data",
   "label": "Membership No",
   "unique": 1
  },
  {
   "fieldname": "award_category_section",
   "fieldtype": "Section Break",
   "label": "Award Category"
  },
  {
   "default": "0",
   "fieldname": "akard_personal_gold",
   "fieldtype": "Check",
   "label": "AKARD PERSONAL GOLD"
  },
  {
   "default": "0",
   "fieldname": "akard_personal_platinum",
   "fieldtype": "Check",
   "label": "AKARD PERSONAL PLATINUM"
  },
  {
   "default": "0",
   "fieldname": "akard_personal_diamond",
   "fieldtype": "Check",
   "label": "AKARD PERSONAL DIAMOND"
  },
  {
   "fieldname": "column_break_24",
   "fieldtype": "Column Break"
  },
  {
   "default": "0",
   "fieldname": "akard_leaders_direct",
   "fieldtype": "Check",
   "label": "AKARD LEADERS DIRECT"
  },
  {
   "default": "0",
   "fieldname": "akard_million_dollar_agency",
   "fieldtype": "Check",
   "label": "AKARD MILLION DOLLAR AGENCY"
  },
  {
   "default": "0",
   "fieldname": "akard_mega_million_dollar_agency",
   "fieldtype": "Check",
   "label": "AKARD MEGA MILLION DOLLAR AGENCY"
  },
  {
   "fieldname": "column_break_28",
   "fieldtype": "Column Break"
  },
  {
   "default": "0",
   "fieldname": "akard_star_rookie",
   "fieldtype": "Check",
   "label": "AKARD STAR ROOKIE"
  },
  {
   "default": "0",
   "fieldname": "akard_101",
   "fieldtype": "Check",
   "label": "AKARD 101"
  },
  {
   "fieldname": "processing_section_section",
   "fieldtype": "Section Break",
   "label": "Processing Section"
  },
  {
   "fieldname": "received_date",
   "fieldtype": "Date",
   "label": "Received Date"
  },
  {
   "fieldname": "receipt_no",
   "fieldtype": "Data",
   "label": "Receipt No."
  },
  {
   "fetch_from": "namlifa_member_id.join_date",
   "fieldname": "join_date",
   "fieldtype": "Read Only",
   "label": "Join Date"
  },
  {
   "fieldname": "akard_id",
   "fieldtype": "Data",
   "label": "AKARD ID"
  },
  {
   "fieldname": "premium_credit",
   "fieldtype": "Data",
   "label": "PREMIUM CREDIT (CONVENTIONAL)"
  },
  {
   "fieldname": "premium_takaful",
   "fieldtype": "Data",
   "label": "PREMIUM CREDIT (TAKAFUL)"
  },
  {
   "fieldname": "premium_total",
   "fieldtype": "Data",
   "label": "PREMIUM CREDIT (TOTAL)"
  },
  {
   "fieldname": "section_break_37",
   "fieldtype": "Section Break"
  },
  {
   "fieldname": "section_break_34",
   "fieldtype": "Section Break"
  },
  {
   "fieldname": "html_37",
   "fieldtype": "HTML",
   "options": "+"
  },
  {
   "fieldname": "html_38",
   "fieldtype": "HTML",
   "options": "="
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
