from flask import request
from flask_restplus import Resource
from department_api.api.department.services import (
    create_department,
    delete_department,
    update_department,
)
from department_api.api.department.serializers import (
    department,
    department_update,
)
from department_api.api.restplus import api
from department_api.database.models import Department

ns = api.namespace("department", description="operations related to department")


@ns.route("/")
class DepartmentAPI(Resource):
    @api.response(201, "Department successfully created.")
    @api.expect(department)
    def post(self):
        """
        Creates a new department.
        """
        data = request.json
        create_department(data)
        return None, 201

    @api.marshal_list_with(department)
    def get(self):
        """
        Returns list of departments.
        """
        departments = Department.query.all()
        return departments

    @api.expect(department_update)
    def put(self):
        """
        update department data
        """
        data = request.json
        update_department(data)
        return data, 200

    @api.response(200, "Department successfully deleted.")
    @api.expect(department)
    def delete(self):
        """
        Deletes a department
        """
        data = request.json
        delete_department(data)
        return None, 201

