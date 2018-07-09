from flask import Flask
import peewee
from flask_cors import CORS
from laptop_services import *
from flask import request
from laptop_status import Laptop_Status
import json


app = Flask(__name__)
CORS(app)

@app.route('/mappings', methods=['POST'])
def add_mapping():
    try:
        data=request.data.decode("utf-8")
        jobj=json.loads(data)
        lap_stat=Laptop_Status.get(laptop_status_id==0)
        create_laptop_employee_map(jobj['employee_id'], jobj['laptop_id'],lap_stat.laptop_status_id)
        
    except:
        print(" error in creation")
