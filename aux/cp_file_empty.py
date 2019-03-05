# -*- coding: latin1 -*-
####################################################################
# Script para copiar arquivos em branco para os diretórios de coleta
#
import os,sys,shutil


reload(sys)
sys.setdefaultencoding('utf-8')

def main():
	i = 0
	for file in os.listdir(source):
		origin = str(source) + str(file)
		if os.path.getsize(origin) < 1:
			shutil.copy(origin, dest1)
			shutil.copy(origin, dest2)
			shutil.copy(origin, dest3)
			i+=1
			print (origin +" copiado com sucesso! "+str(i))


######################################################################################################################################################################
#
# INICIO DO PROGRAMA
#
######################################################################################################################################################################
source = "/home/twitterurt/ProjetoEleicao/profile/json/"  ####### Origen
dest1 = "/home/twitterurt/ProjetoEleicao/timeline/json/"  ####### Destino 1
dest2 = "/home/twitterurt/ProjetoEleicao/friends/json/"   ####### Destino 2
dest3 = "/home/twitterurt/ProjetoEleicao/followers/json/" ####### Destino 3

# Executa o metodo main
if __name__ == "__main__": main()
