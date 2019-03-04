# -*- coding: latin1 -*-
################################################################################################
# Script para coletar a timeline dos usuarios que interagiram com os presidenciaveis durante a campanha eleitoral.
#	
#
import tweepy, datetime, sys, json, os, os.path, shutil, time, struct, random

reload(sys)
sys.setdefaultencoding('utf-8')


######################################################################################################################################################################
##		Status - Versao 1.0 - Coletar timeline dos usuarios especificados usando o Tweepy para controlar as autenticacoes ##
######################################################################################################################################################################

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
	global dictionary
	global api
	global i
	timeline = []
	try:
		for page in tweepy.Cursor(api.user_timeline,id=user,count=200,wait_on_rate_limit_notify=True,wait_on_rate_limit=True).pages(16):	#Retorna os ultimos 3200 tweets (16*20)
			for tweet in page:
				timeline.append(tweet)
		return (timeline)

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		error = {}
		with open(error_dir+"timeline_collect.err", "a+") as outfile:							# Abre o arquivo para gravacao no final do arquivo
			if e.message:
				error = {'user':user,'reason': e.message,'date':agora}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n")
				print error
			else:
				error = {'user':user,'reason': str(e),'date':agora}
				outfile.write(json.dumps(error, cls=DateTimeEncoder, separators=(',', ':'))+"\n") 
				print error
		try:
			if e.message[0]['code'] == 34 or e.message[0]['code'] == 50 or e.message[0]['code'] == 63:	# Usuário não existente/
				dictionary[user] = user										# Insere o usuário coletado na tabela
				with open(data_dir+str(user)+".json", "w") as f:			# Cria arquivo vazio	
					print ("Usuario inexistente. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1
		except Exception as e2:
			print ("E2: "+str(e2))
		
		try:
			if e.message == 'Not authorized.': # Usuarios nao autorizados
				dictionary[user] = user										# Insere o usuario coletado na tabela
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
def save_timeline(j,l,user): # j = numero do usuario que esta sendo coletado
	global i	# numero de usuarios com arquivos ja coletados / Numero de arquivos no diretorio
	 
	# Dicionario - Tabela Hash contendo os usuarios ja coletados
	global dictionary

	#Chama a funcao e recebe como retorno a lista de tweets do usuario
	timeline = get_timeline(user)
	if timeline:	
		try:
			with open(data_dir+str(user)+".json", "w") as f:
				k=0
				for tweet in timeline:
					k+=1
					f.write(json.dumps(tweet._json)+"\n")		# ... no arquivo, imprime o tweet (status) inteiro.
			
			dictionary[user] = user									# Insere o usuario coletado na tabela em memoria
			i +=1
			print ("Total: "+str(i)+" - "+str(candidate)+": "+str(j)+"/"+str(l)+": "+str(user)+" - "+str(k)+" tweets")
	
		except Exception as e:	
			agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')			# Recupera o instante atual na forma AnoMesDiaHoraMinuto
			with open(error_dir+"timeline_collect.err", "a+") as outfile:						# Abre o arquivo para gravacao no final do arquivo
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
	global i 												# Numero de usuarios com arquivos ja coletados / Numero de arquivos no diretorio													# Exibe o numero ordinal do usuário que esta sendo usado para a coleta da timeline
	for file in os.listdir(source_dir+candidate):
		with open(source_dir+candidate+"/"+file, "r") as f:
			users_id = f.readlines()
			j = 0
			l = len(users_id)
			for user in users_id:
				user = long(user)
				j+=1
				if not dictionary.has_key(user):
					save_timeline(j,l,user)						#Inicia funcao de busca da timeline
	print("######################################################################")
	print(str(candidate)+" - Coleta finalizada!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INICIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
################################### CHAVE E AUTENTICAÇÃO
#     Conta: msc20160012_app02 - user: msc2016002_app2 - e-mail: twitter02msc20160012@gmail.com - senha: padrão
#
#
# msc20160012_11 - Alvaro
consumer_key = "O4t25YPnHGNm7B1i5qaN7Gu3s"
consumer_secret = "v298502i9HF2vpFbpOwrvEnYIucp2CVwLU8MPfy2lLGh6AoFXR"
access_token = "813460676475842560-gX5XA6C8kWOk412pFQOMy4HZgJ9fSMi"
access_token_secret = "VLO9eKX8TQhKjH3VPoR2asgxZ9qudY3NW5XFUhXg7iJQB"
#
candidate = "alvaro"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

####################  ARMAZENAMENTO DOS DADOS ###############################################################
#############################################################################################################
source_dir = "/home/twitterurt/ProjetoEleicao/data_id/"
data_dir = "/home/twitterurt/ProjetoEleicao/timeline/json/"  ####### Diretorio para armazenamento dos arquivos JSON
error_dir = "/home/twitterurt/ProjetoEleicao/timeline/error/"  ##### Diretorio para armazenamento dos arquivos de erro

######################################################################################################################
######################################################################################################################
# Cria os diretorios para armazenamento dos arquivos
if not os.path.exists(data_dir):
	os.makedirs(data_dir)
if not os.path.exists(error_dir):
	os.makedirs(error_dir)

###### Iniciando dicionario - tabela hash a partir dos arquivos ja criados.
print
print("######################################################################")
print("Criando tabela hash...")
dictionary = {}  #################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
i = 0  # Conta quantos usuarios ja foram coletados (todos arquivos no diretorio)
for file in os.listdir(data_dir):
	user_id = file.split(".json")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i += 1
print("Tabela hash criada com sucesso...")
print("######################################################################\n")

# Executa o metodo main
if __name__ == "__main__": main()