#!/bin/bash
#Copiar arquivos em branco do diretório profile para os demais diretórios de coleta
PROFILE="/home/twitterurt/ProjetoEleicao/profile/json/"
TIMELINE="/home/twitterurt/ProjetoEleicao/timeline/json/"
FRIENDS="/home/twitterurt/ProjetoEleicao/friends/json/"
FOLLOWERS="/home/twitterurt/ProjetoEleicao/followers/json/"


for _origin in $PROFILE*; do
	if [ -s $_origin ]; then
		echo "$_origin has some data."
	else
		cp -rf $_origin $TIMELINE; cp -rf $_origin $FRIENDS; cp -rf $_origin $FOLLOWERS;
	fi
done



