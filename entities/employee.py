import os
from peewee import *
from playhouse.db_url import connect

import properties	

db=_mysql.connect(db_host,db_user,db_password,db_name)

class Employee(Model):
	employee_id = PrimaryKeyField(null=False)
	employee_name = CharField(null=False)
	employee_team = CharField(null=False)
    class Meta:
        database = db