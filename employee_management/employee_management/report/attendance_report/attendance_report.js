// Copyright (c) 2026, Aqsa and contributors
// For license information, please see license.txt

frappe.query_reports["Attendance Report"] = {
    "filters": [
        {
            "fieldname": "employee",
            "label": "Employee",
            "fieldtype": "Link",
            "options": "Employee"
        },
        {
         "fieldname":"from_date",
         "label":"From Date",
         "fieldtype":"Date"
        },
        {
        "fieldname":"to_date",
        "label":"To Date",
        "fieldtype":"Date"
       }
      {
    "fieldname": "status",
    "label": "Status",
    "fieldtype": "Select",
    "options": "\nPresent\nAbsent\nHalf Day\nOn Leave"
      }
    ]
};
