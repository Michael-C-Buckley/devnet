"""
3.2 Construct a Python script using ncclient that uses NETCONF to manage and monitor an IOS XE device
3.5 Configure a subscription for model driven telemetry on an IOS XE device (CLI, NETCONF, and RESTCONF)
"""

from ncclient import manager
import xmltodict

from ipaddress import IPv4Address as IPv4, IPv6Address as IPv6
from os import getenv
from copy import copy
from re import search

type HostT = IPv4 | IPv6 | str

TEST_HOST1 = getenv('IOS_XE1')
TEST_USER = getenv('IOS_USER')
TEST_PW = getenv('IOS_PW')



def get_interface():
    """
    Get the info from the test VM's uplink interface
    Example is Cat8000V with only 1 gigabit ethernet vNIC
    """
    router = {
        'host': TEST_HOST1,
        'port': 830,
        'username': TEST_USER,
        'password': TEST_PW,
        'hostkey_verify': False,
    }

    server_capabilities = None

    int_filter = """
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" type="subtree">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>GigabitEthernet1</name>
            </interface>
        </interfaces>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>GigabitEthernet1</name>
            </interface>
        </interfaces-state>
    </filter>

    """.strip()

    with manager.connect(**router) as session:
        server_capabilities = copy(session.server_capabilities)
        raw_response = session.get(int_filter)

        # collect the data into parsed variables showcasing their structure
        response = xmltodict.parse(raw_response.xml)['rpc-reply']['data']
        stats = response['interfaces-state']['interface']
        config = response['interfaces']['interface']
        return response

if __name__ == '__main__':
    get_interface()