# afficher toutes les notes de l'élèves
studentNotes = [12,18,9,17,3,14]
for note in studentNotes:
    print (note)
print ('')  

# afficher de 1 à 3
for x in range(3):
    print (x)
print('')
#afficher de 0 a 30 avec un pas de 10
for x in range(0,30,10):
    print(x)
print('')

# boucle tant que
count = 0
while count <= 5:
    print (count)
    count +=1
print('')

# afficher : 
# *
# **
# ***
# ****
# break permet d'arreter la boucle
star = "*"
count = 1
while True:
    print(star)
    star += "*"
    count += 1
    if count >= 5:
        break 
print('')

# afficher : 1, 3, 5, 7, 9
# continue va a la fin de la boucle et la recommence
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
print('')


