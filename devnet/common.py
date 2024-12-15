"""
DevNet Training Common
"""

from ipaddress import IPv4Address as IPv4, IPv6Address as IPv6
from os import getenv

type HostT = IPv4 | IPv6 | str

TEST_HOST1 = getenv('IOS_XE1')
TEST_USER = getenv('IOS_USER')
TEST_PW = getenv('IOS_PW')

STANDARD_HEADERS = {
    'Accept': "application/yang-data+json",
    'Content-Type': "application/yang-data+json",
}