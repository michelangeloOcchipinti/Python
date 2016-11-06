# -*- coding: cp1252 -*-
""" Esercizio sulle liste Compito

Realizzare un programma in grado di produrre una lista di numeri casuali di lunghezza parametrica.

Produrre e verificare una funzione di ricerca ingenua in grado di cercare la prima posizione di un valore nella lista di numeri casuali.

Prudurre una funzione in grado di riordinari i dati nella lista

Produrre una funzione di ricerca efficiente che sfruttando il fatto che lista è ordinata esegue una ricerca "intelligente" arrivando alla posizione del valore cercato in modo più efficiente.

Puoi consegnare fino a tre diverse versioni dello stesso programma."""

# ***VERSIONE 2.0 CON ORDINAMENTO MIGLIORATO***

# Creo una lista parametrica e casuale nell'intervallo 1:100.
# Il range può essere facilmente cambiato agendo sui parametri del metodo random.randint.

import random
def CreaLista (QuantoLungo):
    lista=[0]*QuantoLungo
    indice=0
    while indice<QuantoLungo:
        lista[indice]=random.randint(1,100)
        indice=indice+1
    print lista
    return lista

# Svolgo una ricerca semplice all'interno della lista casuale su input dell'utente.   

def RicercaIngenua(MiaLista,valore):
    indice=0
    while indice<len(MiaLista):
        if valore==MiaLista[indice]:
            return indice
        indice=indice+1
        
    return "Il valore non è stato trovato."

# Ordino la lista casuale generata e la stampo a video.
# L'algoritmo 2.0 creato è composto da un ciclo esterno e da un ciclo inrterno.
# Il ciclo esterno mi permette di ciclare la lista per le volte pari al numero di elementi della lista -1.
# Il ciclo interno invece cicla tutta la lista per le volte del ciclo esterno confrontando l'elemento precedente a quello successivo.
# Ogni volta che l'elemento precedente è superiore a quello successivo li scambia tra loro attraverso una variabile di appoggio.
# Per 1000 elmenti in lista l'ordinamento 1.0 aveva tempi che superavano il minuto, questa versione 2.0 ha tempi che non superano il singolo secondo. 

def Ordinamento (MiaLista):
    indiceEsterno=0
    indiceInterno=0
    scambio=0
    while indiceEsterno<len(MiaLista)-1:
        indiceInterno=0
        while indiceInterno<len(MiaLista)-1:
            if MiaLista[indiceInterno]>MiaLista[indiceInterno+1]:
                scambio=MiaLista[indiceInterno]
                MiaLista[indiceInterno]=MiaLista[indiceInterno+1]
                MiaLista[indiceInterno+1]=scambio
            indiceInterno=indiceInterno+1
        indiceEsterno=indiceEsterno+1
    return MiaLista
    

# Cerco all'interno della lista ordinata attraverso un algoritomo che suddivide i valori totali in due blocchi e controlla a quale
# metà appartiene il valore inserito dall'utente.
# Una volta controllato e trovata la metà giusta suddivide nuovamente in due parti la metà corrispondente e una volta trovato
# il blocco a cui appartiene il valore questa volta esegue una scansione della parte di valori corrispondenti fino a trovare quello
# cercato oppure a dare in output il messaggio di mancato ritrovamento del valore.

def RicercaVeloce(lista,valore):   
    lunghezza=len(lista)
    meta=lunghezza/2
    if valore<=lista[meta-1]:
        metameta=meta/2
        if valore<=lista[metameta-1]:
            indice=0
            while indice<=metameta-1:
                if lista[indice]==valore:
                    return indice
                indice=indice+1
            
        elif valore>lista[metameta-1]:
            indice=metameta
            while indice<=meta-1:
                if lista[indice]==valore:
                    return indice
                indice=indice+1
            
    elif valore>=lista[meta]:
        metameta=meta+meta/2
        if valore<=lista[metameta-1]:
            indice=meta
            while indice<=metameta-1:
                if valore==lista[indice]:
                    return indice
                indice=indice+1
        elif valore>=lista[metameta]:
            indice=metameta
            while indice<=len(lista)-1:
                if valore==lista[indice]:
                    return indice
                indice=indice+1

    return "Il valore cercato non e' stato trovato"
    
    
                

QuantoLungo=input("Inserisci quanti elementi vuoi aggiungere alla lista: ")
MiaLista=CreaLista(QuantoLungo)

valore=input("Inserisci il valore da ricercare nel database: ")
print ("Il valore e' stato trovato in posizione: "),RicercaIngenua(MiaLista,valore)

print "La lista ordinata e' uguale a: ",Ordinamento(MiaLista)

valore=input("Inserisci il valore da ricercare nella lista ordinata: ")
MiaListaOrdinata=Ordinamento(MiaLista)

print "Il valore cercato si trova nella posizione: ",RicercaVeloce(MiaListaOrdinata,valore)




