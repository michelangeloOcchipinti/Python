def RadiceIntera (num):

    a = 1
    k = 0
    while k<num:
        a = a+1
        k = a*a
        if num==k:
            acc=a  
        else:
            acc = a-1
    return acc

num = input ("Inserisci il numero di cui calcolare la radice quadrata intera: ")
print ("La radice intera di "), num, ("e' uguale a "),RadiceIntera(num)
