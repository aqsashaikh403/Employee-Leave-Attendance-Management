# Copyright (c) 2026, Aqsa and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class LeaveRequest(Document):

    def validate(self):
        if getdate(self.to_date) < getdate(self.from_date):
            frappe.throw("To Date cannot be earlier than From Date.")

        self.total_leave_days = (
            getdate(self.to_date) - getdate(self.from_date)
        ).days + 1
