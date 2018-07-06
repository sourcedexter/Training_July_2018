from laptop_services import *
import json
from flask import Flask, request
import os
app = Flask(__name__)


@app.route('/employee',methods = ['POST'])
def employee():
    try:
        data = request.data.decode(encoding='UTF-8',errors='strict')
        data=json.loads(data)
        add_employee_details(data["employee_name"], data["employee_team"])

    except:
        print("Something Went Wrong")

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)