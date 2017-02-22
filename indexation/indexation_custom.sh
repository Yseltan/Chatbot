#!/bin/sh


if [ -z $1 ]
  then
  echo Veuillez saisir le fichier puis le nom de la base dans laquelle indexer
  exit
fi

if [ -z $2 ]
  then
  echo Veuillez saisir le fichier puis le nom de la base dans laquelle indexer
  exit
fi

echo "Début de l'indexation de ${1} dans ${2}"
./sub_2_elastic.sh ${1}
python ../ElastiChat/indexation_auto.py ${1}.propre ${2}
rm ${1}.propre
echo "Indexation terminée"
exit 0
