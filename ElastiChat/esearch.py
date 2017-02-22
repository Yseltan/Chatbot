#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Classe esearch."""
import sys
from elasticsearch import Elasticsearch
import elasticsearch


class Esearch:
    """Classe servant d'interface à Elasticsearch.

    Cette classe est spécifique au projet ElastiChat, puisqu'elle
    insère des paramètres par défaut adapté à ce projet.
    """

    def __init__(self, host, port):
        """Initialisation.

        host -- adresse du serveur
        port -- port d'écoute du serveur
        """
        self.ess = Elasticsearch([{'host' : host, 'port' : port}])

    def create_index(self, index):
        """Crée un index sur le serveur.

        index -- le nom de l'index à créer
        """
        res = self.ess.indices.create(index=index, ignore=400)
        return res

    def delete_index(self, index):
        """Supprime un index.

        index -- nom de l'index à supprimer
        """
        res = self.ess.indices.delete(index=index, ignore=[400, 404])
        return res

    def create(self, index, ident, body):
        """Crée un document.

        index -- index dans lequel insérer le document
        ident -- identifiant unique du document
        body -- le document en lui-même (correctement formaté)
        """
        res = self.ess.create(index=index, doc_type="couple", id=ident,
                              body=body, ignore=400)
        return res

    def delete(self, index, ident):
        """Supprime un document.

        index -- l'index dans lequel se trouve le document
        ident -- l'identifiant du document à supprimer
        """
        res = self.ess.delete(index=index, doc_type="couple", id=ident,
                              ignore=[400, 404])
        return res

    def search(self, index, content):
        """Permet d'effectuer une recherche.

        index -- l'index dans lequel rechercher
        content -- le contenu à rechercher
        """
        doc = {
            "query": {
                "match": {
                    "question": {
                        "query": content,
                        "fuzziness": "AUTO",
                        "operator":  "and"
                    }
                }
            }
        }
        res = self.ess.search(index=index, body=doc)
        return res

    def index(self, content, index, ident=None):
        """Permet d'indexer une ligne dans la base de données.

        content -- la chaîne à indexer
        index -- l'index à utiliser
        ident -- l'identifiant de l'item. Par défaut, à la suite des
        existants
        """
        tab = content.split('\t')
        body = {'question':tab[0], 'answer':tab[1]}
        if ident is None:
            try:
                ident = self.ess.count(index="base")["count"] + 1
            except elasticsearch.NotFoundError:
                print("Index inexistant !")
                return False
        self.create(index, ident, body)
        return True

    def index_file(self, source, index, log=False):
        """Permet d'indexer un fichier dans la base de données.

        source -- le fichier à indexer, correctement formaté
        index -- l'index dans lequel index
        """

	
        with open(source, 'r') as fichier:
            lines = fichier.readlines()
            cent = len(lines)
            self.create_index(index)
	    p = 0
            i = 1
            while self.ess.exists(index="base", doc_type="couple", id=i):
		p = 0
                i += 1
		p += 1
            for line in lines:
                self.index(line, index, ident=i)
                i += 1
		p += 1
                if log:
                    print str(p*100//cent)+"%\r",
