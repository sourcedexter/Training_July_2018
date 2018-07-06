import os
from peewee import *
from playhouse.db_url import connect
from properties import *


db =_mysql.connect(db_host,db_user,db_password,db_name)
class Laptop_mapping:
    default_id = PrimaryKeyField(primary_key=True)
    employee_id = ForeignKeyField(Employee, rerlated_name='mappings')
    laptop_id = ForeignKeyField(Laptop, related_name='laptops')
    issue_date = DateTimeField()
    status_id = ForeignKeyField(Laptop_status, related_name='status')
    class Meta:
        database = db

