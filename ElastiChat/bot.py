#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import json
import time
import sys
from random import randint
from esearch import Esearch
es = Esearch("localhost", 9200)

channel = "#elastichat"
server = "localhost"
nickname = "Cute_Bot"

#Il s'agit des messages liés à l'apprentissage du bot, celui-ci les pose quand un utilisateur parle en public
question_bot = []
message1 = "Pouvez-vous répondre à ma place, j'ai envie de connaitre la réponse :)".decode('utf-8')
message2 = "Je ne comprend pas ce qu'il a dit, pouvez-vous m'expliquer? :o".decode('utf-8')
message3 = "Une réponse à sa question pourrait m'aider à mieux comprendre vos discussions ;)".decode('utf-8')
question_bot.append(message1)
question_bot.append(message2)
question_bot.append(message3)

#Quand le message de l'utilisateur trouve une réponse, le bot signifie qu'il a bien compris le message
reponses_bot = []
message1 = "Oh, cela signifie donc ça :o".decode('utf-8')
message2 = "Ah d'accord :)".decode('utf-8')
message3 = "Intéressant, je note ;)".decode('utf-8')
message4 = "J'ai de bons professeurs ^^".decode('utf-8')
message5 = "Merci, je vais faire de mon mieux pour comprendre :)".decode('utf-8')
reponses_bot.append(message1)
reponses_bot.append(message2)
reponses_bot.append(message3)
reponses_bot.append(message4)
reponses_bot.append(message5)

#Quand le bot n'a pas de réponse, on renvoie un message le signifiant
not_found_bot = []
message1 = "Je ne comprend pas :/".decode('utf-8')
message2 = "Je ne sais pas quoi répondre...".decode('utf-8')
message3 = "Je n'ai pas très bien compris :(".decode('utf-8')
not_found_bot.append(message1)
not_found_bot.append(message2)
not_found_bot.append(message3)

class IRC:

    """Classe du bot

    Cette classe permet le fonctionnement du chatbot, sa connection et la gestion des réponses.
    """
    irc = socket.socket()

    def __init__(self):
        """Initialisation

        socket.AF_INET -- Adresse IP liée au socket
        socket.SOCK_STREAM -- Protocole TCP permettant la liaison entre les utilisateurs
        """
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, msg, chan = None):
        """Envoi de message texte sur le serveur.

        chan -- le canal du discussion à traiter
        msg -- la chaîne de caractère à envoyer
        """
	if chan is None:
		self.irc.send(msg + "\n")
	else:
        	self.irc.send("PRIVMSG " + chan + " :" + msg + "\n")

    def connect(self, server, channel, botnick):
        """Se connecter au serveur.

        server -- le serveur sur lequel se connecter
        channel -- le canal sur lequel se connecter
        botnick -- le pseudo sous lequel le bot doit se connecter
        """
        #connexion au socket
        print ("Connection à :"+server)
	if(len(sys.argv) < 2):
		print ("Veuillez saisir un port de connexion")
		exit()
	else:
        	self.irc.connect((server, int(sys.argv[1])))
        	print ("Connecté")
        #connexion au serveur
        self.irc.send("USER " + botnick + " " + botnick +" " + botnick + " :Essayer de me MP ;D \n")
        #authentification
        self.irc.send("NICK " + botnick + "\n")
	#Boucle permettant de détecter si un ping/pong est nécessaire pour communiquer avec le serveur. 
	#La boucle sert à passer outre le fait d'utiliser un sleep, posant des problèmes de connexion.
	loop = 0
	while loop < 3:
	 	text = irc.get_text().decode('latin1')
	 	if 'PING :' in text:
			#Permet de renvoyer la bonne chaine de caractères au ping
			pong = 'PONG :'+ text.split(":")[-1] + '\r\n'
			self.irc.send(pong)
			self.irc.send("JOIN " + channel + "\n")
			break
		else: 
			loop = loop+1
	self.irc.send("JOIN " + channel + "\n")

    def get_text(self):
        """Recupérer le texte envoyé sur le serveur."""
        #reception du contenu
        text=self.irc.recv(2040)
        return text

    def elastic(self,message):
	#On effectue la recherche sur le message de la requete
        dico = es.search("base",message)
        #Si pas de résultat, on envoie un message explicatif
        print dico
       	if (dico['hits']['hits'] == []):
            #Choix aléatoire du message dans le tableau
            no = randint(0,len(not_found_bot)-1)
            message = not_found_bot[no]
        #Sinon, on renvoie un des messages les plus probable, choisi aléatoirement
        else:
            #Tableau contenant les réponses
            reponses_possibles = []
            #La taille du dictionnaire
            taille = len(dico['hits']['hits'])
            #Le score maximum
            score_max = dico['hits']['hits'][0]['_score']
            #Si on a plus d'un résultat, on vérifie le plus fréquent
            if taille > 1:
                #Pour le dicitonnaire
                for i in range(0, taille-1) :
                    #On vérifie si le nouveau résultat correspond au score maximum
                    if (dico['hits']['hits'][i]['_score'] == score_max):
                        #On ajoutez ces résultats au tableau
                        reponses_possibles.append(dico['hits']['hits'][i]['_source']['answer'])
                #On choisi une réponse aléatoirement
                no = randint(0,len(reponses_possibles)-1)
                message = reponses_possibles[no]
            else:
                message = dico['hits']['hits'][0]['_source']['answer']
	return message

