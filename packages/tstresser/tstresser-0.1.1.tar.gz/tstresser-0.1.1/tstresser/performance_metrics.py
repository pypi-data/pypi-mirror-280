class PerformanceMetrics:
    """
    PerformanceMetrics class to record and print performance metrics
    """
    def __init__(self):
        self.responses = []
        self.errors = []

    def record_response(self, status_code, response_time):
        self.responses.append((status_code, response_time))

    def record_error(self, error):
        self.errors.append(error)

    def print_summary(self):
        total_requests = len(self.responses) + len(self.errors)
        success_requests = len(self.responses)
        failed_requests = len(self.errors)
        avg_response_time = sum(response_time for _, response_time in self.responses) / success_requests if success_requests else 0

        print(f"Total requests: {total_requests}")
        print(f"Successful requests: {success_requests}")
        print(f"Failed requests: {failed_requests}")
        print(f"Average response time: {avg_response_time:.2f} seconds")
