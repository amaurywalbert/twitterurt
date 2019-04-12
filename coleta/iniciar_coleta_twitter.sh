#!/bin/bash
INTERVALO=600	#10 minutos
while true; do
	# Verifica se o python está sendo executado
	if pgrep -x "python" > /dev/null
	then
		echo "Executando"
	else
		echo "Iniciando..."

# Profile
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/alvaro.py; exec $SHELL";
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/amoedo.py; exec $SHELL";
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/bolsonaro1turno.py; exec $SHELL";
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/bolsonaro.py; exec $SHELL";
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/boulos.py; exec $SHELL";
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/ciro.py; exec $SHELL";
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/daciolo.py; exec $SHELL";
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/eymael.py; exec $SHELL";
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/geraldo.py; exec $SHELL";
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/haddad1turno.py; exec $SHELL";
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/haddad.py; exec $SHELL";
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/henrique.py; exec $SHELL";
# OK		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/marina.py; exec $SHELL";

# Timeline - Precisa rever a coleta, temos que salvar apenas alguns dados e no toda a timeline. Problemas com espaço em disco...
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/alvaro.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/amoedo.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/bolsonaro1turno.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/bolsonaro.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/boulos.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/ciro.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/daciolo.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/eymael.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/geraldo.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/haddad1turno.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/haddad.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/henrique.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/marina.py; exec $SHELL";

# Friends - Fazendo um teste com o script "todos.py" em substituição a scripts de coleta por candidato individual.
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/alvaro.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/amoedo.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/bolsonaro1turno.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/bolsonaro.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/boulos.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/ciro.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/daciolo.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/eymael.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/geraldo.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/haddad1turno.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/haddad.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/henrique.py; exec $SHELL";
#		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/marina.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/friends/todos.py; exec $SHELL";

# Followers
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/alvaro.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/amoedo.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/bolsonaro1turno.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/bolsonaro.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/boulos.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/ciro.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/daciolo.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/eymael.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/geraldo.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/haddad1turno.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/haddad.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/henrique.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/followers/marina.py; exec $SHELL";
	fi
	sleep $INTERVALO
done






