#!/bin/bash

if [ -z $1 ]
  then
  echo Veuillez saisir votre identifiant universitaire en paramètre
  exit
fi

ssh -f -N -L:2222:irc6.geo.oftc.net:6667 ${1}@bastion.etu.univ-nantes.fr
echo "Initialisation du bot"
python ./ElastiChat/bot.py 2222
echo "Bot interrompu"

exit 0
