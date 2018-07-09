from flask import Flask
import peewee
from flask_cors import CORS
from laptop_services import *
from flask import request
from entities.laptop_status import Laptop_Status
import json

app = Flask(__name__)
CORS(app)
print("33333333333333333333333333333333333333333333333333333333")
db = MySQLDatabase(db_name, user=db_user, password=db_password, host=db_host)
# create_tables()
print("vwjvWHJBCSVBDVBFDZVBDZMVBMVBMHV")


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


if __name__ == "__main__":
    # debug = True
    app.run()
