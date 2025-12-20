#création de la classe MyClass
class MyClass:
    # variable de la classe
    variable = "blah"
    # ajout d'une méthode
    def function(self):
        print("This is a message inside the class.")

#instance de la classe MyClass
myobjectx = MyClass()
myobjecty = MyClass()

# modification de la variable variable
myobjecty.variable = "yackity"

print(myobjectx.variable)
print(myobjecty.variable)

# j'apelle la methode de l'objet myobjectx
myobjectx.function()


# creation de la classe NumberHolder
class NumberHolder:
    # constructeur de la classe
    # self représente l'objet en cours de création, number la valeur passer au moment de la création de l'objet
    def __init__(self, number):
       self.number = number
    # méthode de la classe 
    def returnNumber(self):
       return self.number
#creation de l'objet var avec comme number 7
var = NumberHolder(7)
print(var.returnNumber()) #Prints '7'



# Exercise : 
# We have a class defined for vehicles. 
# Create two new vehicles called car1 and car2. 
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00
# test code
print(car1.description())
print(car2.description())