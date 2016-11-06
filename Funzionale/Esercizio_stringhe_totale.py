#Una funzione email che, presi come parametri tre stringhe rappresentanti nome, cognome e
#dominio di email di un utente, restituisca la stringa che rappresenta l'email dell'utente. Tale
#stringa è ottenuta concatenando: il primo carattere del nome, il carattere ".", il cognome, il
#carattere "@", ed il dominio di email.

def email (nome,cognome,dominio_web):
    mail = nome[0] + "." + cognome + "@" + dominio_web
    return mail


#Una funzione homePage che, presi come parametri due stringhe rappresentanti cognome e
#dominio web di un utente, restituisca la stringa che rappresenta la homepage dell'utente.
#Tale stringa è ottenuta concatenando: la stringa "http://", il dominio web, la stringa "/~",
#ed il cognome.


def homePage (cognome, dominio_web):
    prefisso_web="http://"
    tilde= "/~"
    indirizzo_web = prefisso_web + dominio_web + tilde + cognome
    return indirizzo_web


#Una funzione userId che, presi come parametri  due stringhe rappresentanti nome e
#cognome di un utente, restituisca la stringa che rappresenta lo userId dell'utente. Tale
#stringa è ottenuta concatenando: il primo carattere del nome con i primi sette caratteri del
#cognome.


def userId (nome, cognome):
    username=nome[0] + cognome [0:7]
    return username


#Una  funzione password che, presi come parametri due stringhe  rappresentanti  nome  e
#cognome di un utente, restituisca una password generata automaticamente. Tale stringa è
#ottenuta concatenando i primi tre caratteri del cognome e gli ultimi tre del nome.

def password (nome, cognome):
    passw= cognome [0:3] + nome[-3:]
    return passw

nome=raw_input ("Inserisci il nome: ")
cognome=raw_input ("Inserisci il cognome: ")
dominio_web=raw_input ("Inserisci il dominio: ")

print

print "Il tuo indirizzo mail completo e': ", "\t", email (nome, cognome, dominio_web)
print "La tua homepage web sarà: ", "\t\t", homePage (cognome, dominio_web)
print "Il tuo user ID sara': ", "\t\t\t", userId (nome, cognome)
print "La tua password sara': ", "\t\t", password (nome, cognome)
