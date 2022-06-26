from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from bs import create_table
app = Flask(__name__)

api = Api()


class Import(Resource):
    def post(self):
        json_data = request.get_json()
        create_table(json_data)



api.add_resource(Import, "/imports")
api.init_app(app)
if __name__ == '__main__':
    app.run(debug=True, port=3000, host='127.0.0.1')
