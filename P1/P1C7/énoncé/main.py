# 1.	Créez un dictionnaire appelé  fruits
fruits={
  "pomme":"rouge",
  "banane":"jaune",
  "orange":"orange"
}
print(fruits)

# 2.Ajoutez la clé  kiwi  avec la valeur  vert  au dictionnaire fruits  
fruits['kiwi'] = "vert"
print(fruits)

#3.	Accédez à la valeur correspondant à la clé  banane  et stockez-la dans une variable appelée  couleur_banane =
couleur_banane= fruits["banane"]
print (couleur_banane)

#4.	Modifiez la valeur associée à la clé pomme  pour  vert  
fruits["pomme"]="vert"

#5.	Supprimez la clé  banane  du dictionnaire  fruits  
del fruits["banane"]

#6.	Affichez les clés restantes dans le dictionnaire
print(fruits.keys())
