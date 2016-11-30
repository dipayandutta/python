#----------------------------------------------------------
#Name :- carInheritance.py
#Purpose :- an example code of inheritance 
#Author :- Dipayan Dutta

#----------------------------------------------------------

class Car (object):
    def __init__(self,name,color):
        self.name = name
        self.color = color
        
    def showModel(self,name):
        self.name = name
        print "Car Model is :"+str(self.name)
        
    def showColor(self,color):
        self.color = color
        print "Car color is :"+str(self.color)
    

class Maruti(Car):
    def showPrice(self,price):
        self.price = (price*12.5)+1000
        print "Car Price is :"+str(self.price)
    

class Tata(Car):
    def showPrice (self,price):
        self.price = (price * 14.5)+5000
        print "Car Price is :"+str(self.price)

class Ashokleyland(Car):
    def showPrice(self,price):
        self.price = (price * 20.5)+12506
        print "Car Price is :"+str(self.price)

class Mahindra(Car):
    def showPrice(self,price):
        self.price = (price *5.52)+12345
        print "Car Price is :"+str(self.price)
        
#car = Car("sx4","red")
#print car
        
carName = raw_input("Enter Car Company").lower()      
carModel = raw_input("Please Enter Car Model")
carColor = raw_input("Please Enter Car Color")
price = input("Please enter car price")

print carName
print carModel
print carColor
print price



#tata = Tata("nano","Electric Blue")
#tata.showModel("nano")
#tata.showColor("Electric Blue")
#tata.showPrice(100000)


if (carName == "tata"):
    tata = Tata(carModel,carColor)
    #print tata
    print "==============================="
    tata.showModel(carModel)
    tata.showColor(carColor)
    tata.showPrice(price)

elif (carName == "maruti"):

    maruti = Maruti(carModel,carColor)
    print "==============================="
    maruti.showModel(carModel)
    maruti.showColor(carColor)
    maruti.showPrice(price)

elif(carName == "ashokleyland"):
    ashok = Ashokleyland(carModel,carColor)
    print "================================="
    ashok.showModel(carModel)
    ashok.showColor(carColor)
    ashok.showPrice(price)

elif(carName == "mahindra"):
    mahindra = Mahindra(carModel , carColor)
    mahindra.showModel(carModel)
    mahindra.showColor(carColor)
    mahindra.showPrice(price)

else:
    print "Not in stock"
    print "Thanks for Query shall update soon!"
