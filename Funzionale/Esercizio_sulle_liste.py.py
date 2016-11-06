# -*- coding: cp1252 -*-
""" Esercizio sulle liste Compito

Realizzare un programma in grado di produrre una lista di numeri casuali di lunghezza parametrica.

Produrre e verificare una funzione di ricerca ingenua in grado di cercare la prima posizione di un valore nella lista di numeri casuali.

Prudurre una funzione in grado di riordinari i dati nella lista

Produrre una funzione di ricerca efficiente che sfruttando il fatto che lista è ordinata esegue una ricerca "intelligente" arrivando alla posizione del valore cercato in modo più efficiente.

Puoi consegnare fino a tre diverse versioni dello stesso programma."""

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
# L'algoritmo creato prevede di ciclare la lista per mezzo dell'istruzione while dal primo valore fino all'ultimo.
# Nel caso durante il ciclo trovi un valore minore successivo ad uno precedente si ferma e cambia l'ordine dei due valori.
# A questo punto un'altro ciclo while esegue la stessa operazione al contrario verso l'alto con il valore scambiato
# fino all'inizio della lista e nel caso trovi valori più alti rispetto a quello oggetto'operazione li scambia tra loro.
# Una volta arrivato all'inizio della lista torna a ciclare fino ad aver ordinato tutti i valori della lista. 

def Ordinamento (MiaLista):
    indice=0
    a=0
    while indice<len (MiaLista)-1:
        if MiaLista[indice]>MiaLista[indice+1]:
            a=MiaLista[indice]
            MiaLista[indice]=MiaLista[indice+1]
            MiaLista[indice+1]=a
            while indice!=0:
                    a=MiaLista[indice-1]
                    MiaLista[indice-1]=MiaLista[indice]
                    MiaLista[indice-1]=a
                    indice=indice-1        
        else:
            indice=indice+1
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




