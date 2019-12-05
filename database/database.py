#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:57:42 2019

@author: tanguy
"""

import mysql.connector
import json
import itertools


class database:
    """La classe base de données permet la création la suppression l'actualisation la gestion des tables situées dans un schéma ainsi que la gestion et la création des requêtes permettant l'insertion l'actualisation des données provenant des corpus upside de langue de branche de phonème de géolocalisation des langues présentes.
    L'initialisation des instances de la classe database requiert des séquences de création des séquences de suppression un nom et l'option debug facultative mais néanmoins utile lors de la création des données pour voir les potentiels erreurs"""
    def __init__(self,db,creation,deletion,name="mydb",debug=False):
        """"""
        self.db=db
        self.mycursor=mydb.cursor()
        self.creation=creation
        self.deletion=deletion
        self.name=name
        self.file=open("%s.sql"%(name),"w",encoding="utf-8")
        self.file.write("-- MySQL Script generated by Tanguy Launay\n")
        for i in self.creation:self.file.write(i+"\n")
        self.file.close()
        self.debug=debug
    def initialisation(self):
        """L'initialisation permet de supprimer les tables précédemment insérées dans la base de données,
        de recréer les tables nécessaires à son bon fonctionnement et ceux de manière automatique,
        sans qu'il y a besoin de vérifier l'état de la base avant de faire les requêtes adaptées"""
        try:
            for i in deletion:mycursor.execute(i)
        except:
            print("Déjà supprimés")
        finally:
            for i in creation:mycursor.execute(i)
            self.db.commit()
            print("Base de données correctement chargée")
    def ajout_donnees(self, table, colonnes, valeurs):
        """La fonction ajouter_données nécessite d'avoir le nom de la table, des colonnes nécessaires à l'insertion et la localisation des champs requis
        pour les données, ensuite le paramètre valeurs qui est une liste des valeurs qui seront insérées"""
        sql="INSERT INTO `%s` (%s) VALUES ({valeurs});"%(table,','.join(["`%s`"%(a) for a in colonnes.split(" ")]))
        self.file=open("%s.sql"%(self.name),"a+")#ouverture du fichier en mode append pour ajouter les nouvelles requêtes aux anciennes
        for valeur in valeurs:
            if self.debug:print(valeur,sql)
            querry=sql.format(**{"valeurs":",".join(valeur)})#Permet de completer la requête sql en y insérant les valeurs pour chaque itération de la boucle for
            if self.debug:print(querry)
            try:
                self.mycursor.execute(querry)#exécution de la requête 
                self.file.write(querry+"\n")#écriture du fichier 
            except mysql.connector.IntegrityError:#dans le cas d'une duplication de clef primaire, la requête n'est pas prise en compte
                continue
            finally:
                self.db.commit()
        self.file.close()
            

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd= "Mon Serveur MySQL 5.7.27",
        auth_plugin='mysql_native_password',
        database = "mydb",
        use_pure=True
        )
mycursor=mydb.cursor()
deletion=["DROP TABLE `Phonemes_Langues`;",
          "DROP TABLE `Langues_Branches`;",
          "DROP TABLE `Branches`;",
          "DROP TABLE `Phonemes`;",
          "DROP TABLE `Langues`;",
        ]
creation=["CREATE TABLE IF NOT EXISTS `mydb`.`Langues` ( `upsid` INT NOT NULL, `nom` TEXT NOT NULL, `biblio` TEXT NULL, PRIMARY KEY (`upsid`)) ENGINE = InnoDB;",
 "CREATE TABLE IF NOT EXISTS `mydb`.`Phonemes` ( `id` INT NOT NULL AUTO_INCREMENT, `IPA` TEXT NOT NULL, `description` TEXT NULL, PRIMARY KEY (`id`)) ENGINE = InnoDB;",
 "CREATE TABLE IF NOT EXISTS `mydb`.`Branches` ( `famille` TEXT NOT NULL, `id` INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (`id`)) ENGINE = InnoDB;",
 "CREATE TABLE IF NOT EXISTS `mydb`.`Phonemes_Langues` ( `upsid` INT NOT NULL, `phoneme` INT NOT NULL, INDEX `upsid_idx` (`upsid` ASC), INDEX `IPA_idx` (`phoneme` ASC), PRIMARY KEY (`upsid`, `phoneme`), CONSTRAINT `upsid` FOREIGN KEY (`upsid`) REFERENCES `mydb`.`Langues` (`upsid`) ON DELETE NO ACTION ON UPDATE NO ACTION, CONSTRAINT `IPA` FOREIGN KEY (`phoneme`) REFERENCES `mydb`.`Phonemes` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION) ENGINE = InnoDB;",
 "CREATE TABLE IF NOT EXISTS `mydb`.`Langues_Branches` ( `famille` INT NOT NULL, `upsid` INT NOT NULL, PRIMARY KEY (`famille`, `upsid`), INDEX `upsid_fk_idx` (`upsid` ASC), INDEX `index3` (`famille` ASC), CONSTRAINT `famille_fk` FOREIGN KEY (`famille`) REFERENCES `mydb`.`Branches` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION, CONSTRAINT `upsid_fk` FOREIGN KEY (`upsid`) REFERENCES `mydb`.`Langues` (`upsid`) ON DELETE NO ACTION ON UPDATE NO ACTION) ENGINE = InnoDB;"
 ]


langues=json.load(open("langues.json"))
phonemes=json.load(open("phonemes.json"))
branches=json.load(open("branches.json"))

base_donnees=database(mydb,creation,deletion,"projet-Tanguy-Launay",True)#instantiation de la l'objet database

base_donnees.initialisation()
val_langues=list(set([("%s"%(langue["UPSIDE number "]),"'%s'"%(langue["Language name "].replace("'","´"))) for langue in langues]))#liste d'un ensemble de tuples composées du numéro upsid et du nom de langue correspondante pour chaque langue présente dans le fichier langues.json
val_phonemes=list(set([("'%s'"%(i[2].replace("'","´")),"'%s'"%(i[1])) for i in itertools.chain.from_iterable(phonemes.values())]))#liste d'un ensemble de tuples composées du phonème au format upsid ainsi que de sa description en anglais
val_branches=[[a] for a in set(["'%s'"%(i.replace("'","´")) for i in itertools.chain.from_iterable(branches.values())])]# liste de listes composées d'un nom de famille linguistique
dico={}
for i in langues:#pour chacune des langues du fichier langues.json
    dico[i["Language name "].strip()]=i["UPSIDE number "]#Ajout du nom de la langue comme clef correspondant au code upsid de ladite langue
    alt=i["Alternate name(s) "]
    if alt!="No alternate name(s)":#si cette langue possède des dénominations alternatives
        if "," in alt:entrees=alt.split(", ")#création de la liste de toutes les autres appellations de ladite langue
        else:entrees=[alt]
        for entree in entrees:dico[entree.strip()]=i["UPSIDE number "]#ajout d'une clef différente pour chaque dénomination mais avec le même code upsid
phon={a[0]:i for i,a in enumerate(val_phonemes)}#création d'un dictionnaire associant à chaque phonème son id
val_pl=[elem for elem in itertools.chain.from_iterable([[(dico[nom.strip()],"%s"%(phon["'%s'"%(son[2].replace("'","´"))])) for son in sons] for nom,sons in phonemes.items()])]#list de tuples qui permettent l'association de tous les codes upsid avec les codes de phonèmes que ces langues comportent.
val_lb=[i for i in itertools.chain.from_iterable([[(dico[nom.strip()],"%s"%(str(val_branches.index(["'%s'"%(famille)])))) for famille in familles] for nom,familles in branches.items()])]#list de tuples qui permettent l'association de tous les codes upsid avec les codes de branche auqelles ces langues appartiennent.
base_donnees.ajout_donnees("Langues","upsid nom",val_langues)#Ajout des valeurs précédemment décrites aux tables de la base de données
base_donnees.ajout_donnees("Phonemes","IPA description",val_phonemes)
base_donnees.ajout_donnees("Branches","famille",val_branches)
base_donnees.ajout_donnees("Langues_Branches","upsid famille",val_lb)
base_donnees.ajout_donnees("Phonemes_Langues","upsid phoneme",val_pl)

print("Todo hecho")