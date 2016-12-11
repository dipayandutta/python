'''
   Purpose :- Get familer with JSON with python , for extracting information
  
   Author :- Dipayan Dutta
'''

import urllib2
import json

def main():
	#Taking the city name as user input 
	city_name= raw_input("Enter Ciry Name ==>  ")
	#creating the URL with appending the city name
	urlData = "http://maps.googleapis.com/maps/api/geocode/json?address={}".format(city_name)
	#print urlData
	#using urllib2 to open the url
	webUrl = urllib2.urlopen(urlData)	
	#print webUrl.getcode()
	#checking and matching the code , if it 200 which is OK response then go to function 
	if (webUrl.getcode()==200):
		data = webUrl.read()
		getlatlong(data,city_name)
	else:
		print "Got Some Error {}".format(webUrl.getcode())

#my getlatlong() function for extracting information 

def getlatlong(data,city_name):
	information = json.loads(data)
	for info in information["results"]:
		print info["formatted_address"]
		print str(city_name)+"'s lat and long is {}".format(info["geometry"]["location"])

if __name__ == '__main__':
	main()




