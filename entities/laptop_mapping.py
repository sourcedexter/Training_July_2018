from peewee import *
from properties import *
from employee import Employee
from laptop import Laptop
from laptop_status import Laptop_Status

db = MySQLDatabase(db_name, user=db_user, password=db_password, host=db_host)


class Laptop_mapping:
    default_id = PrimaryKeyField(primary_key=True)
    employee_id = ForeignKeyField(Employee, rerlated_name='mappings', null=True)
    laptop_id = ForeignKeyField(Laptop, related_name='laptops', null=True)
    issue_date = DateTimeField(null=True)
    status_id = ForeignKeyField(Laptop_Status, related_name='status', null=True)


    class Meta:
        database = db

