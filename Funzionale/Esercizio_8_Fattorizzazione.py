num=input ("Inserisci un numero: ")
resto=0
div=2
acc=0
print 1
while num>1:
    resto=num%div
    if resto==0:
        acc=num/div
        resto=acc%div
        num=acc
        print div
    else:
        div=div+1
        resto=acc%div
        acc=acc/div

