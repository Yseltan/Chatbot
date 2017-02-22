"""Permet de supprimer l'index passe en parametre."""

import sys
from esearch import Esearch

ES = Esearch("localhost", 9200)

ES.delete_index(sys.argv[1])
