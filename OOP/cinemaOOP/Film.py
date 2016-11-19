#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#Classe che crea i film da utilizzare nelle sale come oggetti
class Film:

    def __init__(self, titolo, prezzo):
        self.titolo=titolo
        self.prezzo=prezzo

    def getTitolo(self):
        return self.titolo

    def setTitolo(self, titolo):
        self.titolo=titolo

    def getPrezzo(self):
        return self.prezzo

    def setPrezzo(self, prezzo):
        self.prezzo=prezzo
