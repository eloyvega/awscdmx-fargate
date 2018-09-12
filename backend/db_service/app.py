import os

import boto3
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r'*': {'origins': '*'}})

dynamo_table = boto3.resource('dynamodb').Table(os.environ['DYNAMO_TABLE'])


@app.route('/')
def hello():
    return 'DB Service is responding'


@app.route('/new_record', methods=['POST'])
def new_record():
    record = request.get_json()
    print(record)
    response = dynamo_table.put_item(
       Item=record
    )
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        print(response)
        raise Exception
    return jsonify(response)


@app.route('/all_records')
def all_records():
    items = []
    response = dynamo_table.scan()
    items += response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items += response['Items']
    sorted_response = sorted(items, key=lambda k: k['timestamp'], reverse=True)
    return jsonify(sorted_response)
