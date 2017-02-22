"""Importation d'un fichier depuis la ligne de commande.

Utilisation : python indexation_auto.py <fichier> <index>
"""
import sys
from esearch import Esearch

ES = Esearch("localhost", 9200)

ES.create_index(sys.argv[2])

ES.index_file(sys.argv[1], sys.argv[2], log=True)
