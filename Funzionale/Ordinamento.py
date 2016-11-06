lista=[254,87,98,65,25,8,1,4,56,98,74,12,36,56,98,789,78,45,12,123,5,9,4,2,54,65,35,89,78]
scambio=0
indiceEsterno=0
indiceInterno=0
while indiceEsterno<len(lista)-1:
    indiceInterno=0
    while indiceInterno<len(lista)-1:
        if lista[indiceInterno]>lista[indiceInterno+1]:
            scambio=lista[indiceInterno]
            lista[indiceInterno]=lista[indiceInterno+1]
            lista[indiceInterno+1]=scambio
        indiceInterno=indiceInterno+1
    indiceEsterno=indiceEsterno+1

    print lista

