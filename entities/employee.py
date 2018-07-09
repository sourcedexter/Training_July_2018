import os
from peewee import *
from peewee import PrimaryKeyField
from playhouse.db_url import connect

from properties import *

db= MySQLDatabase(db_name, user=db_user, password=db_password)

class Employee(Model):
    employee_id = PrimaryKeyField(primary_key=True)  # type: PrimaryKeyField
    employee_name = CharField(null=False)
    employee_team = CharField(null=False)
    class Meta:
        database = db