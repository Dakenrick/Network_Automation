from netmiko import ConnectHandler
import os
import threading

PR_01 = {
    'device_type': 'cisco_xr',
    'ip': '172.20.200.1',
    'username': 'cisco',
    'password': 'cisco123'
}

PR_02 = {
    'device_type': 'cisco_xr',
    'ip': '172.20.200.2',
    'username': 'cisco',
    'password': 'cisco123'
}

OS_01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.100',
    'username': 'cisco',
    'password': 'cisco123'
}

IS_02 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.101',
    'username': 'cisco',
    'password': 'cisco123'
}

TYPE_EOS = 'arista_eos'
TYPE_XE = 'cisco_xe'
TYPE_XR = 'cisco_xr'
SPINE_01 = ['10.98.0.244']
SPINE_02 = ['10.98.0.243']

# Change home directory variable to match where you will be storing the configuration text files.
home_dir = 'G:/My Drive/B1 NMCI Project/GitLab/Visual Code/ansible/t1_remediation/Python/Test_Files/'
home_dir_01 = 'G:/My Drive/B1 NMCI Project/Network Automation/Python/Test_Files/NRFK_AS_IS/'
home_dir_02 = 'G:/My Drive/NDP Project/EVE-NG/Labs/NDPColo-2-v001/Configs/'

def send_config(TYPE, IP_LIST, FILE):
    for IP in IP_LIST:
        DEVICE = {
            'device_type': TYPE,
            'ip': IP,
            'username': 'admin',
            'password': 'admin123'
        }
        print('Connecting to device ' + IP)
        net_connect = ConnectHandler(**DEVICE)
        result = net_connect.send_config_from_file(config_file=home_dir_02 + FILE, read_timeout=300)
        net_connect.disconnect
        print(result)
        print('Finishing config push and disonnecting from device ' + IP)

# Creating multiple threads for the send_config function then pass arguments.
#t1 = threading.Thread(target=send_config, args=(IR_01, 'nrkf-u00-ir-01.txt',))

# Start threads. 
#t1.start()

# Wait until each thread is completed before moving on to the next task.
#t1.join()

send_config(TYPE_EOS, SPINE_01, 'SP-0001-Base.txt')