#Importo i moduli di cui avro' bisogno in seguito
import Rana
import random
import time

#Creo la classe Corsa
class Corsa:
     #Inizializzo gli attirbuti privati
    def __init__(self,distPercorso,maxRaneIscritte):
        self.distPercorso=distPercorso
        self.vincitore=""
        self.maxRaneIscritte=maxRaneIscritte
        self.raneIscritte=[]
        self.salto=0
    #Creo i metodi osservatori e modificatori    
    def setDistPercorso(self,distPercorso):
        self.distPercorso=distPercorso
        
    def getDistPercorso(self):
        return self.distPercorso
    
    def setVincitore(self,rana):
        self.vincitore=rana
        
    def getVincitore(self):
        return self.vincitore
    
    def getMaxRaneIscritte(self):
        return self.maxRaneIscritte
    
    def getRaneIscritte(self):
        return self.raneIscritte
    #Creo il metodo che mi permettera' di gestire l'iscrizione delle rane alla gara
    def iscrizioneRane(self):
        i=0
        print "E' arrivato il momento dell'iscrizione, inserisci il nome e di seguito il peso della rana che intendi iscrivere:"
        #Creo il ciclo iterativo per l'iscrizione delle rane da input utente che continuera' finche' il 
        #valore della sentinella avra' raggiunto il valore massimo del numero di rane che e' possibile iscrivere impostato nella variabile maxRaneIscritte
        while i<self.maxRaneIscritte:
            print
            print "Inserisci il nome della rana:"
            nome=raw_input()
            print "Inserisci il peso della rana:"
            peso=input()
            #Creo dinamicamente attraverso una lista gli oggetti di tipo Rana con i relativi valori nome e peso
            self.raneIscritte.append(Rana.Rana(nome,peso))
            print
            print "Ancora "+str(self.maxRaneIscritte-1-i)+" posti liberi!"
            print
            i+=1
    #Creo il metodo che gestira' i salti con valore casuale che simuleranno ogni giro di gara        
    def saltoGara(self,giro):
        i=0
        #Creo il ciclo iterativo che assegnera' un valore casuale al salto della rana e lo salvera' nell'attributo della singola istanza sommandolo al valore gia' inserito nell'attributo
        while i<len(self.raneIscritte):
            self.salto=random.random()
            #Assegno il valore della variabile salto alla variabile saltoMax dell'oggetto Rana solamente se questo e' maggiore di quello presente.
            if self.salto>self.raneIscritte[i].getSaltoMax():
                self.raneIscritte[i].setSaltoMax(self.salto)
            self.raneIscritte[i].setDistPercorsa(self.raneIscritte[i].getDistPercorsa()+self.salto)
            #Richiamo il metodo della classe Rana per calcolare la penale nel caso il peso sia compreso tra 0 e 200gr oppure tra 201gr e 500gr. Se superiore a 501gr non ci sara' penale
            self.raneIscritte[i].calcolaPenale(self.salto)
            #Aggiungo una selezione per fermare l'iterazione nel caso un concorrente raggiunga per primo la distanza del percorso e cosi' sara' decretato vincitore e gli altri concorrenti non salteranno
            if self.raneIscritte[i].getDistPercorsa()>=self.distPercorso:
                i=len(self.raneIscritte)
            i+=1
        #Ordino in ordine decrescente per distanza percorsa (attributo distPercorsa) totale la lista contenente gli oggetti di tipo Rana.
        self.raneIscritte.sort(key=lambda Rana: Rana.distPercorsa, reverse=True)
        print
        print "La classifica aggiornata al giro "+str(giro)+" e' la seguente: "
        print
        #Assegno un delay al prossimo passaggio in modo da rallentare temporalmente il flusso del metodo 
        time.sleep(1.5)
        #Creo un ciclo iterativo che stampa a video la classifica attuale
        for rana in self.raneIscritte:
            print "1) "+rana.getNome()+" con "+str(round(rana.getDistPercorsa(),2))+" metri percorsi!"
            
            
        
            
        
