#!/bin/sh

echo -e "Téléchargement d'ElasticSearch…\n"

wget -c https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.1.2.tar.gz || exit 1

echo -n "Extraction… "

tar -xzf elasticsearch-5.1.2.tar.gz &>/dev/null && echo -e "OK\n" || exit 2

echo "Installation du module Python… "

pip install --user elasticsearch ||  exit 3

echo
echo "Installation terminée avec succès"

exit 0
