from peewee import *
from properties import *
db= MySQLDatabase(db_name, user=db_user, password=db_password)

class Laptop(Model):
    laptop_id=IntegerField(primary_key=True)
    ram=IntegerField(null=False)
    # gpu=BooleanField(null=True)
    os=CharField(null=False)
    company=CharField(null=False)
    storage=IntegerField(null=False)
    
    
    class Meta:
        database=db
        
    