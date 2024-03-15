from netmiko import ConnectHandler

IR_01 = {
    'device_type': 'cisco_xe',
    'ip': '172.20.200.15',
    'username': 'cisco',
    'password': 'cisco123'
}

connection = ConnectHandler(**IR_01)

IR_Remote_Servers = ['172.20.200.11', '172.20.200.14']

for remote in (IR_Remote_Servers):
    ping_remote = connection.send_command("ping vrf Mgmt-vrf " + str(remote), read_timeout=60)
    print(ping_remote)