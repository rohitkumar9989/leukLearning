# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:13:24 2018

@author: AmaDaly
"""

import datetime
import random
import sys
import mysql.connector as mc
try:
    connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "pythonClasse")
    print("connected")
except mc.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

cursor = connection.cursor()
class Employe:
    liste=[]
    
    def __init__(self):
        self.id=""
        self.num_matri=""
        self.nom=""
        self.prenom=""
        self.adresse=""
        self.email=""
        self.service=""
        Employe.liste.append(self)
     
     # Pour l'id
    def getId(self):
        return self.id
    def setId(self, id):
        self.id=id   
        # Pour le matricule
    def getMat(self):
        return self.num_matri
    def setMat(self, num_matri):
        self.num_matri=num_matri
        
    # Pour le nom
    def getNom(self):
        return self.nom
    def setNom(self, nom):
        self.nom=nom
        
    # Pour le prenom
    def getPrenom(self):
        return self.prenom
    def setPrenom(self, prenom):
        self.prenom=prenom
        
    # Pour l'email
    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email=email
        
    # Pour l'adresse
    def getAdresse(self):
        return self.adresse
    def setAdresse(self, adresse):
        self.adresse=adresse
     # Pour le service
    def getService(self):
        return self.service
    def setService(self, service):
        self.service=service   
        
    
    @staticmethod    
    def create_table_Emp():
        
        try:
            connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "pythonClasse")
        except mc.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)

        cursor = connection.cursor()
        
        cursor.execute ("DROP TABLE IF EXISTS employee")
        sql_command = """
        CREATE TABLE employee ( 
        id INTEGER PRIMARY KEY auto_increment, 
        num_matri VARCHAR(20), 
        nom VARCHAR(30),
        prenom VARCHAR(30),
        email VARCHAR(30),
        adresse VARCHAR(60),
        service INTEGER 
        );"""

        cursor.execute(sql_command)
        print("create")
    
    
    @staticmethod
    def data_entry_Emp(mat,nom,prenom,email,adr,serv):
        employe= Employe()

        employe.setMat(mat)
        employe.setNom(nom)
        employe.setPrenom(prenom)
        employe.setEmail(email)
        employe.setAdresse(adr)
        employe.setService(serv)

        #emp = (mat, nom, prenom, email, adr, serv)
        emp = {"mat": mat, "nom" : nom, "prenom" : prenom, "email" : email, "adr" : adr, "serv" : serv}
        #print(emp)
        try:
            connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "pythonClasse")
        except mc.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)

        cursor = connection.cursor()
        cursor.execute("""INSERT INTO employee (num_matri,nom,prenom,email,adresse,service) VALUES (%(mat)s,%(nom)s,%(prenom)s,%(email)s,%(adr)s,%(serv)s)""",emp)
        connection.commit()
        print("\n Employe ajouté avec success ! \n")

    
    @staticmethod   
    def read_from_db_Emp():
        try:
            connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "pythonClasse")
        except mc.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)

        cursor = connection.cursor()
        cursor.execute('select  * from employee')
        #data = cursor.fetchall()
        #print(data)
        for row in cursor.fetchall():
            print("matricule: "+row[1],"nom: "+row[2], "prenom: "+row[3]) 
    @staticmethod
    def AffichageEmp() :
        print("______________________Affichage de la liste du  des Employe_________________________")
        print("\n")
        employe=Employe()
        employe.read_from_db_Emp()
        print("\n___________________________________")        
            
# employe=Employe()
# mat = input("mat : ")
# nom = input("nom : ")
# prenom = input("prenom : ")
# email = input("Email : ")
# adr = input("adresse : ")
# serv = input("service : ")
# employe.data_entry_Emp(mat,nom,prenom,email,adr,serv)