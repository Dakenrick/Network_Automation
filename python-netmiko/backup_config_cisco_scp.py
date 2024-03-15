from netmiko import ConnectHandler
from netmiko import file_transfer 
from netmiko import progress_bar

home_dir = '/home/dakenrick/Documents/Home-Labs/CCNP-Labs/EVE-NG/CCNP-PING-SNMP-SYSLOG-LABS/Backups/'

CCNP_LAB_HOSTS = ['192.168.100.20', '192.168.100.21', '192.168.100.22']

# Run against IP list for CCNP LAB devices.
DEVICE = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.22',
    'username': 'cisco',
    'password': 'Cisco123'
}

net_connect = ConnectHandler(**DEVICE)
print("Connected successfully")

transfer = file_transfer(net_connect,
                         source_file='running-config',
                         dest_file=home_dir + 'running-config',
                         file_system='system:',
                         direction='get',
                         overwrite_file=True,
                         progress4=progress_bar)
print(transfer)
net_connect.disconnect()