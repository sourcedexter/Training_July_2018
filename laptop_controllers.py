from flask import Flask
from flask_cors import CORS
from flask import request
from laptop_services import *
import json


app = Flask(__name__)
CORS(app)


@app.route('/laptop', methods=['DELETE','POST'])
def laptop():
    try:
        if request.method == 'DELETE':
            json_string = request.data.decode('Utf-8')
            laptop_id = json.loads(json_string)
            del_laptop(laptop_id)
            message = "laptop deleted succesfully"
            status_code = 200
            return message, status_code

        elif request.method == 'POST':
            json_string = request.data.decode('Urf-8')
            parameter_obj =  json.loads(json_string)
            add_laptop(parameter_obj['laptop_id'],parameter_obj['ram'],parameter_obj['gpu'],parameter_obj['os'], parameter_obj['company'], parameter_obj['storage'])
            message = "laptop added succesfully"
            status_code = 200
            return message, status_code
    except:
        status_code = 500
        message = "something wrong!!Sorry"
        return message, status_code




