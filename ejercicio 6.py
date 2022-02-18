from curses.ascii import BEL
from tkinter.tix import REAL


Algoritmo: Descuento:
#Queremos crear un algoritmo para el descuento en la compra de microprocesadores que cumpla las siguientes cracterísticas:
    #Si la compra de microprocesadores es de entre 10000 y 20000 unidades, este es de un 10%
    #Si la compra es de entre 20001 y 40000 unidades, es de un 15%
    #Si la compra es superior a 40000 unidades, este s de un 20 %
#Además si el cliente es COMMAQ el descuento se reduce un 2%, mientras que si es BEL este aumenta un 1%
#función:
Descuento (nunmic: REAl, cliente:STRING, ): REAL
    precondición:
        nunmic > 0
        cliente == COMMAQ or cliente == BEL
    si 
        nunmic < 10000
    entonces
        nunmic < 10000 => No aplica descuento
    