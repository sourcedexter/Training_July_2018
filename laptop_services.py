from peewee import *
from flask import Flask
from flask_cors import CORS
from laptop import Laptop
from employee import Employee


def add_laptop(laptop_id, ram, gpu, os, company, storage):
    
    
    """
    adds laptop details to the Laptop table
    
    """
    try:
        
        lap_details=Laptop.create(laptop_id=laptop_id, ram=ram, gpu=gpu, os=os, company=company, storage=storage)
        lap_details.save(force_insert=True)
    except:
        print("laptop already exists")
        


def del_laptop(laptop_id):
    
    
    """
    deletes laptop by laptop id
    
    """
    try:
        
       del_laptop=Laptop.get(Laptop.laptop_id==laptop_id)
       del_laptop.delete_instance()
    
    except:
        print("laptop doesnot exist")
        

    
    
    