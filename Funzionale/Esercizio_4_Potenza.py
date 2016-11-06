def Potenza (n,k):
    acc = 1
    cont = 0
    if n!=0 and k>=0:
            while cont != k:
                acc=acc*n
                cont = cont+1
            return acc

    else:
            print ("I valori inseriti non sono corretti")

n = input ("Inserisci il numero da elevare a potenza: ")
k = input ("Inserisci il numero a cui elevare a potenza: ")

print ("Il risultato di "),n,(" elevato alla "),k,("e' uguale a "),Potenza (n,k)
