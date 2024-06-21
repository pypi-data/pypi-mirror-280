import requests
import threading
import time

from tqdm import tqdm

from .performance_metrics import PerformanceMetrics
from .monitoring_analysis import MonitoringAnalysis
from .request_customization import RequestCustomization


class LoadGenerator:
    """
    LoadGenerator class to generate load on an API endpoint
    :param url: API endpoint to test
    :param method: HTTP method
    :param concurrent_users: Number of concurrent users
    :param request_rate: Requests per second
    """
    def __init__(self, url, method, concurrent_users, request_rate, request_customization=None):
        self.url = url
        self.method = method
        self.concurrent_users = concurrent_users
        self.request_rate = request_rate
        self.metrics = PerformanceMetrics()
        self.monitoring = MonitoringAnalysis()
        self.request_customization = request_customization or RequestCustomization()

    def send_request(self):
        start_time = time.time()
        try:
            headers = self.request_customization.get_headers()
            payload = self.request_customization.get_payload()
            response = requests.request(self.method, self.url, headers=headers, data=payload)
            response_time = time.time() - start_time
            self.metrics.record_response(response.status_code, response_time)
            self.monitoring.record_data(response_time)
        except requests.RequestException as e:
            self.metrics.record_error(e)

    def start_test(self):
        print(f"Generating load on {self.url} with {self.concurrent_users} concurrent users and {self.request_rate} requests per second...")
        threads = []
        for _ in tqdm(range(self.concurrent_users)):
            thread = threading.Thread(target=self.send_request)
            threads.append(thread)
            thread.start()
            time.sleep(1 / self.request_rate)

        for thread in threads:
            thread.join()
        
        self.metrics.print_summary()
        self.monitoring.plot_data()
