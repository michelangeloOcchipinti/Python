#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Esercizio "Cinema" Python programmazione funzionale (testo e consegna)

Creare il programma in Python funzionale che simuli la situazione esposta in seguito (completo di FlowChart ) 

Si vuole realizzare un software che gestisca tre sale cinematografiche.
La SalaCinema ha il seguente insieme di attributi minimali: film (nome del film proiettato), prezzoFilm (prezzo di un singolo biglietto), numero di file (numero di file degli spettatori), maxPerFila (numero massimo di spettatori per fila), posti Occupati (nr di biglietti gia' venduti per la sala), incasso.

Il software gestira' l'accesso alle sale tramite vendita di biglietti.L'operatore in cassa dovra' richiedere il titolo del film, che il cliente vuole vedere, e procedere alla vendita dei biglietti (senza che il biglietto sia assegnato ad un posto preciso); quindi all’aggiornamento della situazione prima del cliente successivo.
In ogni momento deve essere possibile stampare un report sull'occupazione delle sale (posti liberi e occupati) e incasso effettuato"""

#Importo le classi del progetto che utilizzero' in seguito
import SalaCinema
import Film
import Cinema

#Creo gli oggetti delle tre classi importate
film1=Film.Film('Matrix',6.99)
film2=Film.Film('Senorita',9.99)
film3=Film.Film('Leon',3.99)
sala1=SalaCinema.SalaCinema(10,20,film1)
sala2=SalaCinema.SalaCinema(20,15,film2)
sala3=SalaCinema.SalaCinema(30,10,film3)

saleCinema=[sala1,sala2,sala3]

cinema=Cinema.Cinema(saleCinema)

#Creo tre variabili in cui memorizzo i posti totali disponibili per ogni sala
postiSala1=sala1.getNumFile()*sala1.getMaxPerFila()
postiSala2=sala2.getNumFile()*sala2.getMaxPerFila()
postiSala3=sala3.getNumFile()*sala3.getMaxPerFila()

#Creo un ciclo per la vendita dei biglietti che continuera' finche' ci saranno posti disponibili almeno in una sala
while sala1.getPostiOccupati()<postiSala1 or sala2.getPostiOccupati()<postiSala2 or sala3.getPostiOccupati()<postiSala3:
    
    #Salvo in una variabile il return del metodo ricercaTitolo()
    salaAttuale=cinema.ricercaTitolo()
    
    #Richiamo il metodo venditaBiglietti()
    cinema.venditaBiglietti(salaAttuale)
    
    #Stampo a video la situazione aggiornata del cinema
    cinema.stampaReport()
