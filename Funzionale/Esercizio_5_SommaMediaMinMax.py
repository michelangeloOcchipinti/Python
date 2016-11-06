def SommaMediaMinMax(num):
    num=1
    minn=0
    maxx=0
    somma=0
    media=0
    cont=0
    while num!=0:
        num=0
        num= input("Inserire una serie di numeri chiusa da uno zero: ")
        somma=somma+num
        cont=cont+1
        media= float (somma)/cont
        if num != 0:
                if maxx==0:
                    maxx=num
                if minn==0:
                    minn=num
                else:
                    if num<=minn:
                        minn=num
                    else:
                        if num>=maxx:
                           maxx=num
    return minn,maxx,somma,media
               
num=input
print SommaMediaMinMax(num)



            

