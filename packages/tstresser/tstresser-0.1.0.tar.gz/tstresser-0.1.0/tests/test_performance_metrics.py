import unittest
from tstresser.performance_metrics import PerformanceMetrics

class TestPerformanceMetrics(unittest.TestCase):
    def test_record_response(self):
        metrics = PerformanceMetrics()
        metrics.record_response(200, 0.5)
        self.assertEqual(len(metrics.responses), 1)

    def test_record_error(self):
        metrics = PerformanceMetrics()
        metrics.record_error(Exception('Test error'))
        self.assertEqual(len(metrics.errors), 1)

if __name__ == '__main__':
    unittest.main()
