# -*- coding: latin1 -*-
################################################################################################
# Script para coletar a timeline dos usuarios que interagiram com os presidenciaveis durante a campanha eleitoral.
#	
#
import tweepy, datetime, sys, time, json, os, os.path, shutil, time, struct, random
import multi_oauth
#Script que contém as chaves para autenticação do twitter

reload(sys)
sys.setdefaultencoding('utf-8')


######################################################################################################################################################################
##		Status - Versao 1.0 - Coletar timeline dos usuarios especificados usando o Tweepy para controlar as autenticacoes
##						STATUS - Refazer a coleta at� que nao tenha nenhuma mensagem de "Rate Limit Exceeded"
##
######################################################################################################################################################################

######################################################################################################################################################################
#
# Realiza autenticacao
#
######################################################################################################################################################################

def autentication(auths):
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
# Converte formato data para armazenar em formato JSON
#
######################################################################################################################################################################
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            encoded_object = list(obj.timetuple())[0:6]
        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object

######################################################################################################################################################################
#
# Tweepy - Realiza a busca e devolve a timeline de um usuario especifico
#
######################################################################################################################################################################
def get_timeline(user):												#Coleta da timeline
	global key
	global dictionary
	global api
	global i
	timeline = []
	try:
		for page in tweepy.Cursor(api.user_timeline,id=user,count=200,wait_on_rate_limit_notify=True,wait_on_rate_limit=True).pages(16):				#Retorna os últimos 3200 tweets (16*20)
			for tweet in page:
				timeline.append(tweet)
		return (timeline)
	
	except tweepy.error.RateLimitError as e:
			print("Limite de acesso a�API excedido. User: "+str(user)+" - Autenticando novamente... "+str(e))
			api = autentication(auths)

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		error = {}
		with open(error_dir+"timeline_collect.err", "a+") as outfile:								# Abre o arquivo para gravacao no final do arquivo
			if e.message:
				error = {'user':user,'reason': e.message,'date':agora, 'key':key}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
				print error
			else:
				error = {'user':user,'reason': str(e),'date':agora, 'key':key}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n") 
				print error
		try:
			if e.message[0]['code'] == 32 or e.message[0]['code'] == 215:
				key = random.randint(key_init,key_limit)
				api = autentication(auths)
			if e.message[0]['code'] == 34:									# Usuários não existentes
				dictionary[user] = user											# Insere o usuário coletado na tabela em memória
				with open(data_dir+str(user)+".json", "w") as f:			# Cria arquivo vazio	
					print ("Usuario inexistente. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1
		except Exception as e2:
			print ("E2: "+str(e2))
		
		try:
			if e.message == 'Not authorized.': # Usuarios nao autorizados
				dictionary[user] = user											# Insere o usuário coletado na tabela em memória
				with open(data_dir+str(user)+".json", "w") as f:			# Cria arquivo vazio
					print ("Usuario nao autoriza coleta. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1	
		except Exception as e3:
			print ("E3: "+str(e3))
######################################################################################################################################################################
#
# Obtem timeline dos usuarios
#
######################################################################################################################################################################
def save_timeline(j,user): # j = numero do usuario que esta sendo coletado
	global i	# numero de usuarios com arquivos ja coletados / Numero de arquivos no diretorio
	 
	# Dicionario - Tabela Hash contendo os usuarios ja coletados
	global dictionary

	#Chama a funcao e recebe como retorno a lista de tweets do usuario
	k = 0 																# Numero de Tweets por usuario
	timeline = get_timeline(user)
	if timeline:	
		try:
			with open(data_dir+str(user)+".json", "w") as f:	
				for tweet in timeline:
					k+=1
					f.write(json.dumps(tweet._json)+"\n")		# ... no arquivo, imprime o tweet (status) inteiro.
			
			dictionary[user] = user									# Insere o usuario coletado na tabela em memoria
			i +=1
			print ("Usuario numero "+str(j)+": "+str(user)+" coletado com sucesso. "+str(k)+" tweets. Total de usuarios coletados: "+str(i))
	
		except Exception as e:	
			agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
			with open(error_dir+"timeline_collect.err", "a+") as outfile:								# Abre o arquivo para gravacao no final do arquivo
				if e.message:		
					error = {'user':user,'reason': e.message,'date':agora}
				else:
					error = {'user':user,'reason': str(e),'date':agora}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
				print error
			if os.path.exists(data_dir+str(user)+".json"):
				os.remove(data_dir+str(user)+".json")


######################################################################################################################################################################
######################################################################################################################################################################
#
# Metodo principal do programa.
# Realiza teste e coleta a timeline do user especificado no arquivo. 
#
######################################################################################################################################################################
######################################################################################################################################################################

def main():
	global i 												# Numero de usuarios com arquivos ja coletados / Numero de arquivos no diretorio
	j = 0													# Exibe o numero ordinal do usu�rio que esta sendo usado para a coleta da timeline
	with open(users_file, r) as file:
		users_id = file.readlines()
		for user in users_id:
			print user
#			j+=1
#			if not dictionary.has_key(user):
#				save_timeline(j, user)						#Inicia funcao de busca da timeline
	print()
	print("######################################################################")
	print("Coleta finalizada!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INICIO DO PROGRAMA
#
######################################################################################################################################################################

################################### DEFINIR SE SERA TESTE OU NAO!!! ### ['auths_ok'] OU  ['auths_test'] ################
oauth_keys = multi_oauth.keys()
auths = oauth_keys['auths_test']
	
################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################

key_init = 0					################################################# Essas duas linhas atribuem as chaves para cada script
key_limit = len(auths)		##################################################### Usa todas as chaves (tamanho da lista de chaves)
key = random.randint(key_init,key_limit) ######################################## Inicia o script a partir de uma chave aleatoria do conjunto de chaves

users_file = "/home/amaury/coleta/users.txt"
data_dir = "/home/amaury/coleta/timeline/json/" ####### Diretorio para armazenamento dos arquivos JSON
error_dir = "/home/amaury/coleta/timeline/error/" ##### Diretorio para armazenamento dos arquivos de erro
wait = 5
dictionary = {}				#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
######################################################################################################################
######################################################################################################################
######################################################################################################################
#Cria os diretorios para armazenamento dos arquivos
if not os.path.exists(data_dir):
	os.makedirs(data_dir)
if not os.path.exists(error_dir):
	os.makedirs(error_dir)

###### Iniciando dicionario - tabela hash a partir dos arquivos ja criados.
print
print("######################################################################")
print ("Criando tabela hash...")
i = 0	#Conta quantos usuarios ja foram coletados (todos arquivos no diretorio)
for file in os.listdir(data_dir):
	user_id = file.split(".json")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")
#Autenticacao
api = autentication(auths)

	
#Executa o metodo main
if __name__ == "__main__": main()