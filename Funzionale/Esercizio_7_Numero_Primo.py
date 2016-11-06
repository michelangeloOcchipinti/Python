def isPrime(n):
    cont=1
    resto=1
    if n==1:
        n=0
    while resto!=0:
        resto=0
        cont=cont+1
        resto=n%cont
    if cont==n:
            resto=1
    else:
            resto=0
    return bool (resto)
    

n= input ("Inserisci un numero intero: ")
print ("Il risultato e': "),isPrime (n)


