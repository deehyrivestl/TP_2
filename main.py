"""
Code de devinette d'un nombre
Nom: Liam Deehy-Rivest
Groupe: 123
"""
import random
nombre_aleatoire = random(0,100)
nombre_essai = 0
quit = False


def quit_ou_non:
    finir = input("Voulez-vous continuer? Oui ou non?")
    if finir == ("oui"):
        quit = True
    elif finir == ("non"):
        quit = False
    else:
        print("Veuillez répondre avec oui ou non")
        quit_ou_non()


while quit = False:
    print("Devinez un nombre aléatoire entre 0 et 100")
    essai = input("Entrez votre tentative:")
    if essai > nombre_aleatoire:
        print("Le nombre sélectionné est supérieur au nombre aléatoire womp womp")
    elif essai < nombre_aleatoire:
        print("Le nombre sélectionné est inférieur au nombre aléatoire womp womp")
    elif essai = nombre_aleatoire:
        print("Wow bravo vous avez deviner le nombre!!")
        quit_ou_non()







