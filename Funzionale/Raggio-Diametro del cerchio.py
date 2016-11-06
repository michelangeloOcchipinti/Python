#20/10/2014 Occhipinti Michelangelo
#Esercitazione in classe:
#Calcolo del raggio e del diametro del cerchio.

#Importo il modulo math
import math

#Creo la funzione per calcolare il raggio del cerchio
def Raggio (circonferenza):
    return circonferenza/(2*math.pi)

#Creo la funzione per calcolare il diametro del cerchio
def Diametro (circonferenza):
    return circonferenza/(math.pi)

#Definisco la funzione che richiama entrambe le precedenti funzioni
def RaggioDiametro (circonferenza):
    print Raggio (circonferenza),"\t\t",
    return Diametro (circonferenza)

#Richiedo il dato della circonferenza all'utente
c = input ("Inserisci il valore della circonferenza ")

#Inserisco una riga vuota
print ""

#Stampo a video le descrizioni dei due risultati
print ("Raggio del cerchio"), "\t",
print ("Diametro del cerchio")

#Richiamo la funzione e stampo a video i risultati
print RaggioDiametro (c)


    
