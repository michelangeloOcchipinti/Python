#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#Classe che crea cinema multisala come oggetti
import time

class Cinema:
    #Metodo costruttore che salva il parametro attuale con la lista delle sale del cinema creato in una variabile 
    def __init__(self, saleCinema):
        self.saleCinema=saleCinema
        
    #Metodo che utilizzo per la ricerca del titolo inserito dall'operatore all'interno della lista delle sale
    def ricercaTitolo(self):
        
        print "\nBenvenuti al MultiSala Marconi\n"
        time.sleep(1.5)
        print "Scegliere ed inserire il titolo del film tra quelli proposti nella lista sotto:\n"

        #Ciclo che stampa a video la lista dei film disponibili 
        for film in self.saleCinema:
            print film.getFilmInProiezione().getTitolo()
        print
        
        #Salvo nella variabile film il titolo inserito dall'operatore
        self.film=raw_input()
        print
        i=0
        
        #Setto a 'None' la variabile salaAttuale per utilizzarla come riferimento nel ciclo successivo
        self.salaAttuale=None
        
        #Creo un ciclo che trova il titolo inserito dall'operatore all'interno dei titoli disponibili del cinema  restituendo l'oggetto SalaCinema relativo. Se non trovera' nessuna occorrenza restituira' il valore None. 
        while self.salaAttuale==None and i<len(self.saleCinema):
            if self.film==self.saleCinema[i].getFilmInProiezione().getTitolo():
                self.salaAttuale=self.saleCinema[i]
                return self.salaAttuale
                i=len(self.saleCinema)
            i+=1
    
    #Creo il metodo che effettuera' la vendita dei biglietti
    def venditaBiglietti(self, salaAttuale):
        #Se il valore dell'oggetto passato come  parametro attuale avra' valore None allora restituiro' a video il messaggio di film non trovato
        if self.salaAttuale==None:
            print "Il film ricercato non esiste."
            time.sleep(1)
        #nel caso venga trovato il film e ci siano posti sufficienti disponibili proseguo calcolando il costo totale e scrivendolo a video oltre ad aggiornare l'incasso totale della relativa sala e i posti occupati. 
        else:
            print "Inserire il numero di biglietti:"
            self.numBiglietti=input()
            print
            if self.numBiglietti<=self.salaAttuale.getNumFile()*self.salaAttuale.getMaxPerFila()-self.salaAttuale.getPostiOccupati():
                self.costoTotale=self.salaAttuale.getFilmInProiezione().getPrezzo()*self.numBiglietti
                print "Il costo totale dei biglietti e' pari a: "+str(self.costoTotale)+" euro\n"
                time.sleep(1.5)
                self.salaAttuale.setPostiOccupati(self.salaAttuale.getPostiOccupati()+self.numBiglietti)
                self.salaAttuale.setIncasso(self.salaAttuale.getIncasso()+self.costoTotale)
            else:
                    print "Non sono disponibili posti sufficienti per il film scelto."
    #Metodo che stampa a video il report della sala per quanto riguarda il titolo, i posti occupati e l'incasso totale.
    def stampaReport(self):
        print "\nStatistiche vendita e posti disponibili aggiornati nel multisala Marconi:\n"
        time.sleep(2)
        for film in self.saleCinema:
            print "Titolo: "+film.getFilmInProiezione().getTitolo()
            print "Posti disponibili: "+str(film.getNumFile()*film.getMaxPerFila()-film.getPostiOccupati())+" su "+str(film.getNumFile()*film.getMaxPerFila())+" posti totali."
            print "Incasso: "+str(film.getIncasso())
            print
        time.sleep(2)
            
        

        
        
    
