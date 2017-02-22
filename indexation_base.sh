#!/bin/sh
echo "Début de l'indexation"
python ./ElastiChat/indexation_auto.py ./indexation/index_base.txt base
echo "Indexation terminée"
exit 0
