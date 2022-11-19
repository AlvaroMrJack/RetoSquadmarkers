import ast
import math
import random
import requests
from json import loads
from flask_mongoengine import MongoEngine
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, fields, marshal_with

from db.models import ChistesCollection

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'RetoDB',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)

CHUCKNORRIS_URL = 'https://api.chucknorris.io/jokes/random'
ICANHAZDADJOKE = 'https://icanhazdadjoke.com'
LIST_POSSIBLE_VALUES = ['Chuck', 'Dad']

resources_fields ={
    'number': fields.Integer,
    'chiste_texto': fields.String
}

def get_random_chiste(path_param = None):
    try:
        payload={}
        headers = {}
        final_url = None
        final_data = None

        if path_param is None:
            api_election = random.choice(LIST_POSSIBLE_VALUES)
        elif path_param is not None:
            api_election = path_param

        if api_election == LIST_POSSIBLE_VALUES[0]:
            final_url = CHUCKNORRIS_URL
        elif api_election == LIST_POSSIBLE_VALUES[1]:
            final_url = ICANHAZDADJOKE
            headers = {
               'Accept': 'application/json'
            }

        response = requests.request("GET", final_url, headers=headers, data=payload)

        if response.ok:
            if api_election == LIST_POSSIBLE_VALUES[0]:
                final_data = response.json()['value']
            elif api_election == LIST_POSSIBLE_VALUES[1]:
                final_data = response.json()['joke']
        else:
            final_data = 'Error ocurrido al consumir API'

        return final_data
    except Exception as e:
        print(e)

def generate_new_id_to_collection():
    len_collection = None
    get_data = ChistesCollection.objects
    len_collection = len(get_data)
    new_id = len_collection + 1
    return new_id

class Chistes(Resource):
    def get(self, path_param = None):
        data_return = None

        if path_param is None:
            data_return = get_random_chiste()
        elif path_param == LIST_POSSIBLE_VALUES[0]:
            data_return = get_random_chiste(path_param)
        elif path_param == LIST_POSSIBLE_VALUES[1]:
            data_return = get_random_chiste(path_param)
        else:
            data_return = 'El valor ingresado ´{}´ es incorrecto. Este valor debe ser {} o {}.'.format(path_param, '“Chuck”', '“Dad”')

        return jsonify(data_return)

    @marshal_with(resources_fields)
    def post(self):
        # guardará en una base de datos el chiste (texto pasado por parámetro)
        data_return = None
        if request.json:
            request_data = loads(request.data)
            if 'chiste_texto' in [*request_data.keys()]:
                new_id = generate_new_id_to_collection()
                chiste = request_data['chiste_texto']
                nuevo_chiste = ChistesCollection(number=new_id, chiste_texto=chiste).save()
                data_return = 'El chiste ´{}´ fue creado con éxito!'.format(chiste)
            else:
                data_return = 'Se debe enviar un objeto tipo JSON en el body de la petición con la key ´chiste_texto´.'
        else:
            data_return = 'El objeto de entrada debe ser tipo JSON.'
            
        return jsonify(data_return)

    @marshal_with(resources_fields)
    def put(self):
        # actualiza el chiste con el nuevo texto sustituyendo al chiste indicado en el parámetro “number”
        try:
            data_return = None
            if request.json:
                request_data = loads(request.data)
                if 'number' in [*request_data.keys()]:
                    if 'chiste_texto' in [*request_data.keys()]:
                        ChistesCollection.objects.get(number=request_data['number']).update(chiste_texto=request_data['chiste_texto'])
                        data_return = 'El chiste número ´{}´ fue actualizado con éxito con el siguiente chiste: ´{}´'.format(request_data['number'], request_data['chiste_texto'])
                    else:
                        data_return = 'El objeto de entrada no tiene la key ´chiste_texto´'
                else:
                    data_return = 'El objeto de entrada no tiene la key ´number´'
            else:
                data_return = 'El objeto de entrada debe ser tipo JSON.'
            return jsonify(data_return)
        except Exception as e:
            return "Error \n %s" % (e)

    def delete(self, number):
        # elimina el chiste indicado en el parametro number
        data_return = None
        ChistesCollection.objects.get(number=number).delete()
        data_return = 'El chiste número ´{}´ fue eliminado con éxito!'.format(number)
        return jsonify(data_return)

class Calculos(Resource):
    def get(self, numbers = None, number = None):
        data_return = None
        
        parser = reqparse.RequestParser()
        parser.add_argument('numbers', type=list)

        if numbers is not None:
            numbers = ast.literal_eval(numbers)
            if type(numbers) is list:
                if len(numbers) >= 2:
                    data_return = math.lcm(*numbers)
                else:
                    data_return = 'La lista entregada debe tener al menos 2 valores'
        elif type(number) is int:
            data_return = number + 1

        return jsonify(data_return)
    
api.add_resource(Calculos, '/calculos/<numbers>', '/calculos/<int:number>', endpoint = 'calculos')
api.add_resource(
    Chistes
    , '/chistes'
    , '/chistes/<string:path_param>'
    , '/post_chiste'
    , '/update_chiste'
    , '/delete_chiste/<int:number>'
)



if __name__ == '__main__':
    app.run(debug=True)