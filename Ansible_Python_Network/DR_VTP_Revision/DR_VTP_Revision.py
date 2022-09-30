from netmiko import ConnectHandler

DR_01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.200',
    'username': 'cisco',
    'password': 'cisco123'
}

all_devices = [DR_01]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (900,910):
       print ("Creating VLAN " + str(n))
       config_commands = ['vlan ' + str(n), 'name Ansible_' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print(output) 
       print ("Deleting VLAN " + str(n))
       config_commands = ['no vlan ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print(output)
