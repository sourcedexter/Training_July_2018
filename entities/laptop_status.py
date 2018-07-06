from peewee import *
from playhouse.db_url import connect

from properties import *

db= MySQLDatabase(db_name, user = db_user, password = db_password)

class Laptop_Status(Model):
    laptop_status_id = PrimaryKeyField(primary_key=True)
    laptop_status_value = CharField(null=False)
    class Meta:
        database = db