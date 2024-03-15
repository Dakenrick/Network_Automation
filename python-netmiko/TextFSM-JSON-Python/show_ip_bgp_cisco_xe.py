from netmiko import ConnectHandler
import os
import json

OS_01 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.100",
    "username": "cisco",
    "password": "cisco123"
}

IS_02 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "cisco",
    "password": "cisco123"
}

switches = [OS_01, IS_02]

# use_textfsm=True returns interfaces variable as a Python dictionary. json.dump() puts the output of show ip bgp into json format. indent=2 indents by 2
for switch in switches:
    connect = ConnectHandler(**switch)
    prefixes = connect.send_command('show ip bgp',use_textfsm=True)
    print(json.dumps(prefixes, indent=2))