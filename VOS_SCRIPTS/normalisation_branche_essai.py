#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:35:14 2019

@author: estelle
"""

import os
from bs4 import BeautifulSoup
import json

"""Creer une liste avec toutes les langues (sans doublons liés au noms alternatifs)"""
list_languages = []
directory_languages = "Langues/"
languages_files = os.listdir(directory_languages)

for l in languages_files:
    
    #Parse each file with beautifulSoup
    file = open(directory_languages+l).read()
    soup = BeautifulSoup(file, "html.parser")
    
    for balise in soup.find_all("td"):
          
        #find the name of the language
        if balise.string == "Language name:":
            name =balise.find_next().string   
    
    if name not in list_languages : 
        list_languages.append(l)

"""Creer une liste avec toutes les branches"""
list_branches = []
directory_branches = "Branches/"
branches_files = os.listdir(directory_branches)

for b in branches_files : 
    
    #Parse each file with beautifulSoup
    file = open(directory_branches+b).read()
    soup = BeautifulSoup(file, "html.parser")
    
    for balise in soup.find_all("td", valign=True):
         if name not in list_branches : 
             list_branches.append(balise.string[:-2])


"""Pour chaque langue, identifier les sous classes"""
for l in list_languages : 
    
    file = open(directory_languages+l).read()
    soup = BeautifulSoup(file, "html.parser")
    
    list_cla = []
    for a in soup.find_all('a', href=True):
        if a['href'].startswith("../C/C_") : 
            list_cla.append(a.string)
            
    """Pour chaque sous classe créer une entrée de dico cla - langues"""
    dico_cla = {}
    list_tuples = []
    for c in list_cla : 
        
        if c in list_branches : 
        
            file_cla = open("Branches/"+c+".html").read()
            soup2 = BeautifulSoup(file_cla, 'html.parser')
            
            langues_dependantes = []
            for la in soup2.find_all('a', href=True):
                if la['href'].startswith("../L/L") : 
                    langues_dependantes.append(la.string)
                    
            dico_cla[c] = set(langues_dependantes)
            
            print(dico_cla)


    
    
  

        
   
        
        
            
        