# -*- coding: latin1 -*-
################################################################################################
# Script para coletar a timeline dos usuarios que interagiram com os presidenciaveis durante a campanha eleitoral.
#	
#
import tweepy, datetime, sys, json, os, os.path, shutil, time, struct, random
#Script que contÃ©m as chaves para autenticaÃ§Ã£o do twitter

reload(sys)
sys.setdefaultencoding('utf-8')


######################################################################################################################################################################
##		Status - Versao 1.0 - Coletar perfil dos usuarios especificados por cada candidato... esperando o período das janelas.
##						STATUS - Refazer a coleta até que nao tenha nenhuma mensagem de "Rate Limit Exceeded"
##
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
# Tweepy - Realiza a busca e devolve a perfil de um usuario especifico
#
######################################################################################################################################################################
def get_profile(user):												#Coleta do Perfil
	global dictionary
	global api
	global i
	try:
		profile = api.get_user(id=user,wait_on_rate_limit_notify=True,wait_on_rate_limit=True)
		return (profile)

	except tweepy.error.TweepError as e:
		agora = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M')				# Recupera o instante atual na forma AnoMesDiaHoraMinuto
		error = {}
		with open(error_dir+"timeline_collect.err", "a+") as outfile:								# Abre o arquivo para gravacao no final do arquivo
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
				dictionary[user] = user										# Insere o usuário coletado na tabela
				with open(data_dir+str(user)+".json", "w") as f:			# Cria arquivo vazio
					print ("Usuario nao autoriza coleta. User: "+str(user)+" - Arquivo criado com sucesso!")
				i +=1	
		except Exception as e3:
			print ("E3: "+str(e3))
######################################################################################################################################################################
#
# Obtem perfil dos usuarios
#
######################################################################################################################################################################
def save_profile(j,l,user): # j = numero do usuario que esta sendo coletado
	global i	# numero de usuarios com arquivos ja coletados / Numero de arquivos no diretorio
	 
	# Dicionario - Tabela Hash contendo os usuarios ja coletados
	global dictionary

	#Chama a funcao e recebe como retorno o perfil do usuário
	profile = get_profile(user)
	if profile:
		try:
			with open(data_dir+str(user)+".json", "w") as f:

				f.write(json.dumps(profile._json)+"\n")		# ... no arquivo, imprime o perfil completo.
			dictionary[user] = user									# Insere o usuario coletado na tabela em memoria
			i +=1
			print ("Total: "+str(i)+" - "+str(candidate)+": "+str(j)+"/"+str(l)+": "+str(user))

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
#
#
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
					save_profile(j,l, user)						#Inicia funcao de busca da timeline
	print("######################################################################")
	print("Coleta finalizada!")
	print("######################################################################\n")

######################################################################################################################################################################
#
# INICIO DO PROGRAMA
#
######################################################################################################################################################################

################################### CONFIGURAR AS LINHAS A SEGUIR ####################################################
######################################################################################################################
################################### CHAVE E AUTENTICAÇÃO
##############################################################################################################
#		Conta: walbert1810 - user: walbert1810 - e-mail: amaurywalbert@live.com - senha: padrão
#
#msc20160012_teste_21 - JoaoAmoedo
consumer_key = "qvmfyEldFvEmTCAvzFSBTP1wz"
consumer_secret = "L4CQ640r3u72eMbdQaw4AvICRJOqSyu2pLpXi60ottICSgOuKA"
access_token = "786664983862083584-jWBk9sZ6kLSPuArjaUdOMpJbblcFxD0"
access_token_secret = "in67CMCZSDrVGLiPAP0iri5sfEzqRy3qsNOplPer2C2aQ"
#
candidate = "amoedo"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

####################  ARMAZENAMENTO DOS DADOS ###############################################################
#############################################################################################################
source_dir = "/home/twitterurt/ProjetoEleicao/data_id/"
data_dir = "/home/twitterurt/ProjetoEleicao/profile/json/" ####### Diretorio para armazenamento dos arquivos JSON
error_dir = "/home/twitterurt/ProjetoEleicao/profile/error/" ##### Diretorio para armazenamento dos arquivos de erro

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
dictionary = {}	#################################################### Tabela {chave:valor} para facilitar a consulta dos usuários já coletados
i = 0	#Conta quantos usuarios ja foram coletados (todos arquivos no diretorio)
for file in os.listdir(data_dir):
	user_id = file.split(".json")
	user_id = long(user_id[0])
	dictionary[user_id] = user_id
	i+=1
print ("Tabela hash criada com sucesso...") 
print("######################################################################\n")
	
#Executa o metodo main
if __name__ == "__main__": main()
