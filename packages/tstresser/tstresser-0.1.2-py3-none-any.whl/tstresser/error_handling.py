class ErrorHandling:
    def __init__(self):
        self.retries = 3

    def handle_error(self, fn: callable):
        """
        Retry the function fn for self.retries times before raising the exception
        :param fn: function to be executed
        :return: result of the function fn
        """
        for attempt in range(self.retries):
            try:
                return fn()
            except Exception as e:
                if attempt == self.retries - 1:
                    raise e
