#!/bin/bash
INTERVALO=600	#10 minutos
while true; do
	# Verifica se o python está sendo executado
	if pgrep -x "python" > /dev/null
	then
		echo "Executando"
	else
		echo "Iniciando..."
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/alvaro_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/amoedo_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/bolsonaro1turno_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/bolsonaro_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/boulos_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/ciro_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/daciolo_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/eymael_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/geraldo_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/haddad1turno_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/haddad_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/henrique_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/profile/marina_v1.py; exec $SHELL";
	fi
	sleep $INTERVALO
done






