import unittest
from tstresser.load_generator import LoadGenerator

class TestLoadGenerator(unittest.TestCase):
    def test_initialization(self):
        load_gen = LoadGenerator('http://example.com', 'GET', 10, 1)
        self.assertEqual(load_gen.url, 'http://example.com')
        self.assertEqual(load_gen.method, 'GET')
        self.assertEqual(load_gen.concurrent_users, 10)
        self.assertEqual(load_gen.request_rate, 1)

if __name__ == '__main__':
    unittest.main()
