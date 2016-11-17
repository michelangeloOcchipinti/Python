import time

class Cinema:

    def __init__(self, saleCinema):
        self.saleCinema=saleCinema

    def ricercaTitolo(self):
        
        print "Benvenuti al MultiSala Marconi\n"
        print "Scegliere il film tra quelli proposti nella lista sotto:\n"

        for film in self.saleCinema:
            print film.getFilmInProiezione().getTitolo()
        print
        self.film=raw_input()
        print
        i=0
        self.salaAttuale=None
        while self.salaAttuale==None and i<len(self.saleCinema):
            if self.film==self.saleCinema[i].getFilmInProiezione().getTitolo():
                print self.saleCinema[i].getFilmInProiezione().getTitolo()
                self.salaAttuale=self.saleCinema[i]
                return self.salaAttuale
                i=len(self.saleCinema)
            i+=1

    def venditaBiglietti(self, salaAttuale):
        
        if self.salaAttuale==None:
            print "Il film ricercato non esiste."
            time.sleep(1)
        else:
            print "Inserire il numero di biglietti:"
            self.numBiglietti=input()
            print
            if self.numBiglietti<=self.salaAttuale.getNumFile()*self.salaAttuale.getMaxPerFila()-self.salaAttuale.getPostiOccupati():
                self.costoTotale=self.salaAttuale.getFilmInProiezione().getPrezzo()*self.numBiglietti
                print "Il costo totale dei biglietti e' pari a: "+str(self.costoTotale)+" euro\n"
                self.salaAttuale.setPostiOccupati(self.salaAttuale.getPostiOccupati()+self.numBiglietti)
                self.salaAttuale.setIncasso(self.salaAttuale.getIncasso()+self.costoTotale)
            else:
                print "Non sono disponibili posti sufficienti per il film scelto."

    def stampaReport(self):
        print "\nStatistiche vendita e posti disponibili aggiornati nel multisala Marconi:\n"
        for film in self.saleCinema:
            time.sleep(1)
            print "Titolo: "+film.getFilmInProiezione().getTitolo()
            print "Posti disponibili: "+str(film.getNumFile()*film.getMaxPerFila()-film.getPostiOccupati())+" su "+str(film.getNumFile()*film.getMaxPerFila())+" posti totali."
            print "Incasso: "+str(film.getIncasso())
            print
            
        

        
        
    
