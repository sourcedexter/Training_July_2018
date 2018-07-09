from laptop_services import *
import json
from flask import Flask, request
import os
import peewee
from flask_cors import CORS
from laptop_services import *
from entities.laptop_status import Laptop_Status


app = Flask(__name__)
create_tables()

@app.route('/employee',methods = ['POST'])
def create_employee():
    try:
        data = request.json
        print (type(data["employee_id"]))
        add_employee_details(data["employee_id"], data["employee_name"], data["employee_team"])
        return "Success", 200

    except:
        print("Something Went Wrong")
        return "Something Went Wrong", 500


@app.route('/mappings', methods=['POST'])
def add_mapping():
    try:

        data = request.json
        lap_stat = Laptop_Status.get(Laptop_Status.laptop_status_id == 1)
        create_laptop_employee_map(data["employee_id"], data["laptop_id"], lap_stat.laptop_status_id)
        message = "success"
        status_code = 200
        return message, status_code

    except:

        message = "not working"
        status_code = 500
        print(" error in creation")
        return message, status_code


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)