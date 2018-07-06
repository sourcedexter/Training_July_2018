import os
from peewee import *
from playhouse.db_url import connect

from properties import *

db=_mysql.connect(db_host,db_user,db_password,db_name)

class Employee(Model):
    employee_id = PrimaryKeyField(primary_key=True)
    employee_name = CharField(null=False)
    employee_team = CharField(null=False)
    class Meta:
        database = db