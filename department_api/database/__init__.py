from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from department_api.database.models import (
        Department,
        Employee,
    )  # noqa

    db.drop_all()
    db.create_all()
