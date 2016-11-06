def MCD(a,b):
    while b:
        a,b=b,a%b
    return a

a = input("Inserisci il primo numero pr calcolare il massimo comun divisore ")
b = input("Inserisci il secondo numero pr calcolare il massimo comun divisore ")

print MCD (a,b)
