"""
Esercizio "Corsa delle rane" Python Object Oriented programming (testo e consegna)

Creare il programma in Python Object Oriented che simuli la situazione esposta in seguito (completo di diagramma UML e FlowChart dei metodi, esclusi quelli di set e get) 

In un famosa fiera annuale si compie la Corsa delle Rane che prevede che due rane si fronteggino su un percorso di 6 m e avanzino saltando ripetutamente di una distanza che dipende dal peso della rana. Vince chi per prima arriva a tagliare il traguardo. 

Simulare tale competizione affrontando le tre fasi

- iscrizione delle rane concorrenti

- inizio e svolgimento gara

- declamazione della classifica finale con dati riassuntivi della gara
"""


#Importo i moduli e le classi di cui avro' bisogno in seguito
import Rana
import Corsa
import time
#Istanzio l'oggetto di tipo Corsa
corsa2016=Corsa.Corsa(6,5)
#Salvo in una variabile la distanza totale del percorso impostata
distanza=corsa2016.getDistPercorso()
    
print   
print "Benvenuti al nuovo challenge Rane 2016!!"
print
time.sleep(1.5)
#Richiamo il metodo per l'iscrizione delle rane
corsa2016.iscrizioneRane()

#Salvo in una variabile la lista con gli oggetti Rana iscritti
#alla gara per utilizzarli nelle fasi di stampa a video del risultato finale.
rane=corsa2016.getRaneIscritte()

print "Tutte le rane sono state iscritte! Si parte!"
print
time.sleep(1)

print "La gara iniziera' tra "
print
print "3"
time.sleep(1)
print "2"
time.sleep(1)
print "1"
time.sleep(1)
print
print "Via"
time.sleep(2)
#Inizializzo una variabile per salvare poi ad ogni giro il  primo in classifica e all'ultimo giro utilizzarlo per stampare a video la rana vincitrice.
primoInClassifica=0
#Aggiungo un indice che mi servira' per passarlo come parametro al metodo saltoGara() per stampare a video il numero di giro al quale siamo arrivati con la classifica.
i=1
#Utilizzo un ciclo iterativo per simulare la gara richiamando il metodo saltoGara() dell'oggetto corsa2016 di tipo Corsa
while primoInClassifica<distanza:
    corsa2016.saltoGara(i)
    primoInClassifica=rane[0].getDistPercorsa()
    i+=1

print
time.sleep(1)
print "Siamo arrivati alla fine del rana challenge 2016!"
print
time.sleep(2)
print "Ora decreteremo il vincitore per questa edizione annuale!!"
print
time.sleep(2)
print "3"
time.sleep(1)
print "2"
time.sleep(1)
print "1"
time.sleep(1)
print
print "Il vincitore di questa edizione e' la rana "+rane[0].getNome()+" con il salto piu' lungo pari a "+str(round(rane[0].getSaltoMax(),2))+" metri e la bellezza di "+str(round(rane[0].getDistPercorsa(),2))+" metri percorsi!!"
    

