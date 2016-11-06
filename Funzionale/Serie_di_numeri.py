num = 1
somma = 0
cont = 0
media = 0
maxx = 0
minn = 0
while num:
    minn=num
    maxx=num
    num = 0
    num = input ("Inserisci un numero intero qualsiasi, il ciclo si fermerà con l'inserimento di uno zero: ")
    somma = somma + num
    cont = cont +1
    media = float (somma) / cont
if minn<num:
    minn=minn
else:
    minn=num
if maxx<num:
    maxx=maxx
else:
    maxx=num

    print somma
    print media
    print minn
    print maxx
 


