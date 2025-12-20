# pour les chaine de carctères on a ces deux méthodes possible 
str1 = "Bonjour la France !"
str2 = 'Je suis francais <3'

# pour mettre des guillements dans des guillements  ont fait :
quoteInQuote = "Je veux ecrire chat en guillemet : 'chat'"
print (quoteInQuote)

# longueur de la chaine de caractère avec espace et ponctuation
print ("'%s'a %s caracteres. Et dois etre de 19." % (str1, len(str1)))

# donne l'indice de la ponctuation "!"
print ("Le caractere '!' dans '%s' est a l'indice %s." % (str1, str1.index("!")))

# donne le nombre de d'occurence d'une lettre dans une chaine de caractère
print ("Il y a %s 'n' dans '%s'" % (str1.count("n"), str1))

# récupère une chaine de caractère : (nomvariable[indiceDébut:indiceFin])
print ("Dans '%s' il y a :%s" % (str2, str2[6:10]))

# récupère une chaine de caractère : (nomvariable[indiceDébut:indiceFin:pas])
print ("Dans '%s' il y a :%s" % (str2, str2[6:10:2]))

# récupère une chaine de caractère : (nomdevariable[::pas]) -> il prend toute la variable est fais les pas à l'envers
print ("Dans '%s' il y a :%s" % (str2, str2[::-1]))

# je met en majuscule la chaine de caractère 
print ("'%s' en majuscule devient : %s" %(str1, str1.upper()))

# je met en minuscule la chaine de caractere
print ("'%s' en minuscule devient : %s" %(str1, str1.lower()))

# on fait une verification si la chaine de caractere commence par bonjour ou je -> renvoie un bool
print ("'%s' commence par 'Je' ? %s" % (str1, str1.startswith("Je")))

# on fait une verification si la chaine de caractere se termine par bonjour ou je -> renvoie un bool
print ("'%s' se termine par '!' ? %s" % (str1, str1.endswith("!")))

# split permet de faire des séparatin selon un caractère -> renvoie une liste de caractère
print ("%s a un split : %s" % (str1, str1.split(" ")))