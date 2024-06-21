import json


class RequestCustomization:
    """
    Class to customize the request headers and payload
    """
    def __init__(self):
        self.headers = {}
        self.payload = None

    def set_headers(self, headers):
        self.headers.update(headers)

    def set_payload(self, payload):
        self.payload = json.dumps(payload)

    def get_headers(self):
        return self.headers

    def get_payload(self):
        return self.payload
