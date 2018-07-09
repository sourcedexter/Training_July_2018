from peewee import *
from flask import Flask
from flask_cors import CORS
from entities.laptop import Laptop
from entities.employee import Employee
from entities.laptop_status import Laptop_Status
from entities.laptop_mapping import Laptop_mapping
from properties import *
from dto.laptops_emp_dto import Details
import datetime

db= MySQLDatabase(db_name, user = db_user, password = db_password)

def create_tables():
    with db:
        db.create_tables([Laptop_Status, Laptop, Employee, Laptop_mapping])


def view_laptop_emp_details(laptop_id = None, emp_id = None):
    """

    :return:
    """
    laptop_emps_objlist = []
    if (laptop_id is not None) and (emp_id is not None):
        try:
            mapping_object = Laptop_mapping.select().where(Laptop_mapping.laptop_id == laptop_id &
                                                           Laptop_mapping.employee_id == emp_id)
            laptop_emps_objlist.extend(extract_laptop_emp_details(mapping_object.laptops, mapping_object.mappings))
        except:
            print("Something Went Wrong")
            laptop_emps_objlist = None

    elif (laptop_id is not None):
        try:
            mapping_object = Laptop_mapping.select().where(Laptop_mapping.laptop_id == laptop_id)
            laptop_emps_objlist.extend(extract_laptop_emp_details(mapping_object.laptops, mapping_object.mappings))

        except:
            print("Something Went Wrong")
            laptop_emps_objlist = None

    elif (emp_id is not None):
        try:
            mapping_object = Laptop_mapping.select().where(Laptop_mapping.employee_id == emp_id)
            laptop_emps_objlist.extend(extract_laptop_emp_details(mapping_object.laptops, mapping_object.mappings))
        except:
            print("Something Went Wrong")
            laptop_emps_objlist = None

    else:
        try:
            mapping_object = Laptop_mapping.select()
            laptop_emps_objlist.extend(extract_laptop_emp_details(mapping_object.laptops, mapping_object.mappings))
        except:
            print("Something Went Wrong")
            laptop_emps_objlist = None

    return laptop_emps_objlist


def extract_laptop_emp_details(laptop_details, employee_details):
        """
        extract the only imp details
        :param laptop_details:
        :param employee_details:
        :return: detail
        """
        object_list =[]
        for each_ele in range(0,len(employee_details)):
            detail_laptop = laptop_details[each_ele]
            detail_employee = employee_details[each_ele]
            detail = Details(detail_laptop.laptop_id, detail_laptop.laptop_ram, detail_laptop.laptop_gpu,
                             detail_laptop.laptop_os, detail_laptop.laptop_company, detail_laptop.laptop_storage,
                         detail_employee.employee_name, detail_employee.employee_team)
            object_list.append(detail)

        return object_list




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
        employee_obj = Employee(employee_name=employee_name, employee_team=employee_team)
        employee_obj.save()


def add_laptop(laptop_id, ram, os, company, storage):
    """
    adds laptop details to the Laptop table
    
    """
    try:
        Laptop.get_by_id(laptop_id)
    except DoesNotExist:
        laptop_obj = Laptop(laptop_id=laptop_id,ram=ram, os=os, company=company, storage=storage)
        laptop_obj.save(force_insert=True)
    except:
        print(" general exception")


def del_laptop(laptop_id):
    
    
    """
    deletes laptop by laptop id
    
    """
    try:
        
       del_laptop=Laptop.get(Laptop.laptop_id==laptop_id)
       del_laptop.delete_instance()
    
    except:
        print("laptop doesnot exist")
