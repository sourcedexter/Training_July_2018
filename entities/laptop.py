from peewee import *
from properties import *
db=MySqlDatabase(db_name, **{'db_user':db_user, 'db_password':db_password})

class Laptop(Model):
    laptop_id=CharField(primary_key=True)
    ram=IntegerFied(null=False)
    gpu=BooleanField(null=True)
    os=CharField(null=False)
    company=Charfield(null=False)
    storage=IntegerField(null=False)
    
    
    class Meta:
        database=db
        
    