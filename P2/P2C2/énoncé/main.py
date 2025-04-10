# 1.	Demandez à l'utilisateur de saisir une liste de nombres séparés par des virgules#
nombres = input("Saisissez une liste de nombres séparés par des virgules: ")

##2.	Stockez cette valeur dans une variable  nombres.nombresest une chaîne de caractères (str)"""
liste = nombres.split(",")

#"3.	Utilisez la fonctionsplit(explication de la fonction) pour transformer cette chaîne de caractères en une variable de type liste#
print("Liste des nombres:", liste)

##4.	Transformezlisteen une liste d'entiersliste_entiers, en utilisant la fonction  int. Vous devrez convertir chaque élément un par un ! Utilisez une boucle##
liste_entiers = []
for nombre in liste:
    nombre_entier = int(nombre)
    liste_entiers.append(nombre_entier)

##5.	Calculez et affichez la somme des nombres dans la liste##
somme = 0
for nombre in liste_entiers:
    somme += nombre

##6.	Calculez et affichez la moyenne des nombres dans la liste##
Equivalent à:
# somme = sum(liste_entiers)
print("Somme des nombres:", somme)

# Effectuer la moyenne à l'aide de la somme des nombre
moyenne = somme / len(liste_entiers)

print("Moyenne des nombres:", moyenne)

# Trouver combien de nombres de la liste sont supérieurs à la moyenne
nombre_au_dessus_moyenne = 0
for nombre in liste:
    if nombre > moyenne:
        nombre_au_dessus_moyenne += 1
print("Nombre de nombres supérieurs à la moyenne:", nombre_au_dessus_moyenne)

# Equivalent à:
# nombre_au_dessus_moyenne = 0
# idx = 0
# while idx < len(liste_entiers):
#     if liste_entiers[idx] > moyenne:
#         nombre_au_dessus_moyenne += 1
#     idx += 1
# Attention! Il est déconseillé d'utiliser la boucle while pour parcourir une liste.

print("Nombre de nombres pairs:", nombre_au_dessus_moyenne)
