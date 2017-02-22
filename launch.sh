#!/bin/bash

echo "Initialisation du serveur"
~/unrealircd/unrealircd start
echo "Serveur lancé"
echo "Initialisation du bot"
python ./ElastiChat/bot.py 6667
echo "Bot interrompu"

exit 0
