 #boucle de si ... et si ... et
x = 6
if x == 6 : #== permet de tester un égalité
    print ("x vaut 6")
elif type(x) == type(int()) : # elif permet de vérifier une égalité qui n'est pas la première
    print ("x est un entier")
else : # else est choisi si aucune des réponse précedente n'était vraie
    print ("x n'est pas 6, ni un entier")