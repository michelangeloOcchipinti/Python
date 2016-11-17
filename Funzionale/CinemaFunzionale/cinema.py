#Creare il programma in Python funzionale che simuli la situazione esposta in seguito (completo di FlowChart ) 
#Si vuole realizzare un software che gestisca tre sale cinematografiche.
#La SalaCinema ha il seguente insieme di attributi minimali: film (nome del film proiettato), prezzoFilm (prezzo di un singolo biglietto), numero di file (numero di file degli spettatori), maxPerFila (numero massimo di spettatori per fila), posti Occupati (nr di biglietti già venduti per la sala), incasso.
#Il software gestirà l'accesso alle sale tramite vendita di biglietti.L'operatore in cassa dovrà richiedere il titolo del film, che il cliente vuole vedere, e procedere alla vendita dei biglietti (senza che il biglietto sia assegnato ad un posto preciso); quindi all’aggiornamento della situazione prima del cliente successivo.
#In ogni momento deve essere possibile stampare un repoert sull'occupazione delle sale (posti liberi e occupati) e incasso effettuato



#Importo la libreria time per le pause inserite all'iunterno del flusso attraverso il metodo sleep()
import time

#Creo la matrice con i cinema al suo interno completi di tutti gli attributi previsti
listaCinema=[["Ti amo",6.99,10,20,0,0],["Ovvio",8.99,20,20,0,0],["Ciao",2.99,15,5,0,0]]

#Creo le variabili dei posti disponibili per sala
postiSala1=listaCinema[0][2]*listaCinema[0][3]
postiSala2=listaCinema[1][2]*listaCinema[1][3]
postiSala3=listaCinema[2][2]*listaCinema[2][3]

#Creo il metodo per la ricerca del titolo all'interno della matrice in modo da trovare e far restituire il giusto indice che identifica il cineman da utilizzare poi anche con gli altri metodi
def ricercaTitolo(film):
    i=0
    indice=0
    while i<len(listaCinema) and film!=listaCinema[i][0]:
        if film==listaCinema[i][0]:
            indice=i
            i=len(listaCinema)
            return indice
        i+=1
    return i

#Creo il metodo per la vendita dei biglietti 
def venditaBiglietti(indice):
    print "Inserire il numero di biglietti da acquistare:\n"
    numBiglietti=input()
    costoBiglietti=listaCinema[indice][1]*numBiglietti
#Creo una selezione che mi restituira', nel caso in cui il numero di biglietti richiesti sia superiore alla disponibilitÃ  di quella specifica sala, un messaggio con i posti effettivamente disponibili e ricomincera' l'iter dall'inizio
    if numBiglietti<=listaCinema[indice][2]*listaCinema[indice][3]-listaCinema[indice][4]:
        print "\nIl costo totale dei biglietti e' pari a: "+str(costoBiglietti)+" euro"
        time.sleep(1.5)
        listaCinema[indice][5]=listaCinema[indice][5]+costoBiglietti
        listaCinema[indice][4]=listaCinema[indice][4]+numBiglietti
    else:
        print "Il numero di posti richiesto non e' disponibile, il numero massimo di posti disponibili ancora e' pari a: "+str(listaCinema[indice][2]*listaCinema[indice][3]-listaCinema[indice][4])
        time.sleep(2)
#Creo il metodo per la stampa del report per i posti occupati e incasso di ogni sala/film 
def stampaReport():
    i=0
    print "Stampa del report posti occupati ed incasso versione 1.2\n"
    while i<len(listaCinema):
        print "Titolo: "+listaCinema[i][0], "\nPosti occupati: "+str(listaCinema[i][4])+" su "+str(listaCinema[i][2]*listaCinema[i][3])+" totali", "\nIncasso: "+str(listaCinema[i][5])
        i+=1
        print
    

#Inizia il programma principale che continuerÃ  l'iterazione finche' ci saranno posti disponibili almeno in una sala. 
while postiSala1>listaCinema[0][4] or postiSala2>listaCinema[1][4] or postiSala3>listaCinema[2][4]:
    print "Benvenuti al nuovo multisala San Marco!\n"
    print "Inserite il titolo del film tra quelli disponibili:"
    i=0
    while i<len(listaCinema):
        print listaCinema[i][0]
        i+=1
    print
    filmRicercato=raw_input()
    
    indice=ricercaTitolo(filmRicercato)
#Creo una selezione nel caso venisse inserito un titolo errato o non presente nella lista dei film programmati.
    if indice>=len(listaCinema):
        print
        print "il film ricercato non e' presente!\n"
    else:
        venditaBiglietti(indice)
        print
        stampaReport()
