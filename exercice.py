#!/usr/bin/env python
# -*- coding: utf-8 -*-


PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
from os import path
import pickle
import json

from recettes import add_recipes, print_recipe

# TODO: Définissez vos fonction ici


def compare_file(file1, file2):
    if file1 != file2:
        with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
            for index, line1 in enumerate(f1):
                line2 =f2.readline()
                if line1 != line2:
                    print(f"Les fichiers sont differents! A la ligne {index+1}, on a: ")
                    print(line1)
                    print("Et on a: ")
                    print(line2)
                    break

def copie_file_triple_space(file_old, file_new):
    with open(file_old, encoding="utf-8") as in_file, open(file_new, 'w', encoding="utf-8") as out_file:
        for line in in_file:
            words = line.split()
            out_file.write(line.replace(" ", "   "))


def exercice3(file_path, result_file_path):
    with open(file_path, encoding="utf-8") as f:
        note_percent = f.readlines()
    with open(result_file_path, 'w', encoding="utf-8") as f:
        for note in note_percent:
            for key, value in PERCENTAGE_TO_LETTER.items():
                if value[0]<= int(note)<value[1]:
                    f.write(note.strip() + " " + key + "\n")
                    break


def delete_recipe(recipes):
    name= input("Entrez le nom de la reccette que vous voulez supprimer. \n")
    if name in recipes:
        del recipes[name]
        print("La recette est supprimee! \n")
    else:
        print("La recette n'existe pas! \n")


def exercice4(file_path="./recipe.json"):# .p pour pickle
    if path.exists(file_path):
        recipes= json.load(open(file_path, 'r'))#pickle.load(open(file_path, 'rb'))
    else:
        recipes=dict()
    while True:
        choice=input("Choississez une option: \n a) Ajouter une recette \n b) Modifier une recette \n c) Supprimer une recette \n d) Afficher une recette \n e) Quitter le programme \n").strip()
        #choice=choice.strip() instead of .strip() after input
        if choice == "a":
            recipes = add_recipes(recipes)
        elif choice == "b":
            recipes= add_recipes(recipes)
        elif choice == "c":
            recipes = delete_recipe(recipes) # on recall la fonction creer precedemment
        elif choice == "d":
            print_recipe(recipes)
        elif choice == "e":
            break
        else:
            print("Le choix n'est pas valide!")

    json.dump(recipes, open(file_path, 'w'))#pickle.dump(recipes, open(file_path, 'wb'))





if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compare_file(".\exemple.txt", ".\exemple2.txt")
    copie_file_triple_space(".\exemple2.txt", ".\exemple2_copy.txt")
    exercice3("./notes.txt", "./notes_letter.txt")
    exercice4()
