#!/bin/bash
INTERVALO=600	#10 minutos
while true; do
	# Verifica se o python está sendo executado
	if pgrep -x "python" > /dev/null
	then
		echo "Executando"
	else
		echo "Iniciando..."
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/alvaro_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/amoedo_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/bolsonaro1turno_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/bolsonaro_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/boulos_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/ciro_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/daciolo_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/eymael_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/geraldo_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/haddad1turno_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/haddad_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/henrique_v1.py; exec $SHELL";
		gnome-terminal -x bash -c "python /home/twitterurt/twitterurt/coleta/timeline/marina_v1.py; exec $SHELL";
	fi
	sleep $INTERVALO
done






