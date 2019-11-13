# Upsid
Projet de Mr Embarki avec les langues du projet Upsid
Created on Wed Oct 30 18:13:50 2019

@author: RIDA
"""
from bs4 import  BeautifulSoup
import json
import os

"""Trouver les langues d'une branche"""
#variables
os.chdir("projet_Embarki/Embarki-Data/")
directory_name = "projet_Embarki/Embarki-Data/Branches/"
listBranches = os.listdir("Branches/")
file1=open("text.txt","w")
os.chdir("Branches/")
dico={}
for i in listBranches:
    soup=BeautifulSoup(open(i).read(),"lxml")
    finder=soup.find_all("a")
    dico[i.replace(".html","")]={j.string for j in finder if j["href"].endswith("html")}
dico2={}
for i,j in dico.items():
    for a,b in dico.items(): 
        if j.issubset(b) and a!=i:
            print(i,a)
            if a not in dico2:
                dico2[a]=[i]
            else: dico2[a].append(i)
dico3={}
for i,j in dico2.items():
    dico3[i]=[{a:list(dico[a]) for a in j}]
    file1.write("%s\n"%(i))
    for k in j:
        file1.write("\t%s\n\t\t%s\n"%(k,"\n\t\t".join(dico[k])))
os.chdir("..")
monFichier= open("branches.json", "w")
json.dump(dico3,monFichier)
monFichier.close()
file1.close()
