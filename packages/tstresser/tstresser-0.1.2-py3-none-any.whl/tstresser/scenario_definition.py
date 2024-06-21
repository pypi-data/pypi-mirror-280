class ScenarioDefinition:
    """
    A class to represent a scenario definition.
    """
    def __init__(self):
        self.scenarios = []

    def add_scenario(self, scenario):
        self.scenarios.append(scenario)

    def get_scenarios(self):
        return self.scenarios
