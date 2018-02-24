#importation des bibliotheques
import socket
import sys,os;
import pickle

#parametre du server a contacter
SERVER = "127.0.0.1"
PORT = 8080

#Création de la socket
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect((SERVER, PORT))

#recuperation des arguments passé en parametre lor de l'appel 
#Exemlple 1 : python Phyton-Client.py c:\mesfics\ -s fic2.txt
#Exemlple 2 : python Phyton-Client.py c:\mesfics\ -p fic1.txt

#recuperation du nom du fichier
argument1 = sys.argv[0]

#recuperation de l'option -s qui defini le type de fichier a chargé (service ou employe)
option = sys.argv[2]

#recuperation du chemein du fichier contenant les donnees a chargé dans la base
lienrepertoire = sys.argv[1]

#recuperation du nom du fichier
nonfichier = sys.argv[3]

#Si on veut chargé un fichier de personne on fait le traitement suivant
if (option=="-p"):

	#concatenation pour avoir le chemin du fichier
	rep = lienrepertoire+nonfichier

	#Verification de lexistence du fichier si le fichier existe on fait le traitement suivant
	if os.path.exists(rep): 
		print("Traitement de votre fichier........")

		#Ouverture du fichier en lecture
		mesdata = []
		with open(rep) as fp:  
			for line in fp:
				#formatage de la liste de donnees on supprime les nom des champs et on les concatene dans lordre suivant a envoyé au server
				mesdata.append(line.replace('Numero','').replace('nom','').replace('prenom','').replace('adresse','').replace('email','').replace('service','').replace(':','').replace(';',','))

		#On converti la liste (data_to_send) en string pour lenvoyer au client a travers le socket
		data_to_send = ''.join(mesdata)

		#On affiche dans le console du server les donnees a envoyé
		print(data_to_send)

		#Ici on ajoute a notre chaine le mot (emp) qui permetre au server de savoir le le service a invoqué
		dataS = "emp"+data_to_send
	
		while True:
			#On envoi maintenent la donnee au server
			client1.send(bytes(dataS,'UTF-8'))

			#On demande au client s'il veut continuer ou pas
			out_data = input("Voulez vous continuer /bye to quit :")

			#Si le client saisi bye on quite le programme
			if(out_data=="bye"):
				break
			client1.close()

		print("element envoyés")

	else:
		#Si le fichier que le client veut charger nexiste pas
		print("le fichier nexiste pas dans le repertoire")
		#___________________________________________________________________________________________

#Si on veut chargé un fichier de service on fait le traitement suivant
elif(option=="-s"):
	#concatenation pour avoir le chemin du fichier
	rep = lienrepertoire+nonfichier

	#Verification de lexistence du fichier si le fichier existe on fait le traitement suivant
	if os.path.exists(rep): 
		print("Traitement de votre fichier........")

		#Ouverture du fichier en lecture
		mesdata = []
		with open(rep) as fp:  
			for line in fp:
				#formatage de la liste de donnees on supprime les nom des champs et on les concatene dans lordre suivant a envoyé au server
				mesdata.append(line.replace('Nomser','').replace('Resp','').replace(':','').replace(';',','))

		#On converti la liste (data_to_send) en string pour lenvoyer au client a travers le socket
		data_to_send = ''.join(mesdata)

		#On affiche dans le console du server les donnees a envoyé
		print(data_to_send)

		#Ici on ajoute a notre chaine le mot (ser) qui permettra au server de savoir le le service a invoqué
		dataS = "ser"+data_to_send
	
		while True:
			#On envoi maintenent les donnees au server
			client1.send(bytes(dataS,'UTF-8'))

			#On demande au client s'il veut continuer ou pas
			out_data = input("Voulez vous continuer /bye to quit :")

			#Si le client saisi bye on quite le programme
			if(out_data=="bye"):
				break
			client1.close()

		print("element envoyés")
	else:
		#Si le fichier que le client veut charger nexiste pas
		print("le fichier nexiste pas")

