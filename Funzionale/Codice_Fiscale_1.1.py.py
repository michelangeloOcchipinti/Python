# -*- coding: cp1252 -*-
import random
import string

# ***VERSIONE 1.1***

# Miglioramenti:

# - migliorata l'efficienza e la leggibilità dell'algoritmo inserendo l'istruzione ciclica "IF x IN n" al posto delle istruzioni "If" a cascata per la costruzione del nome e del cognome.

# Bugfix:

# - Rimosso un bug che non permetteva al ciclo random di estrarre il giorno corretto in base al mese.
# - Rimosso un bug che non permetteva di avere il codice di controllo corretto.

'''ESERCIZIO
Si vuole realizzare un programma in grado di generare liste di anagrafiche realizzate in modo casuale per verificare il
funzionamento di un sistema gestionale in via di sviluppo. Il programma deve, a partire da dati generati casualmente,
generare il seguente output:
Cognome;Nome;Data di nascita;Comune o Stato estero di nascita;CF;
Carli;Bruno;29/10/1945;Venezia;CRLBRN45L29L736E;
I nomi e cognomi della lista in output saranno generati estraendo un valore plausibile da una lista di stringhe
opportunamente inizializzata.
cognomi = [“Carli”,”Verdi”,”Bruni”,”Rossi”, ... ]
nomi = [“Angelo”,”Antonio”,”Luca”,”Marco”, ... ]
Giorno, mese e anno di nascita
saranno generati casualmente secondo i seguenti criteri:
viene generato casualmente il mese di nascita compreso tra 1 e 12, viene generato casualmente l'anno di nascita
compreso tra il 1920 e 2014 viene generato casualmente il giorno tenendo conto della variabilità dei giorni in base al
mese.
Anche il comune di nascita viene generato casualmente da una lista di codici catastali opportunamente inizializzata a partire da un
campione di dati ricavato dal sito: http://www.comuniecitta.it/codici-catastali'''


# Creo un nome casuale da una lista. Inserisco anche alcuni nomi a due lettere per testare l'algoritmo che aggiunge i caratteri supplmentari.  
def Nome():
    Nomi=[["Giancarlo","M"],["Moreno","M"],["Giancarlo","F"],["Maria","F"],["Alessandro","M"],["Claudia","F"],["Le","F"],["Giosue","M"],["Amentore","M"],["Ernesta","F"],["Paolo","M"],["Rica","F"],["Ernesto","M"],["Massimo","M"],["Ivan","M"]]
    nome=random.choice(Nomi)
    return nome

# Creo un cognome casuale da una lista. Inserisco anche alcuni nomi a due lettere e ad una lettera per testare l'algoritmo che aggiunge i caratteri supplmentari.
def Cognome():
    Cognomi=["El","Dela","Rossi","Faranga","De loreto","O","Giosetti","Occhipinti","Palumbo","Diseo","Zagarella","Bipone","Azelao","Sara","Dimanica","Gorletti","Amendola"]
    cognome=random.choice(Cognomi)
    return cognome

# Creo un anno di nascita casuale da una lista con range 1920:2014
def annoNascita():
    annoNascita=random.randint(1920,2014)
    return annoNascita

# Creo un mese di nascita casuale da una lista con range 1:12
def meseNascita():
    meseNascita=random.randint(1,12)
    if 0<meseNascita<=9:
        meseNascita="0" + str(meseNascita)
    return str(meseNascita)    

# Creo un giorno di nascita casuale rispettando i limiti imposti dal calendario gregoriano
def giornoNascita(meseNascita):
    meseNascita=str(meseNascita)
    if meseNascita == "01" or "03" or "05" or "07" or "08" or "10" or "12":
        giornoNascita=random.randint(1,31)
    elif meseNascita == "02":
        giornoNascita=random.randint(1,28)
    elif meseNascita == "04" or "06" or "09" or "11":
        giornoNascita=random.randint(1,30)
    if 0<giornoNascita<=9:
        giornoNascita="0" + str(giornoNascita)
    return str(giornoNascita)

# Creo un comune di nascita o uno Stato estero di nascita (con collegato il codice catastale in una matrice) casuale da una matrice
def comuneNascita():
    comune=[["Venezia","L736"],["Vicenza","L840"],["Padova","G224"],["Treviso","L407"],["Belluno","A757"],["Verona","L781"],["Rovigo","H620"],["Austria","Z102"],["Danimarca","Z107"],["Francia","Z110"],["Germania","Z112"],["Gran Bretagna","Z114"],["Malta","Z121"]]
    numero=random.randint(0,len(comune)-1)
    comuneNascita=comune[numero]
    return comuneNascita

# Creo il codice a tre caratteri dal cognome per iniziare a comporre il codice fiscale
def cognomeCodice(cognome):
    cons="BCDFGHJKLMNPQRSTVWZYX"
    voc="AEIOU"
    consonanti=""
    indice=len(cognome)-1
    cognome=str.upper(cognome)
    while indice>=0:
        if cognome[indice] in cons:
           
          consonanti=cognome[indice] + consonanti
                            
        indice=indice-1
    indice=0
    if len(cognome)>=3:
        if len(consonanti)<3:
            while len(consonanti)<3:
                if cognome[indice] in voc:
                        consonanti=consonanti+cognome[indice]    
                indice=indice+1	           
    else:
        indice=0
        if len(cognome)==2:
            if len(consonanti)<2:
                while len(consonanti)<2:
                    if cognome[indice]  in voc :
                        consonanti=consonanti+cognome[indice]
                    indice=indice+1    
                consonanti=consonanti + "X"
        if len(cognome)==1:
                consonanti=cognome+"XX"               
    return consonanti [:3]

