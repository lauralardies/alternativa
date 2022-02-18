from curses.ascii import BEL
from tkinter.tix import REAL


Algoritmo: Porcentaje Descuento:
#Queremos crear un algoritmo para el porcentaje de descuento en la compra de microprocesadores que cumpla las siguientes cracterísticas:
    #Si la compra de microprocesadores es de entre 10000 y 20000 unidades, este es de un 10%
    #Si la compra es de entre 20001 y 40000 unidades, es de un 15%
    #Si la compra es superior a 40000 unidades, este s de un 20 %
#Además si el cliente es COMMAQ el descuento se reduce un 2%, mientras que si es BEL este aumenta un 1%
#función:
PORCENT_Descuento (nunmic: REAl, cliente:STRING, ): PORCENTAJE
    precondición:
        nunmic > 0
        cliente == COMMAQ or cliente == BEL
    si 
        nunmic < 10000
    entonces
        nunmic < 10000 => No aplica descuento
        resultado = 0%
    si no si 
        nunmic <= 20000 
    entonces
        10000 < nunmic <= 20000 => Aplica descuento 10%
        resultado = 10%
    si no si 
        nunmic <= 40000
    entonces
        20000 < nunmic <= 40000 => Aplica descuento 15%
         resultado = 15%
    si 
        nunmic > 40000
    entonces
        nunmic > 40000 => Aplica descuento 20%
        resultado = 20%
    si 
        cliente == COMMAQ
    entonces
        cliente == COMMAQ => Disminución del descuento
        resultado = -2%
    si 
        cliente == BEL
    entonces
        cliente == BEL => Aplica descuento 1 %
        resultado = 1%
    Postcondion
    numic < 10000
    1000<nunmic<= 20000
    1
    
