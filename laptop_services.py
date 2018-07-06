from peewee import *
from flask import Flask
from flask_cors import CORS
from laptop import Laptop
from employee import Employee
from laptop_status import Laptop_Status
from laptop_mapping import Laptop_mapping
from properties import *
from laptops_emp_dto import Details

db= MySQLDatabase(db_name, user = db_user, password = db_password)

def create_tables():
    with db:
        db.create_tables([Laptop_Status, Laptop, Employee, Laptop_mapping], True)


def view_laptop_emp_details(laptop_id = None, emp_id = None):
    """

    :return:
    """
    laptop_emps_objlist = []
    if laptop_id:
        try:
            mapping_object = Laptop_mapping.select().where(Laptop_mapping.laptop_id == laptop_id)
            laptop_emps_objlist.extend(extract_laptop_emp_details(mapping_object.laptops, mapping_object.mappings))

        except:
            print("Something Went Wrong")
            laptop_emps_objlist = None

    elif emp_id:
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