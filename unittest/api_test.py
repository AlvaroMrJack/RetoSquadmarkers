import json
import unittest
import requests

MAIN_URL = 'http://127.0.0.1:5000/v1/{}'

class TestAPI(unittest.TestCase):

    endpoint_chistes = MAIN_URL.format('chistes')
    endpoint_post_chiste = MAIN_URL.format('post_chiste')
    endpoint_update_chiste = MAIN_URL.format('update_chiste')
    endpoint_delete_chiste = MAIN_URL.format('delete_chiste?{}')
    endpoint_calculo_mcm = MAIN_URL.format('calculo_mcm?{}')
    endpoint_calculo_mas_uno = MAIN_URL.format('calculo_mas_uno?{}')

    def test_1_endpoint_chistes_solo(self):
        response = requests.get(self.endpoint_chistes)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertGreater(len(response.content), 0)

        response_decode = response.content.decode()

        print("Test 1 completo")
        print(response_decode, '\n')

    def test_2_endpoint_chistes_chuck(self):
        endpoint_chistes_chuck = self.endpoint_chistes + '/' + 'Chuck'
        response = requests.get(endpoint_chistes_chuck)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        self.assertGreater(len(response.content), 0)

        response_decode = response.content.decode()

        print("Test 2 completo")
        print(response_decode, '\n')

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
        self.assertGreater(len(response.content), 0)

        response_decode = response.content.decode()

        print("Test 3 completo")
        print(response_decode, '\n')

    def test_4_endpoint_chistes_bad(self):
        endpoint_chistes_bad_text = self.endpoint_chistes + '/' + 'bad_text'

        response = requests.get(endpoint_chistes_bad_text)

        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.ok)

        response_decode = response.content.decode()

        print("Test 4 completo")
        print(response_decode, '\n')

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

        response_decode = response.content.decode()

        print("Test 5 completo")
        print(response_decode, '\n')

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

        response_decode = response.content.decode()

        print("Test 6 completo")
        print(response_decode, '\n')

    def test_7_endpoint_delete_chiste(self, number):

        payload = {}
        headers = {}

        endpoint_query_param = self.endpoint_delete_chiste.format('number={}'.format(number))

        response = requests.delete(endpoint_query_param, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)

        response_decode = response.content.decode()

        print("Test 7 completo")
        print(response_decode, '\n')

    def test_8_endpoint_calculos_numbers(self, numbers):

        payload = {}
        headers = {}

        endpoint_query_param = self.endpoint_calculo_mcm.format('numbers={}'.format([*numbers]))
        response = requests.get(endpoint_query_param, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        
        response_decode = response.content.decode()
        
        print("Test 8 completo")
        print(response_decode, '\n')

    def test_9_endpoint_calculos_number(self, number):

        payload = {}
        headers = {}

        endpoint_query_param = self.endpoint_calculo_mas_uno.format('number={}'.format(number))
        response = requests.get(endpoint_query_param, headers=headers, data=payload)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.ok)
        
        response_decode = response.content.decode()
        
        print("Test 9 completo")
        print(response_decode, '\n')

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