# -*- coding: latin1 -*-
################################################################################################
# Script para coletar a dados dos usuarios que interagiram com os presidenciaveis durante a campanha eleitoral.
#
import tweepy, datetime, sys, json, os, os.path, shutil, time, struct, random
import multi_oauth
# copiar o modulo acima para /usr/local/lib/python2.7/dist-packages/

reload(sys)
sys.setdefaultencoding('utf-8')

######################################################################################################################################################################
##		Status - Versao 1.0 - Coletar dados dos usuarios especificados usando alternando entre chaves de autenticacao para agilizar a coleta.
######################################################################################################################################################################

######################################################################################################################################################################
#
# Realiza autenticacao da aplicacao.
#
######################################################################################################################################################################
def authentication(auths):
	global key
	key += 1
	if (key >= key_limit):
		key = key_init
	print
	print("######################################################################")
	print ("Autenticando usando chave numero: "+str(key)+"/"+str(key_limit))
	print("######################################################################\n")
	time.sleep(wait)
	api_key = tweepy.API(auths[key])
	return (api_key)
######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve a dados de um usuario especifico
#
######################################################################################################################################################################
def get_data(user):
	global api
	try:
		followers_list = []
		for page in tweepy.Cursor(api.followers_ids,id=user,wait_on_rate_limit_notify=True).pages():
			for follower in page:
				followers_list.append(follower)
		return (followers_list)
	
	except tweepy.error.RateLimitError as e:
			print("Limite de acesso a API excedido. User: "+str(user)+" - Autenticando novamente... "+str(e))
			api = authentication(auths)

	except tweepy.error.TweepError as e:
		try:
			# Usuários nao existentes ou nao encontrados
			if e.message[0]['code'] == 34 or e.message[0]['code'] == 404 or e.reason == "Twitter error response: status code = 404" or e.message == 'Not authorized.':
				with open(data_dir+str(user)+".json", "w") as f:			# Cria arquivo vazio
					print ("Usuario inexistente. User: "+str(user)+" - Arquivo criado com sucesso!")
					
			elif e.message[0]['code'] == 32 or e.message[0]['code'] == 215 or e.message[0]['code'] == 429 or e.message[0]['code'] == 401 or e.reason == "Twitter error response: status code = 401":
				with open(data_dir+str(user)+".json", "w") as f:			# Cria arquivo vazio
					print ("Usuario inexistente. User: "+str(user)+" - Arquivo criado com sucesso!")
				key = random.randint(key_init,key_limit)
				api = authentication(auths)
			else:
				api = authentication(auths)
		except Exception as e2:
			print ("\n ERROR - ERROR ERROR - E2: "+str(e2)+"\n")
			api = authentication(auths)

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
					f.write(json.dumps(id)+"\n")
			print (str(coleta)+" - "+str(candidate)+": "+str(j)+"/"+str(l)+": "+str(user)+" - "+str(k)+" followers")
	
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
	for candidate in candidates:
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
	print("COLETA FINALIZADA!")

######################################################################################################################################################################
#
# INICIO DO PROGRAMA
#
######################################################################################################################################################################
	
################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
# Variáveis da coleta...
wait = 15
coleta = "followers"
candidates = ["alvaro","amoedo","bolsonaro","bolsonaro1turno","boulos","ciro","daciolo","eymael","geraldo","haddad","haddad1turno","henrique","marina"]
source_dir = "/home/twitterurt/ProjetoEleicao/data_id/"
data_dir = "/home/twitterurt/ProjetoEleicao/"+str(coleta)+"/json/"  ####### Diretorio para armazenamento dos arquivos JSON

################################### DEFINIR SE É TESTE OU NÃO!!! ### ['auths_ok'] OU  ['auths_test'] ################				
oauth_keys = multi_oauth.keys()
auths = oauth_keys['auths_ok']

key_init = 0					#################################################### Essas duas linhas atribuem as chaves para cada script
key_limit = len(auths)		#################################################### Usa todas as chaves (tamanho da lista de chaves)
key = random.randint(key_init,key_limit) ###################################### Inicia o script a partir de uma chave aleatória do conjunto de chaves

#Autenticacao
api = authentication(auths)

######################################################################################################################
######################################################################################################################
# Executa o metodo main
if __name__ == "__main__": main()