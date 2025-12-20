 #boucle de si ... et si ... et
age = 6
name = "Max"
if age == 6 : #== permet de tester un égalité
    print ("age vaut 6")
elif type(age) == type(int()) : # elif permet de vérifier une égalité qui n'est pas la première
    print ("age est un entier")
else : # else est choisi si aucune des réponse précedente n'était vraie
    print ("age n'est pas 6, ni un entier")

# boucle de if réduite
print ("'%s' vaut t'il 2 ? %s" % (age, age==2))

# boucle de if ou on vérifie que age est un entier valant 6, et si age est l'un des deuage
if age == 6 and type(6)==type(int()):
    print ('age est un entier valant 6')
if age == 6 or type(6)==type(int()):
    print ('age est soit un entier soit il vaut 6')

# on vérifie si le nom est dans la liste
if name in ["Charles", "Max", "Arthur", "Rick"]:
    print ("Le prenom est soit : Charles, Max, Arthur, Rick")
else:
    print ("Le prenom n'est pas : Charles, Max, Arthur, Rick")

# on peux remplacer '==' par 'is'
print (age is name)

# not() inverse l'expression
print ("'not(True)' vaut %s" %(not(True)))