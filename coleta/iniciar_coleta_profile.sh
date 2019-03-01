#!/bin/bash
INTERVALO=600	#10 minutos
while true; do
	# Verifica se o python está sendo executado
	if pgrep -x "python" > /dev/null
	then
		echo "Executando"
	else
		echo "Iniciando..."
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/alvaro_profile_collect_wait_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/amoedo_profile_collect_wait_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/bolsonaro1turno_profile_collect_wait_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/bolsonaro_profile_collect_wait_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/boulos_profile_collect_wait_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/ciro_profile_collect_wait_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/daciolo_profile_collect_wait_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/eymael_profile_collect_wait_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/geraldo_profile_collect_wait_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/haddad1turno_profile_collect_wait_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/haddad_profile_collect_wait_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/henrique_profile_collect_wait_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/profile/marina_profile_collect_wait_v1.py; exec $SHELL";
	fi
	sleep $INTERVALO
done






