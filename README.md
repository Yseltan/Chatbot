# ElastiChat, robot assistant
Une implémentation python d'un bot IRC, utilisant le moteur de recherche ElasticSearch.
## Contact
Julien Aubert-Béduchaud : julien.aubert---beduchaud@etu.univ-nantes.fr
Yann Gilles : yann.gilles@etu.univ-nantes.fr
Ronan Godicheau-Tornier : ronan.godicheau--tornier@etu.univ-nantes.fr
Guillaume Lefroy : guillaume.lefroy@etu.univ-nantes.fr
## License d'exploitation
Soumis à la license GNU GPL3
## Contenu du repertoire
### Dossiers
- `ElastiChat/`: Contient le moteur de recherche et le bot
- `indexation/`: Fichiers permettant l'indexation de fichier customisés
### Fichiers
- `elasticsearch.sh` : Lancement du serveur elastic
- `indexation\_base.sh` : Indexation de la base de données par défaut
- `install.sh` : Installation des composants de base
- `launch.sh` : Lancer le programme via serveur unrealircd
- `launch\_SSH.sh` : Lancer le programme au sein de l'IUT, sur un serveur tier
- `README.md` : Le fichier présent
## Pré-Requis
- Python 2.7 et 3.0
- unrealircd, nécessaire à la création de serveur local
- Système GNU/Linux - Compatibilité sur d'autres systèmes non vérifiée
- Client IRC
- Si installation manuelle, ElasticSearch 5.0 ou supérieur
## Installation

