try:
	import psycopg2
	import sys
except :
	print "Unable to import modules ..."
	
con = None
try:
	carid = input("Please enter the ID of the car")
	carname = raw_input("Please enter the car name")
	carcode = input("Please enter the car code")
except:
	print "Unable to get the user input"
	
print "You have provided the following information "
print "car ID =-=> "+str(carid)
print "car name ==> "+str(carname)
print "car code ==>" +str(carcode)

try:
	con = psycopg2.connect(dbname="testdb",user="postgres")
	if con:
		print "Database connected"
	else:
		print "Unable to connect Database"
		
	cur = con.cursor()
	update = cur.execute("INSERT INTO cars (ID,NAME,PRICE) VALUES (%s,%s,%s)",(carid,carname,carcode))
	
	con.commit()
	
except psycopg2.DatabaseError ,e :
	print "Database error"
	print e
	
	if con:
		con.rollback()
	
finally:
	if con:
		con.close()
