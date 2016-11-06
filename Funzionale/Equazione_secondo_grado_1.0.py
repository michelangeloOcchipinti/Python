# -*- coding: cp1252 -*-
import math
def Completa (ax,b,c):
    if ax!=0 and b!=0 and c!=0:
        ax=float(ax)
        b=float(b)
        c=float(c)
        risultatoTotale=[0,1]
        discriminante=b**2-(4*ax*c)
        if discriminante<0:
            return "Equazione impossibile"
        elif discriminante>=0:
            radice=math.sqrt(discriminante)
            if radice == 0:
                risultatoPositivo=float(-(b/2*ax))
                risultatoNegativo=float(-(b/2*ax))
                risultatoTotale[0]=(risultatoPositivo)
                risultatoTotale[1]=(risultatoNegativo)
                return risultatoTotale
            else:
                if radice>0:
                    risultatoPositivo=(-b+radice)/(2*ax)
                    risultatoNegativo=(-b-radice)/(2*ax)
                    risultatoTotale[0]=(risultatoPositivo)
                    risultatoTotale[1]=(risultatoNegativo)
                    return risultatoTotale
          

def Pura (ax,b,c):
    ax=float(ax)
    c=float(c)
    risultatoTotale=[0,1]
    discriminante=-(c/ax)
    if ax and c and b==0:
        if discriminante<0:
            return "Equazione impossibile"
        elif discriminante>0:
            risultatoPositivo= math.sqrt(discriminante)
            risultatoNegativo= -(math.sqrt(discriminante))
            risultatoTotale[0]=(risultatoPositivo)
            risultatoTotale[1]=(risultatoNegativo)
            return risultatoTotale
   
    


def Spuria (ax,b,c):
    risultatoTotale=[0,1]
    if ax and b and c==0:
        ax=float(ax)
        b=float (b)
        risultatoPositivo= -(b/ax)
        risultatoNegativo= 0
        risultatoTotale[0]=risultatoPositivo
        risultatoTotale[1]=risultatoNegativo
        return risultatoTotale
    

def Monomia(ax,b,c):
    if b==0 and c==0:
        risultato=0
        return risultato
  

def Risultato(completa,pura,spuria,monomia):
    if completa:
        risultato="Equazione di secondo grado completa con risultato rispettivamente per le due x pari a: ", completa
    if pura:
        risultato="Equazione di secondo grado incompleta pura con risultato rispettivamente per le due x pari a: ",pura
    if spuria:
        risultato="Equazione di secondo grado incompleta spuria con risultato rispettivamente per le due x pari a: ",spuria
    if monomia:
        risultato="Equazione di secondo grado incompleta monomia con risultato rispettivamente per le due x pari a: ",monomia
    return risultato
    

ax=input ("Inserisci il valore di ax^2: ")
bx=input ("Inserisci il valore di bx: ")
c=input ("Inserisci il valore di c: ")
completa=Completa (ax,bx,c)
pura=Pura (ax,bx,c)
spuria=Spuria(ax,bx,c)
monomia=Monomia (ax,bx,c)
print Risultato (completa,pura,spuria,monomia)
