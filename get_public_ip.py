import urllib2
import sys
website = sys.argv[1]
protocol_https = "https://"+website
protocol_http = "http://"+website
r =  urllib2.urlopen(protocol_https)
s = urllib2.urlopen(protocol_http)
peer = r.fp._sock.fp._sock.getpeername()
peer_s = s.fp._sock.fp._sock.getpeername()
print("%s connected\n\tIP and port: %s:%d\n\tpeer = %r" % (r.geturl(), peer[0], peer[1], peer))
if peer[1] == peer_s[1]:
    print "Redirection On "
else:
    print("%s connected\n\tIP and port: %s:%d\n\tpeer = %r" % (s.geturl(), peer_s[0], peer_s[1], peer_s))