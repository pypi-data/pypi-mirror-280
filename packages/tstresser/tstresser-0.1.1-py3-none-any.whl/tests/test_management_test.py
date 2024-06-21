import datetime
import unittest
from tstresser.management_test import ManagementTest

class TestManagementTest(unittest.TestCase):
    def test_schedule_test(self):
        test_management = ManagementTest()
        test = {'name': 'Test 1'}
        time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        test_management.schedule_test(test, time)
        self.assertIn((test, time), test_management.get_tests())

if __name__ == '__main__':
    unittest.main()
