'''
	Author  = Dipayan Dutta 
	Purpose = Extract the weather condition of kolkata from the json file 
'''
import json

filename = 'kolkata_today.json'

def weather_today(filename):

	with open(filename,'r') as weather_file:
		data = json.load(weather_file)

		for info in data['list']:
			print "City Name ==> {}".format(info['name'])
			print "Longitude ==> {}".format(info['coord']['lon'])
			print "Latitude  ==> {}".format (info['coord']['lat'])
			print "Wind Speed ==> {}".format(info["wind"]['speed'])
			print "Wind Speed Angle ==> {}".format(info['wind']['deg'])
			temp_min_kelvin = info['main']['temp_min']
			temp_max_kelvin = info['main']['temp_max']

	temp_min_farenhite = temp_min_kelvin * 9/5 - 459.67
	temp_max_farenhite = temp_max_kelvin * 9/5 - 459.67

	temp_min_cel = (temp_min_farenhite-32) * 5/9
	temp_max_cel = (temp_max_farenhite-32) * 5/9

	print "Min. Temparature of Today ==> {}".format(temp_min_cel)
	print "Max. Temparature of Today ==> {}".format(temp_max_cel)

if __name__ == '__main__':
	weather_today(filename)