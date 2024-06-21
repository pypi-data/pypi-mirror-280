class ManagementTest:
    """
    This class is responsible for managing tests to be executed.
    """
    def __init__(self):
        self.tests = []

    def schedule_test(self, test, time):
        self.tests.append((test, time))

    def get_tests(self):
        return self.tests
