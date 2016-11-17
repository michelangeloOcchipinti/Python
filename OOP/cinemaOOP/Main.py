import SalaCinema
import Film
import Cinema

film1=Film.Film('Matrix',6.99)
film2=Film.Film('Senorita',9.99)
film3=Film.Film('Leon',3.99)
sala1=SalaCinema.SalaCinema(10,20,film1)
sala2=SalaCinema.SalaCinema(20,15,film2)
sala3=SalaCinema.SalaCinema(30,10,film3)

saleCinema=[sala1,sala2,sala3]

cinema=Cinema.Cinema(saleCinema)

postiSala1=sala1.getNumFile()*sala1.getMaxPerFila()
postiSala2=sala2.getNumFile()*sala2.getMaxPerFila()
postiSala3=sala3.getNumFile()*sala3.getMaxPerFila()

while sala1.getPostiOccupati()<postiSala1 or sala2.getPostiOccupati()<postiSala2 or sala3.getPostiOccupati()<postiSala3:
    
    salaAttuale=cinema.ricercaTitolo()
    cinema.venditaBiglietti(salaAttuale)
    cinema.stampaReport()



