from department_api.database import db
from department_api.database.models import Employee, Department


def create_employee_record(data):
    name = data.get("name")
    department_name = data.get("department_name")
    try:
        department = Department.query.filter(Department.name == department_name).first()
        employee = Employee(name, department)
        db.session.add(employee)
        db.session.commit()
        return True
    except Exception as e:
        return False


def update_employee(data):
    department_name = data.get("name")
    department = Department.query.filter(Department.name == department_name).one()
    employee = Employee.query.filter(Employee.name == data.get("employee_name")).one()
    employee.name = data.get("employee_new_name")
    employee.department = department
    db.session.add(employee)
    db.session.commit()


def delete_employee(data):
    name = data.get("name")
    employee = Employee(name).one()
    db.session.delete(employee)
    db.session.commit()


def create_department(data):
    name = data.get("name")
    department = Department(name)
    db.session.add(department)
    db.session.commit()


def update_department(data):
    department_name = data.get("department_name")
    new_name = data.get("new_department_name")
    department = Department(department_name).one()
    if department:
        department.name = new_name
        db.session.add(department)
        db.session.commit()


def delete_department(data):
    name = data.get("department_name")
    department = Department(name).one()
    db.session.delete(department)
    db.session.commit()

