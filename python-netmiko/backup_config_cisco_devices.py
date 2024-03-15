from netmiko import ConnectHandler
from paramiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException
import time
import datetime

home_dir = 'G:/My Drive/B1 NMCI Project/Documentation/JAXS/Configs/Backup_Configs/'

PR_01 = '172.20.200.1'
PR_02 = '172.20.200.2'
IOS_XR = ['172.20.200.1', '172.20.200.2']
OS_01 = '172.20.200.3'
IS_02 = '172.20.200.9'
DR_01 = '172.20.200.11'
IR_01 = '172.20.200.15'
IR_02 = '172.20.200.14'
OR_01 = '172.20.200.13'
OR_02 = '172.20.200.12'
OM_01 = '172.20.200.17'
MS_01 = '172.20.200.252'
MS_02 = '172.20.200.251'
PS_01 = '172.20.200.33'
IOS_XE = ['172.20.200.3', '172.20.200.9', '172.20.200.11', '172.20.200.15', '172.20.200.14', '172.20.200.13', '172.20.200.12', '172.20.200.17', '172.20.200.252', 
          '172.20.200.251', '172.20.200.33']
TEST = ['192.168.1.100', '192.168.1.101']

# Run against IP list for IOS_XR devices.
TNOW = datetime.datetime.now().replace(microsecond=0)
for IP in TEST:
    DEVICE = {
        'device_type': 'cisco_xe',
        'ip': IP,
        'username': 'cisco',
        'password': 'cisco123'
    }
    print('\n ### Connecting to ' + IP.strip() + '### \n')
    try:
        net_connect = ConnectHandler(**DEVICE)

    except AuthenticationException:
        print('Authentication Failure.')
        continue

    except SSHException:
        print('Make sure SSH is enabled.')
        continue
    
    print('Starting config backup ' + str(TNOW))
    output = net_connect.send_command('show run')
    SAVE_FILE = open(home_dir + 'JAXS_' + IP + '.txt', 'w')
    SAVE_FILE.write(output)
    SAVE_FILE.close
    print('\n Finished backing up config \n')