import re
from netmiko import ConnectHandler

# This script searches B1 PRs for total number of prefixes for each BGP peer. The results are printed to the terminal.

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

PR_01_premise = [PR_01]
PR_02_premise = [PR_02]

PR_01_bgp_peers = ['10.8.68.197', '10.8.68.198', '33.40.61.65', '138.163.106.6', '138.145.251.50', '138.145.251.51', '192.168.255.22', '192.168.255.26', 
                  '192.168.255.41', '192.168.255.45']

PR_02_bgp_peers = ['10.8.68.197', '10.8.68.198', '33.41.61.85', '138.163.106.5']

#Show BGP Peer Recieved routes on PR-01
for devices in PR_01_premise:
    net_connect = ConnectHandler(**devices)

    for peer in PR_01_bgp_peers:
      received_output = net_connect.send_command('show bgp neighbors ' + str(peer) + ' received routes')
      advertised_output = net_connect.send_command('show bgp neighbors ' + str(peer) + ' advertised-routes')
      received_regexoutput = re.search('Processed . prefixes\, . paths', received_output)
      advertised_regexoutput = re.search('Processed . prefixes\, . paths', advertised_output)

      print ("Show bgp neighbors " + str(peer) + " received routes total for PR-01")
      print(received_regexoutput)
      print()

      print ("Show bgp neighbors " + str(peer) + " advertised routes total for PR-01")
      print(advertised_regexoutput)
      print()

#Show BGP Peer Recieved routes on PR-02
for devices in PR_02_premise:
    net_connect = ConnectHandler(**devices)

    for peer in PR_02_bgp_peers:
      received_output = net_connect.send_command('show bgp neighbors ' + str(peer) + ' received routes')
      advertised_output = net_connect.send_command('show bgp neighbors ' + str(peer) + ' advertised-routes')
      received_regexoutput = re.search('Processed . prefixes\, . paths', received_output)
      advertised_regexoutput = re.search('Processed . prefixes\, . paths', advertised_output)

      print ("Show bgp neighbors " + str(peer) + " received routes total for PR-02")
      print(received_regexoutput)
      print()

      print ("Show bgp neighbors " + str(peer) + " advertised routes total for PR-02")
      print(advertised_regexoutput)
      print()

net_connect.disconnect()