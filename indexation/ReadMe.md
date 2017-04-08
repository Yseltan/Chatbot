# Indexation de données dans Elastichat


## Contact
- Julien Aubert-Béduchaud : julien.aubert---beduchaud@etu.univ-nantes.fr
- Yann Gilles : yann.gilles@etu.univ-nantes.fr
- Ronan Godicheau-Tornier : ronan.godicheau--tornier@etu.univ-nantes.fr
- Guillaume Lefroy : guillaume.lefroy@etu.univ-nantes.fr

## License d'exploitation
Soumis à la license GNU GPL3


### Dossiers
- `Sed`: Contient le fichier "commandesSED" contenant les chaines de caractères et les caractères modifiés lors du nettoyage


### Fichiers
- `indexation_custom.sh` : Lancement de l'indexation d'un fichier dans une base, tous deux mis en paramètres.
- `sub_2_elastic.sh` : Script de nettoyage de fichier de sous-titres.
- `index_base.txt` : Fichier à indexer dans la base.


## Pré-Requis
- Python 2.7 et 3.0
- unrealircd, nécessaire à la création de serveur local
- Système GNU/Linux - Compatibilité sur d'autres systèmes non vérifiée
- Client IRC
- Si installation manuelle, ElasticSearch 5.0 ou supérieur

## Utilisation 
Afin d'augmenter la base de données du bot, il est possible de récupérer de nombreux sous-titres à l'adresse suivante:
http://opus.lingfil.uu.se/OpenSubtitles2016.php

Une fois sur la page, il faut, dans la partie "Download", cliquer sur le "fr" dans la colonne ou la ligne du tableau.
Le dossier étant lourd (environ 15Go), il faut prévoir un minimum d'espace disque ou une clé USB afin de pouvoir le télécharger.

Une fois ce dossier téléchargé, on peut observer qu'il contient des dossiers correspondant à des années.

Une fois dans le dossier de l'année choisie, le film que l'on voudra prendre ne sera pas un film que l'on aura choisi à l'avance, 
celui-ci étant uniquement répertorié dans un dossier avec un nom correspondant à un nombre de 4 à 10 chiffres environ. 

Ce dossier est constitué d'archives, elles mêmes constituées des fichiers qui nous intéressent.

Ainsi, on copie/collera ce fichier vers le dossier Chatbot/indexation qui n'est autre que celui-ci.

Ensuite, on se place dans ce même dossier dans le terminal.

Puis, on lance le script sub_2_elastic.sh permettant de nettoyer le fichier choisi avec la commande suivante afin de le rendre compréhensible par la suite:

./sub\_2\_elastic.sh *fichier_de_sous\_titres*.

Une fois ceci fait, on obtient un fichier avec une terminaison en .propre.

Ce fichier va ensuite pouvoir être indexé sur le bot avec le fichier indexation_custom situé dans Chatbot/indexation avec la commande suivante :

./indexation\_custom *fichier\_.propre*   *nom\_de\_la\_base\_dans\_laquelle\_indexer*.

Une fois ceci fait, la base a bien reçu l'ajout des sous-titres du film.


## Notes liées à l'utilisation
- Veillez à vous assurer que vous utilisez bien indexation_custom.sh avec un fichier *.propre*. Dans le cas contraire,
l'indexation se fera mais la base sera remplie de couples questions/réponses sans aucun sens.
- Veillez à vous assurer que vous utilisez bien ./sub\_2\_elastic.sh sur un fichier et non sur l"archive contenant le fichier en question.

