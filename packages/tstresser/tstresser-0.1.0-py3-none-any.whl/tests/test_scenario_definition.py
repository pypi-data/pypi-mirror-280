import unittest
from tstresser.scenario_definition import ScenarioDefinition

class TestScenarioDefinition(unittest.TestCase):
    def test_add_scenario(self):
        scenario_definition = ScenarioDefinition()
        scenario = {'action': 'GET', 'url': 'http://example.com'}
        scenario_definition.add_scenario(scenario)
        self.assertIn(scenario, scenario_definition.get_scenarios())

if __name__ == '__main__':
    unittest.main()
