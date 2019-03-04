#!/bin/bash
INTERVALO=600	#10 minutos
while true; do
	# Verifica se o python está sendo executado
	if pgrep -x "python" > /dev/null
	then
		echo "Executando"
	else
		echo "Iniciando..."
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/alvaro_profile_collect_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/amoedo_profile_collect_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/bolsonaro1turno_profile_collect_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/bolsonaro_profile_collect_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/boulos_profile_collect_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/ciro_profile_collect_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/daciolo_profile_collect_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/eymael_profile_collect_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/geraldo_profile_collect_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/haddad1turno_profile_collect_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/haddad_profile_collect_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/henrique_profile_collect_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/amaury/twitterurt/coleta/timeline/marina_profile_collect_v1.py; exec $SHELL";
	fi
	sleep $INTERVALO
done






