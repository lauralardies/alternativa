from signal import siginterrupt
from tkinter.tix import REAL


Algoritmo: Descuento:
#Para este ejercicio tenemos que crear un algoritmo para calcular el descuento de una compra
#teniendo en cuenta que se aplicará un descuento de un 5 % a compras valoradas entre 100 y 500 euros y de un 8% para compras valoradas en más de 500 euros
#función:
Descuento (precio, REAl): REAL
    precondicion:
        precio > 0
    si 
        precio < 100
    entonces
        precio < 100 => No aplica descuento
        resultado = 0
    si no si
        precio <= 500
    entonces 
        100 <= precio <= 500 => Aplica descuento (5%)
        resultado = precio * 5/100
    si no si 
        precio > 500
    entonces 
        precio > 500