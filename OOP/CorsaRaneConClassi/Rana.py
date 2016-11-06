#Creo la classe Rana
class Rana:
    #Inizializzo gli attributi privati
    def __init__(self,nome,peso):
        self.nome=nome
        self.peso=peso
        self.distPercorsa=0
        self.saltoMax=0
        
    
    #Creo i metodi osservatori e modificatori    
    def setNome(self,nome):
        self.nome=nome
        
    def getNome(self):
        return self.nome
    
    def setPeso(self,peso):
        self.peso=peso
        
    def getPeso(self):
        return self.peso
    
    def setDistPercorsa(self,distPercorsa):
        self.distPercorsa=distPercorsa
        
    def getDistPercorsa(self):
        return self.distPercorsa
    
    def setSaltoMax(self,saltoMax):
        self.saltoMax=saltoMax
        
    def getSaltoMax(self):
        return self.saltoMax
    
    #Aggiungo il metodo per calcolare la penale nel caso il peso sia compreso tra 0 e 200gr oppure tra 201gr e 500gr. Se superiore a 501gr non ci sara' penale
    def calcolaPenale(self,salto):
        if self.peso>=0 and self.peso<=200:
            self.distPercorsa=self.distPercorsa-salto*10/100
        elif self.peso>200 and self.peso<=500:
            self.distPercorsa=self.distPercorsa-salto*5/100
      
