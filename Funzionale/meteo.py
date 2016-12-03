import random

citta=[['Venezia',0],['Vicenza',0],['Verona',0],['Padova',0],['Rovigo',0],['Belluno',0],['Treviso',0]]

i=0
pericolo=0
umiditaMax=0
umiditaMin=100
umiditaMedia=0
cittaMax=""
cittaMin=""
nome_manutentore="Gianni Pericopo"
telefono_manutentore="3335897452"

while i<len(citta):
	umidita=random.random()*100
	citta[i][1]=umidita
	umiditaMedia=umiditaMedia+umidita/(i+1)
	if umidita>90:
		pericolo+=1 
	if umidita>umiditaMax:
		umiditaMax=umidita
		cittaMax=citta[i][0]
	if umidita<umiditaMin:
		umiditaMin=umidita
		cittaMin=citta[i][0]
	i+=1

print "\nL'umidita' media tra le provincie del Veneto e' uguale al "+str(round(umiditaMedia,2))+"%\nL'umidita' minima rilevata e' pari al "+str(round(umiditaMin,2))+"% nella citta' di "+cittaMin+"\nE l'umidita' massima misurata e' invece pari al "+str(round(umiditaMax,2))+"% nella citta' di "+cittaMax+"\n"

if pericolo>4 :
	print "Attenzione! Pericolo nebbia!"

if umiditaMin<20:
	print "Attenzione! Errore umidita' sotto al 20% nella centralina della citta' di "+cittaMin+" contattare "+nome_manutentore+" al telefono "+telefono_manutentore


