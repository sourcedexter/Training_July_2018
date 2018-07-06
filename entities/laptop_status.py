import os
from peewee import *
from playhouse.db_url import connect

from properties import *

db=_mysql.connect(db_host,db_user,db_password,db_name)

class Laptop_Status(Model):
    laptop_status_id = PrimaryKeyField(primary_key=True)
    laptop_status_value = CharField(null=False)
    class Meta:
        database = db