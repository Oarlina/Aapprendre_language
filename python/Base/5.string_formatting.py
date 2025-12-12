name = "John"
age = 23
myList = [1,2,3]

# '%' est remplacer par ce qui est dans la parenthèse dan l'ordre
# %s -> chaine de caractère (ou tout objet pouvant être représenté sous forme de chaîne, comme les nombres)
# %d -> entier
# %.<number of digits>f -> nombres réels comportant un nombre fixe de chiffres à droite des points
# %x ou %X -> Entiers en représentation hexadécimale (minuscules/majuscules)
print ("Hello, %s!" % name)
print ("%s is %d years old." % (name, age))
print ("A list : %s" % myList)


#Exercice :
data = ("John", "Doe", 53.44)
format_string = "Hello"

# Afficher "Hello John Doe. Your current balance is $53.44."
print ("%s %s %s. Your current balance is $%s." % (format_string, data[0], data[1], data[2]))