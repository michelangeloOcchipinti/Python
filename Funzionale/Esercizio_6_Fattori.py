n = input ("Inserisci il numero di cui cercare i fattori: ")
k = 0
quadr = 0
while quadr<n or r!=0:
    k = k+1
    quadr = k*k
    r = n%k
    div = n/k
    print ("I fattori sono: "),k,(" e "), div

