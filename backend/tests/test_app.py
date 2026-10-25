import unittest

import app as counter_app


class CounterTests(unittest.TestCase):
    def setUp(self):
        counter_app.counter = 0
        counter_app.app.config['TESTING'] = True
        self.client = counter_app.app.test_client()

    def test_counter_round_trip(self):
        self.assertIn(b'current count is: 0', self.client.get('/').data)
        self.assertEqual(self.client.get('/counter').json, {'counter': 0})
        self.assertEqual(self.client.post('/counter/increment').json, {'counter': 1})
        self.assertEqual(self.client.get('/counter').json, {'counter': 1})

    def test_frontend_cors_preflight(self):
        response = self.client.options('/counter/increment', headers={
            'Origin': 'https://counter.example',
            'Access-Control-Request-Method': 'POST',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Access-Control-Allow-Origin'], 'https://counter.example')
        self.assertIn('POST', response.headers['Access-Control-Allow-Methods'])

    def test_private_network_access_is_not_granted(self):
        response = self.client.options('/counter/increment', headers={
            'Origin': 'https://counter.example',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Request-Private-Network': 'true',
        })
        self.assertNotEqual(response.headers.get('Access-Control-Allow-Private-Network'), 'true')


if __name__ == '__main__':
    unittest.main()
