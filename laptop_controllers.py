from flask import Flask
from flask_cors import CORS
from flask import request
from laptop_services import *
import traceback
import json
import os


app = Flask(__name__)
CORS(app)


create_tables()


@app.route('/laptop', methods=['DELETE','POST'])
def laptop():
    try:
        if request.method == 'DELETE':
            data = request.json
            del_laptop(data['laptop_id'])
            message = "laptop deleted succesfully"
            status_code = 200
            return message, status_code

        elif request.method == 'POST':
            data = request.json
            add_laptop(data["laptop_id"], data["ram"], data["os"], data["company"], data["storage"])
            message = "laptop added succesfully"
            status_code = 200
            return message, status_code
    except:
        traceback.print_exc()
        status_code = 500
        message = "something wrong!!Sorry"
        return message, status_code


if __name__ == '__main__':
   app.debug = True
   app.run()


