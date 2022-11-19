from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_mongoengine import MongoEngine

from config import MONGODBCONFIG
from resources.resources import Chistes, Calculos 

app = Flask(__name__)
api = Api(app)
cors = CORS(app)


app.config['MONGODB_SETTINGS'] = MONGODBCONFIG

db = MongoEngine()
db.init_app(app)
    
api.add_resource(Calculos, '/v1/calculo_mcm', '/v1/calculo_mas_uno')
api.add_resource(
    Chistes
    , '/v1/chistes'
    , '/v1/chistes/<string:path_param>'
    , '/v1/post_chiste'
    , '/v1/update_chiste'
    , '/v1/delete_chiste'
)

if __name__ == '__main__':
    app.run(debug=True)