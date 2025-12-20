x = 3.2
y = "family"
z = True
x = y + " hhaha " + y 
# donnera :family hhaha family
# permet d'indenter plusieurs variable en une seule ligne
a, b, c = "chat", True, 3.85 

# str : pour du texte
xo = "folle"
# int : pour les entiers
xo = 21
# float : pour les nombre réels
xo = 20.5
# complex : on a d'abord un nombre réel et un nombre imaginaire
xo = 1j
# list : sert à stocker plusieurs éléments dans une seule variable
xo = ["apple", "banana", "berry"]
# tuple : c'est une collection ordonnée et immuable
xo = ("apple", "banana", "berry")
# range : range(start, stop, step) ou range(n), donnera un nombre entre 0 et n-1
xo = range (6) 
# dict : sert à stocker les valeurs de données sous forme de paire clé:valeur
xo = dict (name="John", age=36) 
xo = {"name" : "John", "age" : 36}
# set : permet de sotcker plusieurs éléments dans une seule variable
xo = {"apple", "banana", "berry"}
# forzenset : c'est une version immuable d'un ensemble . On doit utiliser des méthodes de gel dessus
xo = frozenset ( {"apple", "banana", "berry"} )
# bool : permet de dire si une équation ou question est vrai ou fausse
xo = bool (5 == 5)
# bytes : renvoie un objet bytes non modifiable
xo = bytes (5) 
# renvoie un objet tableau d'octets qui peut etre modifiable
xo = bytearray (5) 
# renvoie un objet de vue mémoire à partir d'un objet spécifié
j = memoryview (b"Hello") 
# donnera 72 101 108 111, si je fais j[5] cela me dira que je sors de la dimension 1
print (j[0], j[1], j[2], j[3],j[4])
# none : il ne représente rien 
xo = None