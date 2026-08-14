# Copyright (c) 2026, Aqsa and contributors
# For license information, please see license.txt

# import frappe


import frappe


def execute(filters=None):
    filters = filters or {}

    columns = [
        {
            "label": "Employee",
            "fieldname": "employee",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 150
        },
        {
            "label": "Attendance Date",
            "fieldname": "attendance_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": "Remarks",
            "fieldname": "remarks",
            "fieldtype": "Data",
            "width": 200
        }
    ]

    conditions = {}

    if filters.get("employee"):
        conditions["employee"] = filters.get("employee")

    if filters.get("from_date"):
        conditions["attendance_date"] = [">=", filters.get("from_date")]

    if filters.get("to_date"):
        conditions["attendance_date"] = ["<=", filters.get("to_date")]

    data = frappe.db.get_all(
        "Attendance",
        filters=conditions,
        fields=[
            "employee",
            "attendance_date",
            "status",
            "remarks"
        ],
        order_by="attendance_date desc"
    )

    return columns, data

