#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import recettes

# TODO: Définissez vos fonction ici
def comparateur(fichier1, fichier2):
    with open(fichier1, "r") as f1, open(fichier2, "r") as f2:
        for index, line in enumerate(f1):
            ligne = f2.readline()
            if line != ligne:
                print(f"Les fichiers sont différents à la ligne {index + 1}")
                a = str(input("Voulez-vous afficher les lignes? dites OUI ou NON: "))
                if a == "OUI":
                    print(line)
                    print(ligne)
                break

def triple_espace(fichier):
    with open(fichier, "r") as f, open("triple.txt", "w") as c:
        for line in f:
            c.write(line.replace(" ", "   "))

def mention(notes):
    with open(notes, "r") as n, open("mentions.txt", "w") as m:
        liste = n.read().splitlines()

        for elem in liste:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0] <= int(elem) and int(elem) < value[1]:
                    m.write(elem + " " + key + "\n")
                    #faut rajouter un break pour rendre le programme plus efficace
                    break


def exercice4():
    demande = str(input("Souhaitez-vous ajouter, modifier ou supprimer des recettes? \n"))
    recettes.print_recipe()
    if demande == "ajouter":
            l.write(recettes.add_recipes())
    elif demande == "modifier":


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    comparateur("exemple.txt", "exemple.txt")

    triple_espace("exemple.txt")

    mention("notes.txt")
    pass
