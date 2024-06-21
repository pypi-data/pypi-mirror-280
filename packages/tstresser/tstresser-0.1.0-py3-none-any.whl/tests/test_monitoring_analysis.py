import unittest
from tstresser.monitoring_analysis import MonitoringAnalysis

class TestMonitoringAnalysis(unittest.TestCase):
    def test_record_data(self):
        monitoring_analysis = MonitoringAnalysis()
        monitoring_analysis.record_data(5)
        self.assertIn(5, monitoring_analysis.data)

if __name__ == '__main__':
    unittest.main()
