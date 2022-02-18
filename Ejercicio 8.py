Algoritmo prima_anual

ENTRADA
    accidentes : ENTERO # Número de accidentes
     distancia : ENTERO # Distancia recorrida
   antigüedad : ENTERO # Antigüedad

   Resultado: REAL

variable
    prima_antigüedad : REAL
    prima_distancia : REAL

realización
    si
        accidentes > 3
    entonces
        Resultado ← 0,00
    si no
        # Cálculo de la prima de antigüedad
        si
            antigüedad < 4
        entonces
            prima_antigüedad ← 0,00
        si no
            prima_antigüedad ← 200,00 + 
                                      REAL(antigüedad – 4) x 20,00
        fin si

        # cálculo de la prima de rendimiento
        prima_distancia ← inf(REAL(distancia) x 0,01, REAL(400))

        # Cálculo de la prima anual
        Resultado ← (prima_antigüedad + prima_distancia) /
                   REAL(accidentes + 1)
    fin si

postcondición
...
fin prima_anual