from netmiko import ConnectHandler
from paramiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException

SP_105A = {
    "device_type": "arista_eos",
    "ip": "10.98.0.244",
    "username": "admin",
    "password": "admin123"
}

arista_term0 = ["terminal length 0"]
enable_evpn = ["service routing protocols model multi-agent"]

eos_devices = ['10.98.0.251', '10.98.0.244', '10.98.0.243', '10.98.0.248', '10.98.0.247', '10.98.0.246', '10.98.0.245', '10.98.0.250', '10.98.0.249', '10.98.0.239', 
               '10.98.0.238', '10.98.0.237', '10.98.0.236']

spin_leaf_edge = ['10.98.0.244', '10.98.0.243', '10.98.0.248', '10.98.0.247', '10.98.0.246', '10.98.0.245', '10.98.0.250', '10.98.0.249', '10.98.0.239', '10.98.0.238', 
                  '10.98.0.237', '10.98.0.236']

for device in spin_leaf_edge:
    DEVICE = {
        'device_type': 'arista_eos',
        'ip': device,
        'username': 'admin',
        'password': 'admin123'
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

    print ("Enabling BGP EVPN.")
    output = net_connect.send_config_set(enable_evpn, read_timeout=60)
    print(output)
    net_connect.disconnect