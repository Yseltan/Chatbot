# -*- coding: utf-8 -*-
#!/bin/bash

#Nettoyage des caractères spéciaux
sed -f ./sed/commandesSED $1 > $1.a;

head --lines=-3 $1.a>$1.b;
sed '/   /d' $1.b>$1.c;
sed '/  /d' $1.c>$1.d;
tr "\012" "	" <$1.d > $1.e;
awk '{ORS=NR%2==0?"\n":RS}1' RS="	" $1.e>$1.f;
sed '$ d' $1.f > $1.g;
sed '1,1d' $1.g > $1.h;
sed '/-/d' $1.h>$1.propre;

#On supprime les fichier temporaires
rm $1.[a-r];
rm $1;


#Chaque espace devient un retour chariot
#tr " " "\012" <$1.a> $1.b;
