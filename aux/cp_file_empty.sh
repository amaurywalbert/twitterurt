#!/bin/bash
#Copiar arquivos em branco do diretório profile para os demais diretórios de coleta
PROFILE="/home/twitterurt/ProjetoEleicao/profile/json/"
TIMELINE="/home/twitterurt/ProjetoEleicao/timeline/json/"
FRIENDS="/home/twitterurt/ProjetoEleicao/friends/json/"
FOLLOWERS="/home/twitterurt/ProjetoEleicao/followers/json/"

i=0
for _origin in $PROFILE*; do
	if ! [ -s $_origin ]; then
		cp -rf $_origin $TIMELINE; cp -rf $_origin $FRIENDS; cp -rf $_origin $FOLLOWERS;
		i=$((i+1))
		echo "$_origin copiado com sucesso! $i"
		
	fi
done



