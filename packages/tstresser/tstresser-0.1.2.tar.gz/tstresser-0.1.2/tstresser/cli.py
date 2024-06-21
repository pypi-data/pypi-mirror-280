import argparse
import json

from .load_generator import LoadGenerator
from .request_customization import RequestCustomization


def main():
    parser = argparse.ArgumentParser(description='API Stress Tester')
    parser.add_argument('--url', required=True, help='API endpoint to test')
    parser.add_argument('--method', default='GET', help='HTTP method')
    parser.add_argument('--concurrent_users', type=int, default=10, help='Number of concurrent users')
    parser.add_argument('--request_rate', type=int, default=1, help='Requests per second')
    parser.add_argument('--headers', help='Custom headers as JSON string')
    parser.add_argument('--payload', help='Custom payload as JSON string')
    args = parser.parse_args()

    request_customization = RequestCustomization()
    if args.headers:
        try:
            headers = json.loads(args.headers)
        except json.JSONDecodeError:
            print('headers must be a valid JSON string')
            return
        request_customization.set_headers(headers)
    if args.payload:
        try:
            payload = json.loads(args.payload)
        except json.JSONDecodeError:
            print('payload must be a valid JSON string')
            return
        request_customization.set_payload(payload)

    load_gen = LoadGenerator(args.url, args.method, args.concurrent_users, args.request_rate, request_customization)
    load_gen.start_test()

if __name__ == '__main__':
    main()
