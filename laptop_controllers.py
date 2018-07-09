from laptop_services import *
import json
from flask import Flask, request
import os

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


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)