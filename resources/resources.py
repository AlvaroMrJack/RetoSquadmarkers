import ast
import math
from json import loads
from flask_cors import cross_origin
from flask import request, Response, jsonify, json
from flask_restful import Resource, request
from common.utils import get_random_chiste, generate_new_id_to_collection, ChistesCollection

from config import LIST_POSSIBLE_VALUES, RESPONSE_MIMETYPE

class Chistes(Resource):

    @cross_origin()
    def get(self, path_param = None):
        try:
            data_return = None

            if path_param is None:
                data_return = get_random_chiste()
            elif path_param == LIST_POSSIBLE_VALUES[0]:
                data_return = get_random_chiste(path_param)
            elif path_param == LIST_POSSIBLE_VALUES[1]:
                data_return = get_random_chiste(path_param)
            else:
                data_return = 'El valor ingresado ´{}´ es incorrecto. Este valor debe ser {} o {}.'.format(path_param, '“Chuck”', '“Dad”')
                return Response(json.dumps([data_return]), status=400, mimetype=RESPONSE_MIMETYPE)

            return Response(json.dumps([data_return]), status=200, mimetype=RESPONSE_MIMETYPE)
        except Exception as e:
            return Response(json.dumps(['Error: {}'.format(e)]), status=400, mimetype=RESPONSE_MIMETYPE)

    def post(self):
        # guardará en una base de datos el chiste (texto pasado por parámetro)
        try:
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
                
            return Response(json.dumps([data_return]), status=200, mimetype=RESPONSE_MIMETYPE)
        except Exception as e:
            return Response(json.dumps(['Error: {}'.format(e)]), status=400, mimetype=RESPONSE_MIMETYPE)

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
            return Response(json.dumps([data_return]), status=200, mimetype=RESPONSE_MIMETYPE)
        except Exception as e:
            return Response(json.dumps(['Error: {}'.format(e)]), status=400, mimetype=RESPONSE_MIMETYPE)

    def delete(self):
        # elimina el chiste indicado en el parametro number
        try:
            data_return = None
            args_keys = request.args.keys()
            args_values = request.args

            if 'number' in [*args_keys]:
                number = int(args_values['number'])
                ChistesCollection.objects.get(number=number).delete()
                data_return = 'El chiste número ´{}´ fue eliminado con éxito!'.format(number)
            else:
                return Response('Query param no válido', status=400, mimetype=RESPONSE_MIMETYPE)

            return Response(json.dumps([data_return]), status=200, mimetype=RESPONSE_MIMETYPE)
        except Exception as e:
            return Response(json.dumps(['Error: {}'.format(e)]), status=404, mimetype=RESPONSE_MIMETYPE)


class Calculos(Resource):
    def get(self):
        try:
            data_return = None
            numbers = []
            number = None

            args_keys = request.args.keys()
            args_values = request.args
            
            if 'numbers' in [*args_keys]:
                numbers = ast.literal_eval(args_values['numbers'])
                if type(numbers) is list:
                    if len(numbers) >= 2:
                        data_return = math.lcm(*numbers)
                    else:
                        data_return = 'La lista entregada debe tener al menos 2 valores'
                else:
                    return Response('El query param numbers debe ser una lista', status=400, mimetype=RESPONSE_MIMETYPE)
            elif 'number' in [*args_keys]:
                number = int(args_values['number'])
                data_return = number + 1
            else:
                return Response('Query param no válido', status=400, mimetype=RESPONSE_MIMETYPE)

            return Response(json.dumps([data_return]), status=200, mimetype=RESPONSE_MIMETYPE)
        except Exception as e:
            return Response(json.dumps(['Error: {}'.format(e)]), status=400, mimetype=RESPONSE_MIMETYPE)
