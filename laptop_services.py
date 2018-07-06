from peewee import *
from flask import Flask
from flask_cors import CORS
from laptop import Laptop
from employee import Employee
from laptop_mapping import Laptop_mapping
import datetime


def create_laptop_employee_map(employee_id, laptop_id, status_id):
    """
    populate laptop_mapping table

    :param employee_id:
    :param laptop_id:
    :param status_id:
    :return:
    """
    try:
        mapping = Laptop_mapping(employee_id=employee_id, laptop_id=laptop_id, status_id=status_id, issue_date=datetime.date.now())
        mapping.save()
    except:
        print("invalid parameters or all parameters not specified")


def add_employee_details(employee_id, employee_name, employee_team):
    """
    populate employee table
    :param id:
    :param name:
    :param service:
    :return:
    """
    try:
        Employee.get_by_id(employee_id)
    except DoesNotExist:
        employee_obj = Employee(employee_id=employee_id, employee_name=employee_name, employee_team=employee_team)
        employee_obj.save()


def add_laptop(laptop_id, ram, gpu, os, company, storage):
    
    
    """
    adds laptop details to the Laptop table
    
    """
    try:
        
        lap_details=Laptop.create(laptop_id=laptop_id, ram=ram, gpu=gpu, os=os, company=company, storage=storage)
        lap_details.save()
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
