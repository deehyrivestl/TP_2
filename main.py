"""
Code de devinette d'un nombre aléatoire.
Nom: Liam Deehy-Rivest
Groupe: 123
"""
import random
nombre_essai = 0



print("Choisissez 2 nombres et je choisirai un nombre au hasard entre les deux."
    " À vous de le deviner...")

def choisir_bornes():
   a = int(input("Choisissez la limite inférieur"))
   b = int(input("Choisissez la limite supérieur"))
   print(f"La limite inférieure est {a} et la limite supérieure est {b}")
   return a, b

def quit_ou_non():
  continuer = input("Voulez-vous faire une autre partie (oui/non?)")
  if continuer == "non":
      print("Merci et au revoir")
      return False


  elif continuer == "oui":
      return True
  else:
      print("Veuillez répondre avec oui ou non")
      return quit_ou_non()

borne_inf, borne_sup = choisir_bornes()
nombre_aleatoire = random.randint(borne_inf, borne_sup)

while True:

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
     reponse = quit_ou_non()
     if not reponse:
         break
     else:
         borne_inf, borne_sup = choisir_bornes()
         nombre_aleatoire = random.randint(borne_inf, borne_sup)
         nombre_essai = 0


