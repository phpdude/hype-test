# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask.ext.cors import CORS

from rest import Users, Providers, Vehicles, UsersList, ProvidersList, VehiclesList

app = Flask(__name__)
api = Api(app)

# CORS package
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/test')
def test():
    return 'yeah12345'


cors = CORS(app, resources={r"/*": {"origins": "*"}})

api.add_resource(Users, '/users/<int:key_id>')
api.add_resource(UsersList, '/users')

api.add_resource(Providers, '/providers/<int:key_id>', '/providers')
api.add_resource(ProvidersList, '/providers')

api.add_resource(Vehicles, '/vehicles/<int:key_id>')
api.add_resource(VehiclesList, '/vehicles')

if __name__ == '__main__':
    app.run()
