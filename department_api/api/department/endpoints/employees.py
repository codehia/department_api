from flask import request
from flask_restplus import Resource
from department_api.api.department.services import (
    create_employee_record,
    delete_employee,
    update_employee,
)
from department_api.api.department.serializers import (
    employee,
    employee_department,
)
from department_api.api.restplus import api
from department_api.database.models import Employee

ns = api.namespace("employee", description="operations related to employee")


@ns.route("/")
class EmployeeAPI(Resource):
    @api.response(201, "Employee record successfully created.")
    @api.expect(employee)
    def post(self):
        """
        Creates a new employee.
        """
        data = request.json
        status = create_employee_record(data)
        if status:
            return None, 201
        else:
            return {"message": "fail"}, 500

    @api.marshal_list_with(employee)
    def get(self):
        """
        Returns list of employees.
        """
        employees = Employee.query.all()
        return employees

    @api.expect(employee_department)
    def put(self):
        """
        update employee data
        """
        data = request.json
        update_employee(data)
        return data, 200

    @api.response(200, "Employee successfully deleted.")
    @api.expect(employee)
    def delete(self):
        """
        Deletes a employee
        """
        data = request.json
        delete_employee(data)
        return None, 201

