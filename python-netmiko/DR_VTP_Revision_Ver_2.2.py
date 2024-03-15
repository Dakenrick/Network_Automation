from netmiko import ConnectHandler

DR_01 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.164.204',
    'username': 'cisco',
    'password': 'cisco'
}

all_devices = [DR_01]

n = 999

revisionrequest = int(input("Increase VTP Revision Number By: "))
revisionamount = revisionrequest//2

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for count in range (revisionamount):
       print ("Creating VLAN " + "999")
       config_commands = ['vlan ' + str(n), 'name Ansible_' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print(output) 
       print ("Deleting VLAN " + "999")
       config_commands = ['no vlan ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print(output)
