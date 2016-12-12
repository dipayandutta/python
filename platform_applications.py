'''
	Purpose :- To get familer with the platform module of python
				This module is very much useful for getting the 
				information of underlying system .
	
'''
import platform

# to get the python version
print "Python Version {} ".format(platform.python_version())

# to get the python major , minor and patch level version information
print "Python Major Version {} ".format(platform.python_version_tuple()[0])
print "Python Minor Version {} ".format(platform.python_version_tuple()[1])
print "Python PatchLable Version {} ".format(platform.python_version_tuple()[2])
#to get the compiler
print "Python Compiler {} ".format(platform.python_compiler())

#uname and functionallity 
print "UNAME {} ".format(platform.uname())

#to get the system OS type 
print "OS Type {} ".format(platform.uname()[0]) 
print "System OS {} ".format(platform.system())

#To get the kernel version
print "Kernel Version {} ".format(platform.uname()[2])
print "Kernel Version {} ".format(platform.release())

#To the system host name
print "System Host Name {} ".format(platform.uname()[1])
print "System Host Name {} ".format(platform.node())

#To get machine architecture info
print "Machine Architecture {} ".format(platform.machine())

#Make Good output of the architecture

architecture = platform.machine()

if architecture == "x86_64":
	print "64 Bit Machine !!!"

else:
	print "32 Bit Machine"
	
#Another way to get the architecture 
print "System Architecture ",platform.architecture()[0]

#To get the Linux Distribution Details 
print "Linux Distro Name {} ".format(platform.linux_distribution()[0])
print "Distro Version {} ".format(platform.linux_distribution()[1])
print "Version Name {} ".format(platform.linux_distribution()[2])
