import sys
import time 
import select 
import paramiko

ip = '<ip_address>'
ssh_client = paramiko.SSHClient()

def connect():

	username = '******'
	password = '******'
	port 	 = ** 
	i = 1
	while True:

		print "Trying to connect to %s"%ip
		try:
			
			ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh_client.connect(ip,username=username,password=password,port=port,look_for_keys=False,allow_agent=False)
			print "Connected To the Remote Server %s"%ip

			break
		except paramiko.AuthenticationException:
			print "Authentication Faliure"

		except:
				print "Unable to establish a connection"
				i += 1
		if i == 30:
			print "Unable to make a connection"
			sys.exit(1)

	

def close_connection():
	print "Closeing The connection"
	ssh_client.close()
	print "Connection Closed"

def check_current_dir():
	stdin,stdout,stderr = ssh_client.exec_command("pwd")

	while not stdout.channel.exit_status_ready():
		if stdout.channel.recv_ready():
			rl,wl,xl = select.select([stdout.channel],[],[],0.0)
			if len(rl) > 0:
				print "Current Directory = >",stdout.channel.recv(1024)

def update_cache():
	stdin,stdout,stderr = ssh_client.exec_command("apt-get update")

	while not stdout.channel.exit_status_ready():
		if stdout.channel.recv_ready():
			rl,wl,xl = select.select([stdout.channel],[],[],0.0)
			if len(rl) > 0:
				print "== >",stdout.channel.recv(1024)

def install_package():
	package_name = "python-pip"
	stdin,stdout,stderr = ssh_client.exec_command("apt-get install -y %s"%package_name)

	while not stdout.channel.exit_status_ready():
		if stdout.channel.recv_ready():
			rl,wl,xl = select.select([stdout.channel],[],[],0.0)
			if len(rl) > 0:
				print "installing = >",stdout.channel.recv(1024)

if __name__ == '__main__':
	connect()
	check_current_dir()
	update_cache()
	install_package()
	close_connection()
