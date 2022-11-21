from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)

@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())

@app.route('/hello', methods=['GET'])
def test():
    return {'msg': 'hello world!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # run our Flask app
