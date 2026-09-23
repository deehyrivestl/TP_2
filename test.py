"""
Code de devinette d'un nombre
Nom: Liam Deehy-Rivest
Groupe: 123
"""
import random
nombre_essai = 0
quit = False
global a
global b


print("Choisissez 2 nombres et je choisirai un nombre au hasard entre les deux."
     " À vous de le deviner...")

def choisir_bornes():
    a = int(input("Choisissez la limite inférieur"))
    b = int(input("Choisissez la limite supérieur"))



def quit_ou_non():
   global nombre_essai
   global quit
   global nombre_aleatoire
   continuer = input("Voulez-vous faire une autre partie (oui/non?)")
   if continuer == ("non"):
       print("Merci et au revoir")
       quit = True
   elif continuer == ("oui"):
       quit = False
       print("Choisissez 2 nombres et je choisirai un nombre au hasard entre les deux."
             " À vous de le deviner...")
       choisir_bornes()
       nombre_essai = 0
   else:
       print("Veuillez répondre avec oui ou non")

choisir_bornes()
limite_inf = choisir_bornes(a)
nombre_aleatoire = random.randint(a, b)

while quit == False:
  essai = int(input("Merci. Entrez votre tentative:"))
  if essai > nombre_aleatoire:
      print(f"Mauvais choix, le nombre est plus petit que {essai} "
            "Entrez votre essai :_")
      nombre_essai += 1
  elif essai < nombre_aleatoire:
      print(f"Mauvais choix, le nombre est plus grand que {essai}"
            "Entrez votre essai :_")
      nombre_essai += 1
  elif essai == nombre_aleatoire:
      (print("Bravo! Bonne réponse"))
      nombre_essai += 1
      print(f"Vous avez réussi en {nombre_essai} essai(s)")
      quit_ou_non()

