#!/usr/local/bin/python 
# -*- coding: utf-8 -*-

#Classe che crea le sale del cinema come oggetti
class SalaCinema:
    
    def __init__(self,numFile,maxPerFila,film):
        self.numFile=numFile
        self.maxPerFila=maxPerFila
        self.postiOccupati=0
        self.incasso=0
        self.filmInProiezione=film

    def getNumFile(self):
        return self.numFile

    def getMaxPerFila(self):
        return self.maxPerFila

    def getIncasso(self):
        return self.incasso

    def setIncasso(self, incasso):
        self.incasso=incasso

    def getPostiOccupati(self):
        return self.postiOccupati

    def setPostiOccupati(self, postiOccupati):
        self.postiOccupati=postiOccupati

    def getFilmInProiezione(self):
        return self.filmInProiezione

    def setFilmInProiezione(film):
        self.filmInProiezione=film
        

    
