import frappe
import json

mock_data = [
  {
"fieldval": "123456789",
   "fieldname": "membership_no",
   "fieldtype": "Data",
   "label": "Membership No"
  },
  {
"fieldval": "31 Dec 2025",
   "fieldname": "membership_expiry",
   "fieldtype": "Data",
   "label": "Membership Valid Till"
  },
  {
"fieldval": "01 Feb 2020",
   "fieldname": "pi_join_date",
   "fieldtype": "Data",
   "label": "PI Joined Since"
  },
  {
"fieldval": "1323456",
   "fieldname": "receipt_number",
   "fieldtype": "Data",
   "label": "Receipt Number"
  },
  {
"fieldval": "KUALA LUMPUR",
   "fieldname": "branch",
   "fieldtype": "Data",
   "label": "Branch"
  },
  {
"fieldval": "Neel Singh",
   "fieldname": "full_name",
   "fieldtype": "Data",
   "label": "Name"
  },
  {
"fieldval": "880808-88-8888",
   "fieldname": "new_nric_no",
   "fieldtype": "Data",
   "label": "IC No"
  },
  {
"fieldval": "Single",
   "fieldname": "relationship",
   "fieldtype": "Data",
   "label": "Relationship"
  },
  {
"fieldval": "27",
   "fieldname": "age",
   "fieldtype": "Data",
   "label": "Age"
  },
  {
"fieldval": "Engineer",
   "fieldname": "occupation",
   "fieldtype": "Data",
   "label": "Occupation"
  },
  {
"fieldval": "Yes",
   "fieldname": "renewal_application",
   "fieldtype": "Data",
   "label": "Renewal/New Application"
  },
  {
    "fieldval": "Agent X",
   "fieldname": "agent",
   "fieldtype": "Data",
   "label": "Agent/Leader"
  },
  {
"fieldval": "150000",
   "fieldname": "sum_assured",
   "fieldtype": "Data",
   "label": "Sum Assured"
  },
  {
"fieldval": "No.64, Taman Permata, Chemor",
   "fieldname": "address",
   "fieldtype": "Data",
   "label": "Address"
  },
  {
"fieldval": "30450",
   "fieldname": "postcode",
   "fieldtype": "Data",
   "label": "Postcode"
  },
  {
"fieldval": "Ipoh",
   "fieldname": "city",
   "fieldtype": "Data",
   "label": "City"
  },
  {
"fieldval": "Perak",
   "fieldname": "state",
   "fieldtype": "Data",
   "label": "State"
  },
  {
"fieldval": "052134654",
   "fieldname": "tel_o",
   "fieldtype": "Data",
   "label": "Tel No(O)"
  },
  {
"fieldval": "0123456789",
   "fieldname": "tel_hp",
   "fieldtype": "Data",
   "label": "Tel H/P"
  },
  {
"fieldval": "My Company",
   "fieldname": "company",
   "fieldtype": "Data",
   "label": "Company"
  },
  {
"fieldval": "test@gmail.com",
   "fieldname": "email",
   "fieldtype": "Data",
   "label": "Email"
  },
  {
"fieldval": "31 Dec 2045",
   "fieldname": "insurance_validity",
   "fieldtype": "Data",
   "label": "Period Of Insurance"
  },
  {
"fieldval": "0123-4567-8901-2345",
   "fieldname": "credit_card_no",
   "fieldtype": "Data",
   "label": "Credit Card No"
  },
  {
"fieldval": "Visa",
   "fieldname": "payment_mode",
   "fieldtype": "Data",
   "label": "Payment Mode"
  },
  {
"fieldval": "Maybank",
   "fieldname": "bank",
   "fieldtype": "Data",
   "label": "Bank"
  },
  {
"fieldval": "150",
   "fieldname": "sst_charge",
   "fieldtype": "Data",
   "label": "Premium Exclude SST 6%"
  },
  {
"fieldval": "159",
   "fieldname": "total_premium",
   "fieldtype": "Data",
   "label": "Total Premium Include SST 6%"
  },
  {
"fieldval": "150000",
   "fieldname": "premium",
   "fieldtype": "Data",
   "label": "Premium"
  },
  {
"fieldval": "180000",
   "fieldname": "over_premium",
   "fieldtype": "Data",
   "label": "Over Premium"
  },
  {
"fieldval": "Yes",
   "fieldname": "auto_renewal",
   "fieldtype": "Data",
   "label": "Auto Renewal"
  },
  {
"fieldval": "12334488",
   "fieldname": "certificate_number",
   "fieldtype": "Data",
   "label": "Certificate Number"
  }
 ]

def get_context(context):

    context.user = frappe.session.user
    context.user_doc = frappe.session
    context.csrf_token = frappe.sessions.get_csrf_token()
    context.mock = mock_data

    return context