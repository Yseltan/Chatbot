#!/bin/python

"""Effectue une recherche de la chaîne passée en paramètre."""

import sys
from esearch import Esearch

ES = Esearch("localhost", 9200)

print(ES.search("base", sys.argv[1]))
