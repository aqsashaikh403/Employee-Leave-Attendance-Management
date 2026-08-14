# Copyright (c) 2026, Aqsa and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class Attendance(Document):

    def validate(self):

        # Prevent duplicate attendance
        existing = frappe.db.exists(
            "Attendance",
            {
                "employee": self.employee,
                "attendance_date": self.attendance_date,
                "name": ["!=", self.name]
            }
        )

        if existing:
            frappe.throw(
                "Attendance already exists for this employee on this date."
            )

        # Validate attendance status
        allowed_statuses = [
            "Present",
            "Absent",
            "Half Day",
            "On Leave"
        ]

        if self.status not in allowed_statuses:
            frappe.throw(
                "Invalid attendance status."
            )
