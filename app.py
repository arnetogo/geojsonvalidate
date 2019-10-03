#!/usr/bin/env python
from flask import Flask, request, jsonify
import json

from subprocess import Popen,PIPE,STDOUT

app = Flask(__name__)


@app.route("/", methods=['GET'])
def send_error():
    return jsonify(error = 'Method not allowed')


@app.route('/', methods=['POST'])
def get_request():
    payload = request.get_json()
    result = is_geojson(payload)
    return result


def is_geojson(js_data):
    with open('/tmp/data.txt', 'w') as outfile:
        json.dump(js_data, outfile)
    ret = Popen(["gjv", "/tmp/data.txt"],stderr=STDOUT,stdout=PIPE)
    #since the cli does not return proper return codes, we need to check the output
    message = ret.communicate()[0].strip()
    if message == "valid!":
        return jsonify(is_valid_geojson = 'true')
    else:
        return jsonify(is_valid_geojson = 'false', validation_error = message)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=False, port=8080)

