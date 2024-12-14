"""
3.1 Implement device management and monitoring using Netmiko
"""

# Python Modules
from ipaddress import IPv4Address as IPv4, IPv6Address as IPv6
from os import getenv
from re import search

# Third-Party Modules
from netmiko import BaseConnection, ConnectHandler

type HostT = IPv4 | IPv6 | str

TEST_HOST1 = getenv('IOS_XE1')
TEST_USER = getenv('IOS_USER')
TEST_PW = getenv('IOS_PW')

def connect_device(host: HostT, port: int, username: str, password: str) -> BaseConnection:
    input_kwargs = {k: v for k, v in locals().items()}
    device = ConnectHandler(**input_kwargs, device_type='cisco_ios')
    return device


def add_loopback(loopback_id: int, host: HostT, port: int, username: str, password: str) -> bool:
    config = [
        f'int loopback{loopback_id}',
        'ip address 10.101.1.101 255.255.255.255',
        'no shut',
    ]
    device = connect_device(host, port, username, password)
    device.enable()
    device.send_config_set(config)

    response = device.send_command('show ip interface brief')

    return bool(search(f'loopback{loopback_id}', response))

if __name__ == '__main__':
    result = add_loopback(1000, TEST_HOST1, 22, TEST_USER, TEST_PW)

    if result:
        print(f'Added loopback 1000 to: {TEST_HOST1}')
    else:
        print(f'Failed to add loopback 1000 to: {TEST_HOST1}')