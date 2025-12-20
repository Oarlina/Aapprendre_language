
# je crée une liste
myList = []

#je rajoute deux valeurs
# .append() ne peux avoir qu'une seul valeur
myList.append(1) 
myList.append("chat")
myList.append(1j)

# je parcours chaque élément de la liste
for x in myList :
    print(x)

# permet d'afficher un élément selon son indice
print ("L'element correspond a l'indice 1 :", myList[1])

# permet d'afficher toutess la liste
print ("My list :", myList)