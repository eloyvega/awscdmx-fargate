import os
import uuid
import time
import calendar

import requests
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r'*': {'origins': '*'}})

headers = {'Content-Type': 'application/json'}

db_service_url = os.environ['DATABASE_SERVICE_URL']


@app.route('/')
def hello():
    return 'API is responding'


@app.route('/api/insert_task', methods=['POST'])
def insert_task():
    record = request.get_json()
    record['id'] = str(uuid.uuid4())
    record['timestamp'] = str(calendar.timegm(time.gmtime()))
    response_object = {
        'status': 0,
        'task': record
    }
    url = f'{db_service_url}/new_record'
    try:
        response = requests.post(url, json=record, headers=headers)
        response.raise_for_status()
        response_object['status'] = 200
    except Exception as e:
        print(e)
        response_object['status'] = 400
    return jsonify(response_object)


@app.route('/api/get_tasks')
def get_tasks():
    url = f'{db_service_url}/all_records'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except:
        return []
