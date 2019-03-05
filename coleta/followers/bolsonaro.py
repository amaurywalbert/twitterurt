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
		followers_list = []
		for page in tweepy.Cursor(api.followers_ids,id=user).pages():
			for follower in page:
				followers_list.append(follower)
		return (followers_list)

	except tweepy.error.TweepError as e:
		try:
			# Usu�rios n�o existentes ou n�o encontrados
			if e.message[0]['code'] == 32 or e.message[0]['code'] == 34 or  e.message[0]['code'] == 215 or e.message[0]['code'] == 429 or e.message[0]['code'] == 401 or e.message[0]['code'] == 404 or e.reason == "Twitter error response: status code = 401" or e.reason == "Twitter error response: status code = 404" or e.message == 'Not authorized.':
				with open(data_dir+str(user)+".json", "w") as f:			# Cria arquivo vazio
					print ("Usuario inexistente. User: "+str(user)+" - Arquivo criado com sucesso!")
		except Exception as e2:
			print ("\n ERROR - ERROR ERROR - E2: "+str(e2)+"\n")

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
			with open(data_dir+str(user)+".json", "w") as f:
				k=0
				for id in data:
					k+=1
					f.write(json.dumps(id)+"\n")		# ... no arquivo, imprime o tweet (status) inteiro.
			print (str(coleta)+" - "+str(candidate)+": "+str(j)+"/"+str(l)+": "+str(user)+" - "+str(k)+" friends")
	
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
#		Conta: msc2016001227 - user: msc2016001227 - e-mail: twitter27msc20160012@yahoo.com - senha: padr�o
#msc20160012_271 - Bolsonaro
consumer_key = "tY71hkUKRrr9Bf94Bo1El5ozW"
consumer_secret = "Xm3ZSg2zmCNSMJtx3sBeODkZkQqiLAFmkOi7KoTrcak00rLyHK"
access_token = "822174289742925824-FzJqDAWIgRkJ8xR15BLQR9E8oJ7L3a3"
access_token_secret = "bwD0p1lREYF9kSSiYp1vWXdKBM4jzAjW8ONJgCDXuT66n"

candidate = "bolsonaro"
coleta = "followers"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True,wait_on_rate_limit=True)

####################  ARMAZENAMENTO DOS DADOS ###############################################################
#############################################################################################################

source_dir = "/home/twitterurt/ProjetoEleicao/data_id/"
data_dir = "/home/twitterurt/ProjetoEleicao/"+str(coleta)+"/json/"  ####### Diretorio para armazenamento dos arquivos JSON

######################################################################################################################
######################################################################################################################

# Executa o metodo main
if __name__ == "__main__": main()