#Variables de stockage pour apprentissage
question = None
reponse = None
#Connection au serveur
irc = IRC()
irc.connect(server, channel, nickname)

#Message d'arrivée
irc.send("Bonjour, je suis un gentil bot ! Parlez moi avec @"+nickname+" ;)".encode('utf-8'), channel)

#Tant que le bot tourne, on analyse les messages
while 1:
    #On décode les caractères spéciaux et on récupère un message de la forme ":NomExpéditeur!~Info_IP : PRIVMSG NomDuBot :Message"
    text = irc.get_text().decode('latin1')
    if(len(text) > 0):
   	print(text)
    else:
	exit(1)
    # Ping Pong pour éviter la déconnexion
    last_ping = time.time()
    if text.find('PING ') != -1:
	pong = 'PONG '+ text.split()[1] + '\r\n'
        irc.send(pong)
        last_ping = time.time()
    #Si le dernier ping à plus de 2 minutes, on quitte le programme
    if (time.time() - last_ping) > 120:
        break
    #On récupère le pseudo, sous la forme ":NomExpéditeur!", on sépare la chaine pour ne garder que ce bloc : ":NomNomExpéditeur"
    temp_nom = text.split("!")
    #On supprime les : du début pour ne garder que le nom
    nom = temp_nom[0][1:]


    #Si le bot reçoit un MP
    if('PRIVMSG' in text):
	
        #Permet de faire apprendre de nouvelles réponses au bot
        if(channel in text and ('@'+nickname).lower() not in text.lower() and nickname.lower() not in text.lower()):
            temp_message = " ".join(text.split(" ")[3:])
            message = temp_message[1:]
            #L'apprentissage fonctionne en deux temps, d'abord, un message ayant rôle de question
            if (question == None):
                question = message
                #Choix aléatoire du message dans le tableau
                no = randint(0,len(question_bot)-1)
                message = question_bot[no]
                irc.send(message.encode('utf-8'), channel.encode('utf-8'))
            #Si la question est déjà formulé, on attend maintenant une réponse
            else:
                reponse = message
                #On indexe le nouveau couple dans l'index
                es.index(question+"\t"+reponse, "base")
                question = None
                reponse = None
                #Choix aléatoire du message dans le tableau
                no = randint(0,len(reponses_bot)-1)
                message = reponses_bot[no]
                irc.send(message.encode('utf-8'), channel.encode('utf-8'))

        #Si l'utilisateur en canal privé
        if (nickname in text and channel not in text):
            temp_message = " ".join(text.split(" ")[3:])
            message = temp_message[1:]
 	    #Recherche dans elastic
            message = irc.elastic(message)
            #On envoie les résultats à l'expéditeur du message
            irc.send(message.encode('utf-8'), nom.encode('utf-8'))

        #Si un message est publié sur le canal
        if(channel.lower() and ('@'+nickname).lower() in text.lower()):
    	    temp_message = text.lower()
            temp_message = text.replace(('@'+nickname).lower(),'')
            temp_message = " ".join(temp_message.split(" ")[3:])
            message = temp_message[1:]
	    #Recherche dans elastic
            message = irc.elastic(message)
            #On envoie les résultats à l'expéditeur du message
            irc.send(message.encode('utf-8'), channel)

    #Si un utilisateur se connecte sur le canal
    elif('JOIN' in text and nickname.lower() not in text.lower()):
        #On lui envoi un message de bienvenue
        irc.send(("Bienvenue "+nom+', utilise @Cute_Bot pour me parler :D').encode('utf-8'), channel)

    #Si un utilisateur se déconnecte du canal
    elif('PART' in text):
        #On lui envoi un message de départ
        irc.send(('Au revoir '+nom+' :D').encode('utf-8'), nom.encode('utf-8'))
