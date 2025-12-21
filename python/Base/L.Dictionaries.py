# je crée un dictionnaire vide
friendNumber = {}

# dictionnaire deja rempli 
blackListPhone = {
    "Pub1" : 744332211,
    "SonarPanel" : 3259485524,
    "WaterHeader" : 3296514958
}

# je rajoute trois valeur nomDuDictionnaire["clé"]=valeur
friendNumber["John"]= 7701020304
friendNumber["Max"]= 711223344
friendNumber["Arthur"]= 710203040

# j'affiche le dictionnaire
print (friendNumber)

# je parcours le dictionnaire -> .items() permet de donner la clé et la valeur
for name,number in blackListPhone.items():
    print ("Phone number of %s is %d" % (name, number))

# je supprime la valeur avec l'indice Arthur puis John
del friendNumber["Arthur"]
print (friendNumber)
friendNumber.pop("John")
print (friendNumber)

# Exercise :
# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here
phonebook["Jake"] = 938273443
phonebook.pop('Jill')
# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")