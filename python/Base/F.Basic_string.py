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

# récupérer une chaine de caractère selon l'indice de début et de fin
print ("Dans '%s' il y a :%s" % (str2, str2[6:10]))

# 
print ("Dans '%s' il y a :%s" % (str2, str2[6:10:3]))