# Creo il codice a tre caratteri dal nome per continuare a comporre il codice fiscale
def nomeCodice(nome):
    cons="BCDFGHJKLMNPQRSTVWZYX"
    voc="AEIOU"
    consonanti=""
    indice=len(nome)-1
    nome=str.upper(nome)	
    while indice>=0:
        if nome[indice] in cons:
           
          consonanti=nome[indice] + consonanti
                            
        indice=indice-1
       
    if len(consonanti)>=4:
        consonanti=consonanti[0]+consonanti[2:]
    indice=0    
    if len(nome)>=3:
        if len(consonanti)<3:
            while len(consonanti)<3:
                if nome[indice] in voc:
                        consonanti=consonanti+nome[indice]    
                indice=indice+1	
      
    else:
        indice=0 
        if len(nome)==2:
            if len(consonanti)<2:
                while len(consonanti)<2:
                    if nome[indice] in voc:
                        consonanti=consonanti+nome[indice]    
                    indice=indice+1
            consonanti=consonanti + "X"
        if len(nome)==1:
                consonanti=nome+"XX"              
    return consonanti [:3]

# Creo il codice del mese da una matrice per continuare a comporre il codice fiscale
def meseCodice(mese):
    codiciMese=[["01","A"],["02","B"],["03","C"],["04","D"],["05","E"],["06","H"],["07","L"],["08","M"],["09","P"],["10","R"],["11","S"],["12","T"]]
    indice=0
    while indice<len(codiciMese):
        if mese==codiciMese[indice][0]:
            mese=codiciMese[indice][1]

        indice=indice+1
    return mese

# Creo il codice del giorno da una matrice per continuare a comporre il codice fiscale distinguendo tra uomo e donna (nel caso il sesso sia femminile aggiungo "40" al numero del giorno)
def giornoCodice(giorno,nome):
    if nome[1]=="F":
        giorno=giorno + 40
    else:
        if 0<giorno<=9:
            giorno = "0" + str(giorno)
    return giorno

# Creo il codice di controllo per terminare il codice fiscale
def codiceControllo(codiceFiscale):
    indice=1
    indice2=0
    caratteriPari=""
    caratteriDispari=""
    sommaPari=0
    sommaDispari=0
    codiceControllo=0
    tabelle=[["0",0,1],["1",1,0,],["2",2,5],["3",3,7],["4",4,9],["5",5,13],["6",6,15],["7",7,17],["8",8,19],["9",9,21],["A",0,1,0],["B",1,0,1],["C",2,5],["D",3,7],["E",4,9],["F",5,13],["G",6,15],["H",7,17],["I",8,19],["J",9,21],["K",10,2],["L",11,4],["M",12,18],["N",13,20],["O",14,11],["P",15,3],["Q",16,6],["R",17,8],["S",18,12],["T",19,14],["U",20,16],["V",21,10],["W",22,22],["X",23,25],["Y",24,24],["Z",25,23]]
    while indice2<len(codiceFiscale):
        if indice%2==0:
            caratteriPari=caratteriPari+codiceFiscale[indice2]
        else:
            if indice%2!=0:
                caratteriDispari=caratteriDispari+codiceFiscale[indice2]
        indice2=indice2+1
        indice=indice+1
    indice=0
    while indice<len(caratteriPari):
        indice2=0
        while indice2<len(tabelle):
            if caratteriPari[indice]==tabelle[indice2][0]:
                sommaPari=sommaPari+tabelle[indice2][1]
            indice2=indice2+1
        indice=indice+1
    indice=0
    while indice<len(caratteriDispari):
        indice2=0
        while indice2<len(tabelle):
            if caratteriDispari[indice]==tabelle[indice2][0]:
                sommaDispari=sommaDispari+tabelle[indice2][2]
            indice2=indice2+1
        indice=indice+1
    codiceControllo=(sommaPari+sommaDispari)%26
    indice=10
    while indice<len(tabelle):
        if codiceControllo==tabelle[indice][1]:
            codiceControllo=tabelle[indice][0]
        indice=indice+1    
    return codiceControllo
        
    

# Stampo a video tutte le informazioni   
print "Nome;",
print "Cognome;",
print "Data di nascita;",
print "Comune o Stato estero di nascita;",
print "Codice Fiscale"

n=Nome()
print n[0],";",
c=Cognome()
print c,";",
anno=str(annoNascita())
mese=meseNascita()
giorno=giornoNascita(mese)
print str(giorno)+"/"+ str(mese) + "/" + anno,";",
giornoCode=giornoCodice(int(giorno),n)
comune=comuneNascita()
print comune[0],";",
codiceFiscale= cognomeCodice(c)+ nomeCodice(n[0]) + str(anno[2:4]) + str(meseCodice(mese)) + str(giornoCode) + comune[1]
codControllo=codiceControllo(codiceFiscale)
codiceFiscaleCompleto= cognomeCodice(c)+ nomeCodice(n[0]) + str(anno[2:4]) + str(meseCodice(mese)) + str(giornoCode) + comune[1] + str(codControllo)
print codiceFiscaleCompleto

                                                                    






        
    





   
    
    
    
    
    
   

   
