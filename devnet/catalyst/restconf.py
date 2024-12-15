"""
3.3 Configure device using RESTCONF API utilizing Python requests library
3.5 Configure a subscription for model driven telemetry on an IOS XE device (CLI, NETCONF, and RESTCONF)
"""

# Python Modules
from json import loads

# Third-Party Modules
from requests import get, Response
from requests.auth import HTTPBasicAuth

from devnet.common import HostT, STANDARD_HEADERS, TEST_HOST1, TEST_PW, TEST_USER


def get_interfaces(host: HostT, port: int, user: str, password: str) -> Response:
    base_url = f'https://{host}:{port}/restconf/data/ietf-interfaces:interfaces/interface'

    kwargs = {
        'headers': STANDARD_HEADERS,
        'auth': HTTPBasicAuth(user, password),  # Add Basic Authentication here
        'verify': False,
    }

    return get(base_url, **kwargs)

if __name__ == '__main__':
    response = get_interfaces(TEST_HOST1, 443, TEST_USER, TEST_PW)

    if response.status_code == 200:
        print(f'Interface info for: {TEST_HOST1}')

        body = loads(response.text)

        for interface in body['ietf-interfaces:interface']:
            print(interface['name'])

    else:
        print(f'Unable to obtain data for: {TEST_HOST1}')