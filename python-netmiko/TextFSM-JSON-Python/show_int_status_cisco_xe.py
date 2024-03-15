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

# use_textfsm=True returns interfaces variable as a Python dictionary. json.dump() puts the output of show interfaces status into json format. indent=2 indents by 2. f is
# for Python3 format function.
for switch in switches:
    connect = ConnectHandler(**switch)
    interfaces = connect.send_command('show interfaces status',use_textfsm=True)
    print(json.dumps(interfaces, indent=2))
    for interface in interfaces:
        if interface['vlan'] == '1':
            print(f"{interface['port']} is in vlan 1")
connect.disconnect