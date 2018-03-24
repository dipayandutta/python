try:
	import urllib2
	import sys
except Exception as e:
	raise e 
	print "[*] Modules not found"
else:
	print "\n"
	print "#========================================#"
	print "[*] Web Information Gathering Programm [*]"
	print "#=========================================="
	print "Author:- Dipayan Dutta"
	print "*********FOR EDUCATIONAL PURPOSE***********"
	
	

finally:
	pass
# Importing nmap Module
try:
	import nmap
except Execution as e :
	print e 
	print "Nmap is not install "
	print "[*]apt-get install nmap"
	print "[*]pip install python-nmap"



def web_engine_details(peer):
	print "[*]IP address : ",peer[0]
	print "[*]Port Number: ",peer[1]

	address = peer[0]
	port = str(peer[1])

	scanner = nmap.PortScanner()
	scanner.scan(address,port)

	for host in scanner.all_hosts():
	    print "=============================================================="
	    print "[*]Host : %s (%s)" %(host,scanner[host].hostname())
	    print "[*]Host is : %s" %(scanner[host].state())
    
	    for proto in scanner[host].all_protocols():
	        print "[*]Port Status Starts Here"
	        print "======================="
	        print "[*]Protocol: %s "%proto
	        
	        ports = scanner[host][proto].keys()
	        ports.sort()
	        for port in ports:
	            print "[*]port: %s \t\t state: %s"%(port,scanner[host][proto][port]['state'])
	            print "[*]Web Server :{0}".format(scanner[host][proto][port]['product'])
	            print "[*]Web Server Version :{0}".format(scanner[host][proto][port]['version'])
	
def ssh_status(peer):

	address = peer[0]
	port = "22" 
	scanner = nmap.PortScanner()
	scanner.scan(address,port)

	for host in scanner.all_hosts():
	        
	    for proto in scanner[host].all_protocols():
	    	print "#========================================#"
	        print "[*]SSH Port Status Scanning On Port 22[*]"
	        print "#========================================#"
	        
	        print "[*]Protocol: %s "%proto
	        
	        ports = scanner[host][proto].keys()
	        ports.sort()
	        for port in ports:
	            print "[*]port: %s \t\t state: %s"%(port,scanner[host][proto][port]['state'])
	            print "[*]Name :{0}".format(scanner[host][proto][port]['name'])
	            print "[*]Conf :{0}".format(scanner[host][proto][port]['conf'])
	            print "[*]Product :{0}".format(scanner[host][proto][port]['product'])
	            print "[*]Version :{0}".format(scanner[host][proto][port]['version'])
	print"==========================================================================="

def ip_extractor(web_address):
	
	open_webaddress = urllib2.urlopen(web_address)
	peer = open_webaddress.fp._sock.fp._sock.getpeername()
	

	web_engine_details(peer)
	ssh_status(peer)

def webaddress_getter():
	website = sys.argv[1]
	protocol_http  = "http://"+website
	
	ip_extractor(protocol_http)


if __name__ == '__main__':
	webaddress_getter()