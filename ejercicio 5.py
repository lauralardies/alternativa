# ADIF
# Descuento de la Warner. Este descuento es del 10 % para 2 niños, 15 % para 3 niños y 18 % para 4 niños. A partir de 5 niños, 
# el descuento es del 18 %, pero aumenta un 1 % por cada niño por encima de 4.

# Nuestro algoritmo calcula el porcentaje de descuento para cualquier familia, inependientemente del número de niños que tenga.

Algoritmo descuento

Entrada
    n : ENTERO # Número de niños en la familia

Resultado : ENTERO # Porcentaje de descuento que se aplica a esa familia

Precondicion
    # Vemos en en enunciado del ejercicio que las familias que sólo tienen un niño no cuentan con descuento
    n > 1 

Realizacion
    Si n = 2
        Resultado <- 10 %
    Si n = 3
        Resultado <- 15 %
    Si n = 4
        Resultado <- 18 %
    Si n > 4
        Resultado <- (14 + n) %
        
        Si Resultado > 100 %
            Resultado <- 100 % 

fin descuento