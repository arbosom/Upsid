# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:34:58 2019

@author: Estelle
"""
import os
from bs4 import BeautifulSoup
import json

"""Storage list for the data"""
container_json = []

"""Trouver les langues d'une branche"""
#variables
directory_name = "Branches/"
list_files = os.listdir(directory_name) 

"""Browse the "sounds" files in order to extract the information we need """
for i in list_files:

    branch_name = i.split(".")[0]
    
    #read the file and apply an html parser to it
    file = open(directory_name+i).read()
    soup = BeautifulSoup(file, "html.parser")
    
    #list to store the languages inside the branch
    list_languages = []
    
    #access the branch 
    branch = soup.find(text=branch_name+": ")
    #access the language tag using the sibling relationship
    td_tag = branch.parent
    languages = td_tag.findNext('td')
    for i in languages : 
        if i.name == "a" : 
            list_languages.append(i.string)
    
    """Access the different phones of each languages """
    dico = {}
    for l in list_languages : 
        list_sounds = []
        file2 = open("Langues/"+l).read()
        soup2 = BeautifulSoup(file2, "html.parser")
        branch2 = soup2.find(text="The language has these sounds:")
        td_tag2 = branch2.parent
        sounds = td_tag2.findNext('td')
        for s in sounds : 
            if s.name == "a" : 
                list_sounds.append(s.string)
        
        dico[l]=set(list_sounds)
    
    common_sounds = set()
    
    for i, phon in enumerate(dico.values()):
        if i==0:
            common_sounds=phon
        else:
            common_sounds=common_sounds.intersection(phon)
    
    
    container_json.append({"Branche ": branch_name ,
                               "Phones ": list(common_sounds)})
    

"""Dump the data in the json file"""
file_json = open('stat_branches.json', 'w')
file_json = json.dump(container_json, file_json)
    
            
    



