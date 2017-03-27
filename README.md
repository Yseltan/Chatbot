# ElastiChat, robot assistant
Une implémentation python d'un bot IRC, utilisant le moteur de recherche ElasticSearch.
## Contact
- Julien Aubert-Béduchaud : julien.aubert---beduchaud@etu.univ-nantes.fr
- Yann Gilles : yann.gilles@etu.univ-nantes.fr
- Ronan Godicheau-Tornier : ronan.godicheau--tornier@etu.univ-nantes.fr
- Guillaume Lefroy : guillaume.lefroy@etu.univ-nantes.fr
## License d'exploitation
Soumis à la license GNU GPL3
## Contenu du repertoire
Il est recommandé de disposer de l'ensemble des droits sur les fichiers du projet, à obtenir via `chmod -R u+xwr ElastiChat/`
### Dossiers
- `ElastiChat/`: Contient le moteur de recherche et le bot
- `indexation/`: Fichiers permettant l'indexation de fichier customisés
### Fichiers
- `elasticsearch.sh` : Lancement du serveur elastic
- `indexation_base.sh` : Indexation de la base de données par défaut
- `install.sh` : Installation des composants de base
- `launch.sh` : Lancer le programme via serveur unrealircd
- `launch_SSH.sh` : Lancer le programme au sein de l'IUT, sur un serveur tier
- `README.md` : Le fichier présent
## Pré-Requis
- Python 2.7 et 3.0
- unrealircd, nécessaire à la création de serveur local
- Système GNU/Linux - Compatibilité sur d'autres systèmes non vérifiée
- Client IRC
- Si installation manuelle, ElasticSearch 5.0 ou supérieur
## Installation
- Se placer à la racine du dossier
- Lancer `./install.sh`, un message confirmera le bon fonctionnement de l'opération. Un répertoire sera créé dans la racine du dossier `elasticsearch-5.1.2/`, celui-ci contient le moteur de recherche Elastic.
- Lancer une fois `./elasticsearch.sh`. Le bon fonctionnement sera signal par le log : `Cluster health status changed from [RED] to [YELLOW]`. Le programme s'executant en mode utilisateur, celui-ci occupe le terminal en cours. Un nouveau terminal devra être ouvert à nouveau, contenant la suite des instructions.
- Lancer `./indexation_base.sh`, ceci à pour effet l'indexation des résultats par défaut que renvera notre bot. A noter que dans l'état actuel, les résultats n'ont pas de cohérence, ces derniers sont issus d'une conversation IRC prise à la volée. Un message signifiera le succès de l'opération.
- Lancer au choix `./launch.sh` ou `launch_SSH.sh`, selon le type de lancement à effectuer : sur un serveur local, réalisé au moyen d'unrealircd ou sur un serveur distant, par défaut celui d'Ubuntu. La connexion distante nécessite les identifiants de connexion étudiant, permettant d'accéder au bastion de l'IUT. La compatibilité connexion professeur n'a pas été testée.
- Lancer le client IRC et se connecter au serveur localhost. Dans le cadre de XChat, installé sur les postes de l'IUT, cette connexion s'effectue après la connexion à un serveur, dans la saisie : `/server localhost XXXX`. XXXX sera à remplacer par 2222 sur un serveur distant et par 6667 sur serveur local.
- Se connecter au channel, par défaut `ElastiChat`. Le nom du bot par défaut est `Cute_Bot`.
## Notes liées à l'installation
- Le processus d'indexation peu être délicat, nécessitant parfois le restart du serveur elastic. Pour cela, dans le terminal contenant elasticsearch.sh, effectuer un `Ctrl+C` puis relancer le script. 
- Le bot peut être relancé à tout moment; à noter que si le serveur elastic n'est pas nécessaire au lancement du bot, celui-ci ne pourra plus répondre, entrainant un crash de celui-ci.
- Le recours au bastion de l'IUT est lié au pare-feu mit en place par l'IUT, empêchant la connexion à IRC sans tunnel SSH.
##Fonctionnement
- Le bot fonctionne sur un message publique ou privé. Pour changer de mode de discussion, effectuer `/query Cute_Bot` dans la saisie du client IRC permettra le message privé.
- En public, le bot doit être interpellé via `@Cute_Bot` dans les termes de la recherche. Néanmoins, la casse et l'emplacement du mot-clé dans la phrase ne sont pas importants.
- Le bot peut avoir un certain délai de réponse, il conviendra d'éviter de surcharger le bot, afin d'éviter une surcharge sur le moteur de recherche. 
- Le bot peut mentionner des phrases-type : "Je n'ai pas compris". Il est alors en phase d'apprentissage, un message suivant sa requête permettra l'indexation de nouveaux résultats dans la base de données. Des phrases-type : "Merci beaucoup" signifieront le succès de l'opération. 
