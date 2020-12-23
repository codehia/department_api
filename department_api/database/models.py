from . import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Department %r>" % self.name


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    department_id = db.Column(db.Integer, db.ForeignKey("department.id"))
    department = db.relationship(
        "Department", backref=db.backref("departments", lazy="dynamic")
    )

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __repr__(self):
        return "<Employee %r>" % self.name
