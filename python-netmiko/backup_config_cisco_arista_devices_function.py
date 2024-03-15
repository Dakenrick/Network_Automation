from netmiko import ConnectHandler
from paramiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException
import time
import datetime

GETVPN_LISP = ['192.168.71.40', '192.168.71.41', '192.168.71.42', '192.168.71.43']
IOS_XE = ['192.168.71.50', '192.168.71.51', '192.168.71.52', '192.168.71.13', '192.168.71.17', '192.168.71.15', '192.168.71.23', '192.168.71.27', '192.168.71.25']
EOS_DEVICES = ['10.98.0.251', '10.98.0.244', '10.98.0.243', '10.98.0.248', '10.98.0.247', '10.98.0.246', '10.98.0.245', '10.98.0.250', '10.98.0.249', '10.98.0.239', 
               '10.98.0.238', '10.98.0.237', '10.98.0.236']
EVE_COLO2_IOS = ['10.98.0.235', '10.98.0.234', '10.98.0.233', '10.98.0.232', '10.98.0.15', '10.98.0.14', '10.98.0.13', '10.98.0.12']
TEST_XE = ['10.98.0.15', '10.98.0.14', '10.98.0.13', '10.98.0.12']
TEST_EOS = ['10.98.0.236']
TYPE_XR = 'cisco_xr'
TYPE_XE = 'cisco_xe'
TYPE_EOS = 'arista_eos'

home_dir = 'C:/Users/Dakenrick/OneDrive/Documents/NextGen Data Systems/B1 NMCI Project/Cisco CML Lab/B1 CML Labs/GET VPN LISP/Backups/'

# Run against IP list for IOS_XR devices.
def BACKUP(TYPE, IP_LIST, USERNAME, PASSWORD):
    TNOW = datetime.datetime.now().replace(microsecond=0)
    for IP in IP_LIST:
        DEVICE = {
            'device_type': TYPE,
            'ip': IP,
            'username': USERNAME,
            'password': PASSWORD
        }
        print('\n ### Connecting to ' + IP + ' ' + str(TNOW) + '### \n')
        try:
            net_connect = ConnectHandler(**DEVICE)
            net_connect.enable()
        
        except AuthenticationException:
            print('Authentication Failure.')
            continue

        except SSHException:
            print('Make sure SSH is enabled.')
            continue
        
        print('Starting config backup ' + str(TNOW))
        output = net_connect.send_command('show run', read_timeout=300)
        SAVE_FILE = open(home_dir + 'GET_VPN_LISP_Lab_' + IP + '.txt', 'w')
        SAVE_FILE.write(output)
        SAVE_FILE.close
        print('\n Finished backing up config \n')

#BACKUP(IOS_XR, TYPE_XR)
#BACKUP(IOS_XR, TYPE_XE)
#BACKUP(TYPE_XE, TEST)
#BACKUP(TYPE_EOS, EOS_DEVICES, 'admin', 'admin123')
#BACKUP(TYPE_XE, EVE_COLO2_IOS, 'admin', 'admin123')
#BACKUP(TYPE_EOS, TEST_EOS, 'admin', 'admin123')
#BACKUP(TYPE_XE, IOS_XE, 'cisco', 'cisco123')
BACKUP(TYPE_XE, GETVPN_LISP, 'cisco', 'cisco')