from flask_restplus import fields
from department_api.api.restplus import api

department = api.model(
    "department",
    {"name": fields.String(required=True, description="department name"),},
)

department_update = api.model(
    "department_update",
    {
        "department_name": fields.String(
            required=True, description="existing department name"
        ),
        "new_department_name": fields.String(
            required=True, description="updated_department name"
        ),
    },
)

employee = api.model(
    "employee",
    {
        "name": fields.String(required=True, description="employee name"),
        "department_name": fields.String(required=True, description="department.name"),
    },
)

employee_department = api.inherit(
    "employee and department mapping",
    department,
    {"department": fields.List(fields.Nested(department))},
)

