import unittest
from tstresser.request_customization import RequestCustomization

class TestRequestCustomization(unittest.TestCase):
    def test_set_headers(self):
        request_customization = RequestCustomization()
        headers = {'Content-Type': 'application/json'}
        request_customization.set_headers(headers)
        self.assertEqual(request_customization.get_headers(), headers)

    def test_set_payload(self):
        request_customization = RequestCustomization()
        payload = {"key": "value"}
        request_customization.set_payload(payload)
        self.assertEqual(request_customization.get_payload(), '{"key": "value"}')

if __name__ == '__main__':
    unittest.main()
