from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine

from config import MONGODBCONFIG
from resources.resources import Chistes, Calculos 

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = MONGODBCONFIG

db = MongoEngine()
db.init_app(app)
    
api.add_resource(Calculos, '/calculos', endpoint = 'calculos')
api.add_resource(
    Chistes
    , '/chistes'
    , '/chistes/<string:path_param>'
    , '/post_chiste'
    , '/update_chiste'
    , '/delete_chiste'
)

if __name__ == '__main__':
    app.run(debug=True)