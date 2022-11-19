import json
import unittest
import requests

MAIN_URL = 'http://127.0.0.1:5000/{}'

class TestAPI(unittest.TestCase):

    endpoint_chistes = MAIN_URL.format('chistes')
    endpoint_post_chiste = MAIN_URL.format('post_chiste')
    endpoint_update_chiste = MAIN_URL.format('update_chiste')
    endpoint_delete_chiste = MAIN_URL.format('delete_chiste')
    endpoint_calculos = MAIN_URL.format('calculos?{}')

    def test_1_endpoint_chistes_solo(self):
        response = requests.get(self.endpoint_chistes)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertGreater(len(response.text), 0)

        print("Test 1 completo")
        print("Mostrando chiste: ", response.text, '\n')

    def test_2_endpoint_chistes_chuck(self):
        endpoint_chistes_chuck = self.endpoint_chistes + '/' + 'Chuck'
        response = requests.get(endpoint_chistes_chuck)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertGreater(len(response.text), 0)

        print("Test 2 completo")
        print("Mostrando chiste: ", response.text, '\n')

    def test_3_endpoint_chistes_dad(self):
        endpoint_chistes_dad = self.endpoint_chistes + '/' + 'Dad'

        response = requests.get(
            endpoint_chistes_dad, 
            headers={
                'Accept': 'application/json'
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertGreater(len(response.text), 0)

        print("Test 3 completo")
        print("Mostrando chiste: ", response.text, '\n')

    def test_4_endpoint_chistes_bad(self):
        endpoint_chistes_bad_text = self.endpoint_chistes + '/' + 'bad_text'

        response = requests.get(endpoint_chistes_bad_text)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.ok)

        print("Test 4 completo")
        print("Mostrando chiste: ", response.text, '\n')

    def test_5_endpoint_post_chiste(self, chiste):

        payload = json.dumps({
            "chiste_texto": chiste
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(self.endpoint_post_chiste, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)

        print("Test 5 completo")
        print('Chiste creado con éxito', '\n')

    def test_6_endpoint_update_chiste(self, number, chiste):

        payload = json.dumps({
            "number": number,
            "chiste_texto": chiste
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.put(self.endpoint_update_chiste, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)

        print("Test 6 completo")
        print('Chiste number {} fue actualizado con éxito'.format(number), '\n')

    def test_7_endpoint_delete_chiste(self, number):

        payload = json.dumps({
            "number": number
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.delete(self.endpoint_delete_chiste, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)

        print("Test 7 completo")
        print('Chiste number {} fue eliminado con éxito'.format(number), '\n')

    def test_8_endpoint_calculos_numbers(self, numbers):

        payload = {}
        headers = {}

        endpoint_query_param = self.endpoint_calculos.format('numbers={}'.format([*numbers]))
        response = requests.get(endpoint_query_param, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        
        mcm = response.text
        
        print("Test 8 completo")
        print('El mínimo común multiplo es: {}'.format(mcm), '\n')

    def test_9_endpoint_calculos_number(self, number):

        payload = {}
        headers = {}

        endpoint_query_param = self.endpoint_calculos.format('number={}'.format(number))
        response = requests.get(endpoint_query_param, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        
        numero_final = response.text
        
        print("Test 9 completo")
        print('El número ingresado {} + 1 es: {}'.format(number, numero_final), '\n')

if __name__ == "__main__":
    try:
        print('\n', 'Comenzando unittest', '\n')
        tester = TestAPI()
        tester.test_1_endpoint_chistes_solo()
        tester.test_2_endpoint_chistes_chuck()
        tester.test_3_endpoint_chistes_dad()
        tester.test_4_endpoint_chistes_bad()

        tester.test_5_endpoint_post_chiste("Un nuevo chiste desde unittest")
        tester.test_6_endpoint_update_chiste(1, "chiste actualizado desde unittest")
        tester.test_7_endpoint_delete_chiste(1)

        tester.test_8_endpoint_calculos_numbers([1,3,6,7])
        tester.test_9_endpoint_calculos_number(10)

        print('\n', 'unittest Finalizado', '\n')
    except Exception as e:
        print('Error: {}'.format(e))