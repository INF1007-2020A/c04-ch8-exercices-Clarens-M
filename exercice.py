#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import recettes

# TODO: Définissez vos fonction ici
def comparateur(fichier1, fichier2):
    with open("fichier1", "r") as f1, open("fichier2", "r") as f2:
        for line in f1:
            ligne = f2.readline()
                if line != ligne:
                    print("Les fichiers sont pas exactement les mêmes à la ligne ")

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
