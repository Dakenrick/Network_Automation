from netmiko import ConnectHandler
from paramiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException

MS_01 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.100",
    "username": "cisco",
    "password": "cisco123"
}

logging_commands = ["no logging console"]

netconf_restconf = ['ip http secure-server',
                    'netconf-yang',
                    'restconf']

all_devices = ['192.168.71.50', '192.168.71.51', '192.168.71.13', '192.168.71.17', '192.168.71.15', 
               '192.168.71.23', '192.168.71.27', '192.168.71.25']

cml_home_devices = ['192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105']

for device in cml_home_devices:
    DEVICE = {
        'device_type': 'cisco_xe',
        'ip': device,
        'username': 'cisco',
        'password': 'cisco123'
    }

    print('\n ### Connecting to ' + device + '## \n')
    try:
        net_connect = ConnectHandler(**DEVICE)
        net_connect.enable()

    except AuthenticationException:
        print('Authentication Failure.')
        continue
    
    except SSHException:
        print('Make sure SSH is enabled.')
        continue

    print ("Configuring NETCONF and RESTCONF.")
    output = net_connect.send_config_set(netconf_restconf, read_timeout=60)
    output1 = net_connect.send_config_set(logging_commands, read_timeout=60)
    print(output)
    print(output1)
    net_connect.disconnect