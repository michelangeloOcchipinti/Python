#20/10/2014 Occhipinti Michelangelo
#Esercitazione in classe:
#Calcolo dell'area e della circonferenza del cerchio.
#Calcolo del volume di una sfera.

#Importo il modulo math
import math

#Creo la funzione per calcolare l'area del cerchio
def AreaDelCerchio(raggio):
	return math.pi * (raggio ** 2)

#Creo la funzione per calcolare la circonferenza del cerchio
def Circonferenza(raggio):
	return math.pi * (2 * raggio)

#Creo la funzione per calcolare il diametro
def Diametro(raggio):
	return raggio*2

#Creo la funzione per calcolare il volume della sfera
def VolumeSfera (raggio):
        return (4*math.pi*raggio**3)/3
	
#Richiedo il valore del raggio all'utente
r = input("Raggio del Cerchio? ")

#Inserisco una riga vuota
print ""

#Richiamo le funzioni e stampo a video i risultati
print "Diametro \tCirconferenza \tArea\t\tVolume Sfera" 
print Diametro(r),"\t\t",
print Circonferenza(r),"\t",
print AreaDelCerchio(r),"\t",
print VolumeSfera(r), "\t"


