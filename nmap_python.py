# -*- coding: utf-8 -*-

import sys
try:
    import nmap
except:
    sys.exit("[!]Please install namp and then pip nmap")
    
# Argument Validator
if len(sys.argv) != 3:
    sys.exit("Please provide post number and ip address in the argument")

address = str(sys.argv[1])
port = str(sys.argv[2])

scanner = nmap.PortScanner()
scanner.scan(address,port)

print scanner.command_line()
print scanner.scaninfo()
print scanner.all_hosts()
print scanner[address].hostname()
print scanner[address].state()
print scanner[address].all_protocols()
print scanner[address]['tcp'].keys()
#print scanner[address]['tcp'].values()

for port_state in scanner[address]['tcp'].values():
    print "SSH Port Status is ==> " +str(port_state['state'])
    
for host in scanner.all_hosts():
    print "=============================================================="
    print "Host : %s (%s)" %(host,scanner[host].hostname())
    print "Host is : %s" %(scanner[host].state())
    
    for proto in scanner[host].all_protocols():
        print "Port Status Starts Here"
        print "======================="
        print "Protocol: %s "%proto
        
        ports = scanner[host][proto].keys()
        ports.sort()
        for port in ports:
            print "port: %s \t\t state: %s"%(port,scanner[host][proto][port]['state'])
            print "Prodcut :{0}".format(scanner[host][proto][port]['product'])
            print "Version :{0}".format(scanner[host][proto][port]['version'])