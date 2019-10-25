#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCRIPT : 
Parcourt des fichiers html présents dans le répertoire /Langues
Extraction des balises "Language name","UPSID number" et "Alternate names(s)
OUTPUT:
A Json file : "normalisationLangues.json
"""
#librairies nécessaires
import os
import json
#librairie pour parcourir les fichiers html
from bs4 import BeautifulSoup

#premiere partie du chemin des fichiers : le répertoire
nom_repertoire = "Langues/"
#deuxieme partie du chemin : les fichiers du répertoire
liste_fichiers = os.listdir(nom_repertoire)
#liste contenant nos futures dictionnaires {nom balise : contenu balise}
container_json = []

#parcourt des fichiers du répertoire
for fichier in liste_fichiers:
        #récupération de chaque fichier par concaténation Langue/ + nom fichier
        nom_file = nom_repertoire+fichier
        #ouverture en lecture des fichiers
        file = open(nom_file).read()
        #parsing des fichiers
        soup = BeautifulSoup(file, "html.parser")
        #recherche des clefs/valeurs dans les balises <td> du html
        for balise in soup.find_all("td"):
            #recherche d'une balise avec un contenu precis
            if balise.string == "Language name:":
                #on conserve le contenu de la balise suivante
                #car c'est l'information que l'on souhaite retenir
                value_name_language =balise.find_next().string             
            if balise.string == "UPSID number:":
                value_upsid =balise.find_next().string
            if balise.string == "Alternate name(s):":
                if balise.find_next().string == None:
                    value_alt_name = "No alternate name(s)"
                else:
                    value_alt_name = balise.find_next().string
               
        #récupération des données dans des dictionnaires, ajout dans la liste           
        container_json.append({"Language name ": value_name_language ,
                                   "UPSIDE number ": value_upsid,
                                   "Alternate name(s) ": value_alt_name})

"""correction du bug à l'ouverture des fichiers:
    lorsqu'une langue a un nom alternatif, cette langue alternative 
    possède également un nom de fichier.
    Mais lorsqu'on ouvre le fichier correspondant au nom alternatif,
    c'est le fichier de la langue d'origine qui s'ouvre, ce qui crée 
    des doublons dans les noms de langues (value_name_language)"""
for dic in container_json:
    #si un dictionnaire existe en plusieurs fois
    if container_json.count(dic) >1:
        #suppression des dictionnaires en trop (il en reste un)
        del container_json[container_json.index(dic)]
        
#print(len(container_json))
#print(container_json)
#écriture du fichier json
file_json = open('NormalisationLangues.json', 'w')
file_json = json.dump(container_json, file_json)



