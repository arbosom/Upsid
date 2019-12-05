# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:59:13 2019

@author: Estelle
"""
import os
from bs4 import BeautifulSoup
import json

"""Storage list for the data"""
container_json = []

"""Count the number of languages we're anlyszing"""
directory_languages = "Langues/"
languages_files = os.listdir(directory_languages)
nb_languages = len(languages_files) 


"""Access all sound files in the directory 'sounds' """
directory_sounds = "sounds/"
list_files = os.listdir(directory_sounds) 

"""Browse the "sounds" files in order to extract the information we need """
for i in list_files:
    
    #Parse each file with beautifulSoup
    file = open(directory_sounds+i).read()
    soup = BeautifulSoup(file, "html.parser")
    
    #browse the 'td' balises in order to access the 'sound' balise
    for balise in soup.find_all("td"):
        #id the sound name"""
        if balise.string == "Sound:":
            value_sound_name = balise.find_next().string
        
    #id the number of languages who use this sound
    #commencer le count à -1 car l'adresse email du createur est stocké dans une balise a
    count_langue = -1
    for link in soup.find_all('a'):
        count_langue += 1
    value_language_number = count_langue
    
    frq = (100*value_language_number)/nb_languages
        
    container_json.append({"Sound ": value_sound_name ,
                           "Language ": value_language_number ,
                           "FRQ " : frq})
    
    
"""Dump the data in the json file"""
file_json = open('stat_sounds.json', 'w')
file_json = json.dump(container_json, file_json)
        
        


