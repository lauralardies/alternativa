# Sucesor de un DÍA de la semana
# Nuestro algoritmo calcula qué día de la semana va después de un día de la semana ya dado.


Tipo DIA estructura:

j : ENTERO # En esta variable insertamos el número que corresponde al día de la semana del cual queremos averiguar el día sucesor

invariante
    # No podemos salir del rango 0-6 porque sino no corresponde a ningún día de la semana
    0 <= j <= 6

# (lunes, martes, miércoles, jueves, viernes, sábado, domingo)
# (  0  ,   1   ,     2    ,   3   ,    4   ,   5   ,    6   )
# A cada día de la semana se le asigna un número

fin DIA




Algoritmo sucesor(dia : DIA)

Entrada
    dia : ENTERO # Día de la semana (enunciado)

Realizacion
    # Para calcular el resultado final, simplemente añadimos 1 al número correpondiente al día de la semana del enunciado.
    # Así obtenemos el siguiente número que corresponde con el siguiente día de la semana.
    # Nos aseguramos de poner módulo 7 (sólo hay  días a la semana) para que no obtener un resultado fuera del rango 0-6.

    Resultado <- (dia + 1) modulo 7

Poscondicion
    Resultado = resto(dia + 1, 7)

fin sucesor