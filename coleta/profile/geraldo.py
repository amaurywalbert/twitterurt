# -*- coding: latin1 -*-
################################################################################################
# Script para coletar a dados dos usuarios que interagiram com os presidenciaveis durante a campanha eleitoral.
#
import tweepy, datetime, sys, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versao 1.0 - Coletar dados dos usuarios especificados usando o Tweepy para controlar as autenticacoes ##
######################################################################################################################################################################

######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve a dados de um usuario especifico
#
######################################################################################################################################################################
def get_data(user):
	try:
		profile = api.get_user(id=user, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)
		return (profile)

	except tweepy.error.TweepError as e:
		try:
			# Usu�rios n�o existentes ou n�o encontrados
			if e.message[0]['code'] == 34 or e.message[0]['code'] == 50 or e.message[0]['code'] == 63 or e.message[0]['code'] == 401 or e.message[0]['code'] == 404 or e.reason == "Twitter error response: status code = 401" or e.reason == "Twitter error response: status code = 404" or e.message == 'Not authorized.':
				with open(data_dir+str(user)+".json", "w") as f:			# Cria arquivo vazio
					print ("Usuario inexistente. User: "+str(user)+" - Arquivo criado com sucesso!")
		except Exception as e2:
			print ("E2: "+str(e2))

######################################################################################################################################################################
#
# SALVA dados dos usuarios
#
######################################################################################################################################################################
def save_data(j,l,user): # j = numero do usuario que esta sendo coletado
	#Chama a funcao e recebe como retorno a lista de tweets do usuario
	data = get_data(user)
	if data:
		try:
			with open(data_dir + str(user) + ".json", "w") as f:
				f.write(json.dumps(data._json) + "\n")  # ... no arquivo, imprime o perfil completo.
			print (str(coleta)+" - "+str(candidate)+": "+str(j)+"/"+str(l)+": "+str(user))
	
		except Exception as e:
			print e
			if os.path.exists(data_dir+str(user)+".json"):
				os.remove(data_dir+str(user)+".json")

######################################################################################################################################################################
######################################################################################################################################################################
#
# Metodo principal do programa.
# Realiza teste e coleta dados do user especificado no arquivo.
#
######################################################################################################################################################################
######################################################################################################################################################################
def main():
	print ("Autenticacao realizada. Iniciando coleta - "+str(coleta))
	for file in os.listdir(source_dir + candidate):
		with open(source_dir + candidate + "/" + file, "r") as f:
			users_id = f.readlines()
			j = 0
			l = len(users_id)
			for user in users_id:
				user = long(user)
				j += 1
				if not os.path.isfile(data_dir + str(user) + ".json"):
					save_data(j,l,user)  # Inicia funcao de busca dos dados
				else:
					print("Usuario ja coletado! "+str(coleta)+" - "+str(candidate)+": "+str(j)+"/"+str(l)+": "+str(user)+" - Seguindo...")
		print("######################################################################")
		print(str(candidate) + " - Coleta finalizada!")
		print("######################################################################\n")

######################################################################################################################################################################
#
# INICIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CHAVE E AUTENTICA��O
#		Conta: msc2016001233 - user: msc2016001233 - e-mail: twitter33msc20160012@yahoo.com - senha: padr�o
#msc20160012_331 - Geraldo
consumer_key = "3gdXCHZ8T43pOmZcBVt86ttBf"
consumer_secret = "vnoo0P17s7iJ0Qh4jh08FRUzP3FF3cEr1fgcSQNndsFdYpxTTs"
access_token = "831849920944553984-els3pI9zCLz1c8D3FIrfpHqo6i58b44"
access_token_secret = "sRs5nE5F07k7Pw4LlWycPcIiNRgMYE94ti3zbVoNUerlW"

candidate = "geraldo"
coleta = "profile"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

####################  ARMAZENAMENTO DOS DADOS ###############################################################
#############################################################################################################

source_dir = "/home/twitterurt/ProjetoEleicao/data_id/"
data_dir = "/home/twitterurt/ProjetoEleicao/"+str(coleta)+"/json/"  ####### Diretorio para armazenamento dos arquivos JSON

######################################################################################################################
######################################################################################################################

# Executa o metodo main
if __name__ == "__main__": main()