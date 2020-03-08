# -*- coding: utf-8 -*-
# Copyright (c) 2020, ERP-X and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, json, base64, os, copy, re
from frappe import throw, _
from frappe.utils import getdate, validate_email_add, today, formatdate
from frappe.model.document import Document
from collections import namedtuple

class NamlifaMember(Document):
	__new_password = None
	__send_password_update_notification = None
	__logout_all_sessions = None

	def run_post_save_methods(self):
		# Auto create user
		if self.application_status in ["Approved"]:
			if self.user_id is None:
				if frappe.db.exists('User', self.email):
					self.user_id = self.email
				else:
					self.user_id = self.create_user(self)
			else:
				self.activateUser(self.user_id, True)
		elif self.user_id is not None:
			self.activateUser(self.user_id, False)

		# sync userid with email and owner
		if self.user_id:
			self.update_user()
			if self.application_status == 'Active':
				if self.user_id is not self.email:
					self.email = self.user_id
				if self.user_id is not self.owner:
					self.owner = self.user_id
			else:
				self.user_id = ''
		self.db_update()

	def validate(self):
		self.validate_date()
		self.validate_email()

		if self.user_id:
			self.validate_duplicate_user_id()

		if frappe.db.exists('Namlifa Member', self.name):
			existing_member = frappe.get_doc('Namlifa Member', self.name)
			if existing_member.name != self.name:
				self.validate_id()
			if self.user_id is None and existing_member.user_id:
				frappe.permissions.remove_user_permissions('Namlifa Member', self.name, existing_member.user_id)

		# clear new password
		self.__new_password = self.new_password
		self.new_password = ""

		self.__send_password_update_notification = self.send_password_update_notification
		self.send_password_update_notification = 0

		self.__logout_all_sessions = self.logout_all_sessions
		self.logout_all_sessions = ""

	def validate_date(self):
		if self.date_of_birth and getdate(self.date_of_birth) > getdate(today()):
			throw(_("Date of Birth cannot be greater than today."))

	def validate_email(self):
		if self.email:
			validate_email_add(self.email, True)

	def validate_id(self):
		user = frappe.db.sql_list("""select name from `tabUser` where
			username=%s """, self.name)

		if user:
			throw(_('Prudential ID {0} already exist in the system').format(
				self.name), frappe.DuplicateEntryError)

	def validate_duplicate_user_id(self):
		member = frappe.db.sql_list("""SELECT name FROM `tabNamlifa Member` WHERE
			user_id=%s AND user_status='Active' AND name!=%s""", (self.user_id, self.name))
		if member:
			throw(_("User {0} is already assigned to Member {1}").format(
				self.user_id, member[0]), frappe.DuplicateEntryError)

	def update_user(self):
		# add employee role if missing
		user = frappe.get_doc('User', self.user_id)
		user.flags.ignore_permissions = True

		if self.application_status != 'Approved':
			user.enabled = 0
		else:
			user.enabled = 1
			if "Namlifa Member" not in [user_role.role for user_role in user.get('roles')]:
				user.add_roles('Namlifa Member')

			# copy details from member to user
			if self.full_name:
				user.first_name = self.full_name

			if self.date_of_birth:
				user.birth_date = self.date_of_birth

			if self.gender:
				user.gender = self.gender

			if self.photo:
				if not user.user_image:
					user.user_image = self.photo
					try:
						frappe.get_doc({
							"doctype": "File",
							"file_name": self.photo,
							"attached_to_doctype": "User",
							"attached_to_name": self.user_id
						}).insert()
					except frappe.DuplicateEntryError:
						# already exists
						pass

			if self.__new_password:
				user.new_password = self.__new_password
				if self.__send_password_update_notification:
					user.send_password_update_notification = self.__send_password_update_notification
				if self.__logout_all_sessions:
					user.logout_all_sessions = self.__logout_all_sessions
		user.save()

	def activateUser(self, userid=None, activate=True):
		# add employee role if missing
		if frappe.db.exists('User', userid):
			user = frappe.get_doc('User', userid)
			if user.enabled != activate:
				user.flags.ignore_permissions = True
				user.enabled = activate
				user.save()

	def create_user(self, member, user=None):
		user = frappe.get_doc({
			"doctype": "User",
			"email": member.email,
			"enabled": 1,
			"username": member.name,
			"first_name": member.full_name,
			"gender": member.gender,
			"birth_date": member.date_of_birth
		})
		user.flags.no_welcome_email = True
		user.flags.ignore_permissions = True
		if self.__new_password:
			user.new_password = self.__new_password
			if self.__send_password_update_notification:
				user.send_password_update_notification = self.__send_password_update_notification
			if self.__logout_all_sessions:
				user.logout_all_sessions = self.__logout_all_sessions
		else:
			from frappe.utils import random_string
			user.new_password = random_string(10)
		user.insert(ignore_permissions=True)
		user.add_roles("Namlifa Member")
		return user.name


@frappe.whitelist()
def member_login():
	member_name = frappe.db.sql.list("""SELECT name from `tabNamlifa Member` WHERE 
			user_id=%s and application_status='Approved'""", (frappe.session.user))

	if not member_name:
		throw(_("Unable to find member profile for {0}").format(
			frappe.session.user), frappe.DoesNotExistError)
	else:
		member = frappe.get_doc('Namlifa Member', member_name[0])

		return member


@frappe.whitelist(allow_guest=True)
def member_registration():
	date_attrs = ["date_of_birth", "date_contracted_as_agent"]
	#file_attrs = ['photo', 'signature']
	file_attrs = ['terms_signature', 'payment_signature']
	files = []
	data = json.loads(frappe.local.form_dict.data)

	for e in date_attrs:
		if data[e]:
			data[e] = formatdate(data[e], "yyyy-mm-dd")

	for e in file_attrs:
		if data[e]:
			files.append((e, data[e]))
			del data[e]

	doc = frappe.get_doc({"doctype": "Namlifa Member", **data})

	doc.insert(ignore_permissions=True, ignore_mandatory=True)

	files = None

	if files:
		for f in files:
			fieldname, filedata = f
			filerem, filedata = filedata.split(',', 1)
			ext = filerem.split(';')[0].split('/')[1]
			filedata = filedata.encode()
			filename = "{0}-{1}.{2}".format(doc.name, fieldname, ext)
			fileurl = os.path.abspath(frappe.local.site_path) + "/public/files/" + filename

			fh = open(fileurl, "wb")
			fh.write(filedata.decode('base64'))
			fh.close()

			_file = frappe.get_doc({
				"doctype": "File",
				"file_name": filename,
				"attached_to_doctype": doc.doctype,
				"attached_to_name": doc.name,
				"file_url": "/files/" + filename
			})
			_file.save()

			# update values
			doc.set(fieldname, _file.file_url)
			doc.save()

	frappe.db.commit()

	return data
