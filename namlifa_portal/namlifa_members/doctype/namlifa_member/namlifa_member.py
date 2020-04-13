# -*- coding: utf-8 -*-
# Copyright (c) 2020, ERP-X and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe, json, base64, os, copy, re
from frappe import throw, _
from frappe.utils import getdate, validate_email_add, today, formatdate, random_string
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
            # self.__new_password = random_string(10)
            self.update_user()
            if self.application_status in ["Approved"]:
                if self.user_id is not self.email:
                    self.email = self.user_id
                if self.user_id is not self.owner:
                    self.owner = self.user_id
            else:
                self.user_id = ''

        self.db_update()

    def on_submit(self):
        if self.membership_no:
            if self.name != self.membership_no:
                self.name = self.membership_no
        self.db_update()

    def validate(self):
        self.validate_date()
        self.validate_email()

        if self.user_id:
            self.validate_duplicate_user_id()

        if frappe.db.exists('Namlifa Member', self.name):
            existing_member = frappe.get_doc('Namlifa Member', self.name)

            if self.application_status != existing_member.application_status:
                if self.application_status in ["Approved"]:
                    if self.new_password:
                        pass
                    else:
                        self.new_password = random_string(10)
                    frappe.sendmail(
                        recipients=self.email,
                        subject='Your NAMLIFA account is approved',
                        template='set_password',
                        args={
                            'msg': 'Your NAMLIFA application has been approved. Thank you for your support.',
                            'full_name': self.full_name,
                            'password': self.new_password,
                            'email': self.email
                        }
                    )
                elif self.application_status in ["Rejected"]:
                    if self.new_password:
                        pass
                    else:
                        self.new_password = random_string(10)
                    frappe.sendmail(
                        recipients=self.email,
                        subject='Your NAMLIFA account is rejected',
                        template='reject_user',
                        args={
                            'full_name': self.full_name
                        }
                    )

            if existing_member.name != self.name:
                self.validate_id()
            if self.user_id is None and existing_member.user_id:
                frappe.permissions.remove_user_permissions('Namlifa Member', self.name, existing_member.user_id)

        # clear new password
        if self.new_password:
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
                        user_id=%s AND application_status='Approved' AND name!=%s""", (self.user_id, self.name))
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
            user.new_password = random_string(10)
        user.insert(ignore_permissions=True)
        user.add_roles("Namlifa Member")
        return user.email


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
    date_attrs = ["date_of_birth"]
    file_attrs = ['terms_signature', 'payment_signature', 'photo', 'receipt']
    files = []
    data = json.loads(frappe.local.form_dict.data)

    print('dataaaaaaaaaaa', data)

    for e in date_attrs:
        if data[e]:
            data[e] = formatdate(data[e], "yyyy-mm-dd")
    for e in file_attrs:
        if e in data:
            if data[e] != "":
                files.append((e, data[e]))
            del data[e]
    doc = frappe.get_doc({"doctype": "Namlifa Member", **data})
    doc.insert(ignore_permissions=True, ignore_mandatory=True)
    if files:
        for f in files:
            fieldname, filedata = f
            if fieldname in {'photo', 'receipt'}:
                if filedata != '':
                    filerem, filedata = filedata.split(',', 1)
            else:
                filerem, filedata = filedata['img'].split(',', 1)
            ext = filerem.split(';')[0].split('/')[1]
            filename = "{0}-{1}.{2}".format(doc.name, fieldname, ext)
            fileurl = os.path.abspath(frappe.local.site_path) + "/public/files/" + filename
            imgdata = base64.b64decode(filedata)
            with open(fileurl, 'wb') as fh:
                fh.write(imgdata)

            _file = frappe.get_doc({
                "doctype": "File",
                "file_name": filename,
                "attached_to_doctype": doc.doctype,
                "attached_to_name": doc.name,
                "file_url": "/files/" + filename
            })
            _file.save(ignore_permissions=True)
            # update values
            doc.set(fieldname, _file.file_url)
            doc.save()
    frappe.db.commit()
    return data

@frappe.whitelist(allow_guest=True)
def registered(data):
    dat = json.loads(data)
    member = frappe.db.get_value("Namlifa Member", {"email": dat.get('email')}, "*")

    return member

@frappe.whitelist()
def member_update(data):
    dat = json.loads(data)
    doc = frappe.get_doc('Namlifa Member', dat.get('name'))

    if doc.user_id == frappe.session.user:
        doc.flags.ignore_permissions = True
        doc.correspondence_address = dat.get('correspondence_address')
        doc.postcode = dat.get('postcode')
        doc.tel_o = dat.get('tel_o')
        doc.tel_h = dat.get('tel_h')
        doc.tel_hp = dat.get('tel_hp')
        doc.tel_fax = dat.get('tel_fax')

        doc.save()
        return doc
    else:
        throw(_("Unable to find member profile for {0}").format(
            frappe.session.user), frappe.DoesNotExistError)

@frappe.whitelist()
def update_password(data):
    dat = json.loads(data)
    new_password = dat.get('new_password')
    old_password = dat.get('old_password')
    key = None

    from frappe.core.doctype.user import user as _core_user
    result = _core_user.test_password_strength(new_password, key, old_password)
    feedback = result.get("feedback", None)

    if feedback and not feedback.get('password_policy_validation_passed', False):
        return { 'error': 1, 'text': feedback.get('warning') }
        # _core_user.handle_password_test_fail(result)

    #if fail, chances are wrong old_password given for current user
    try:
        res = _core_user._get_user_for_update_password(key, old_password)
    except:
        return { 'error': 1, 'text': 'Wrong password given!', 'wrong_password': 1 }

    if res.get('message'):
        return { 'error': 1, 'text': res['message'] }
    else:
        user = res['user']
        _core_user._update_password(user, new_password)

        return { 'text': 'Password is successfully updated!' }


@frappe.whitelist(allow_guest=True)
def forgot_password(data):
  dat = json.loads(data)
  email = dat.get('email')
  doc = frappe.get_all('Namlifa Member', filters={
            "email": email
        }, fields=['name'])

  # check if member exists
  if len(doc) == 0:
    return { 'error': 1, 'text': 'Account {0} not found.'.format(email)}
  else:
    member = frappe.get_doc('Namlifa Member', doc[0].name)
    if member.application_status == "Approved":
      new_password = random_string(10)
      member.new_password = new_password
      member.flags.ignore_permissions = True
      member.save()
      frappe.sendmail(
        recipients=email,
        subject='Your NAMLIFA account password has been reset',
        template='set_password',
        args={
          'msg': 'Your NAMLIFA account password has been reset. Thank you for your support.',
          'full_name': member.full_name,
          'password': new_password,
          'email': email
        }
      )
      return { 'text': 'An email with temporary credentials will be sent to {0}.'.format(email)}
    elif member.application_status == "Pending":
      return {'error': 1, 'text': 'Application status is currently {0}. An email with credentials will be sent once application is approved'.format(member.application_status)}
    else:
      return { 'error': 1, 'text': 'Application status is currently {0}'.format(member.application_status) }
