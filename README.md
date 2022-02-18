# alternativa

La dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/alternativa)
https://github.com/lauralardies/alternativa

Esta tarea consiste en resolver los enunciados aportados en el campus virtual (son 8 ejercicios en total). Para ello, desarrollamos un pseudocódigo de un algoritmo, el cual nos permite crear un código para llegar a la solución del problema. Además, hacemos un diagrama de clases que complementa al ejercicio. 

Ejercicio 1: Trata de crear un algoritmo que sea capaz de calcular el día de la semana sucesivo a otro. Por ejemplo, si me dicen que estamos a jueves, a través de este algoritmo tenemos que poder calcular que el día siguiente al jueves es viernes a través de un programa. 

Ejercicio2: Creación de un algoritmo, dados dos números, que clasifique su producto y suma.

Eejercicio 3:  En este ejercicio se nos planteaba la siguiente situación : "Un comerciante hace un descuento del 5 % en todas las compras con un importe comprendido entre 100 y 500 €, y del 8 % en los importes superiores." Y se nos pedía escribir el algoritmo de cálculo del importe del descuento en una compra dada.

Ejercicio 4: para este ejercicio teníamos que definir el algoritmo con el que un profesor podría  calcular la media de 4 notas de un alumno para hallar la nota de evaluación correspondiente

Ejercicio 5: En este ejercicio sólo conociendo el número de niños de una familia, somos capaces de calcular qué porcentaje de descuento tenemos que aplicar a las entrada para el Parque Warner Madrid.

Ejercicio 6: En este ejercicio se nos planteaba que una empresa de microprocesadores haría descuentos de la siguiente forma:

El descuento concedido es de un 10 % en compras de entre 10 000 y 20 000 componentes.

El descuento concedidio es de un 15 % en compras de entre 20 001 y 40 000 componentes. 

El descuento concedidio es de un 20 % en compras superiores a  40 000 componentes.

Además, si el cliente es COMMAQ, el descuento se reduce un 2 %, mientras que si es BEL disfruta de un descuento mejorado en un 1 %.

Dada esta información se epide establecer el algoritmo de cálculo del porcentaje de descuento.

Ejercicio 8: en este ejercicio debíamos escribir el algoritmo de cálculo de la prima anual que se concederá a cada conductor teniendo en cuenta lo siguiente: 

En principio, el conductor recibirá la prima anual completa si no ha tenido accidentes con una responsabilidad superior o igual al 20 % durante el año que termina. Si la responsabilidad es superior al 20 %, la empresa considera al conductor responsable del accidente. Si el conductor ha sido responsable de un accidente, solo recibe la mitad de la prima. Con dos accidentes, solo recibe un tercio. Con tres accidentes, la prima se reduce a un cuarto. Si supera los tres accidentes, la prima se anula.

Esta prima es la suma de una prima de distancia y de una prima de antigüedad.

La prima de distancia aumenta un céntimo por kilómetro recorrido durante el año, con un máximo de 400 €.

La prima de antigüedad solo se paga una vez transcurridos cuatro años de antigüedad y es de 200 €. Luego aumenta 20,00 € por año adicional.


Ejercicio 7: Se trata  de crear un algoritmo para saber el coste total de un viaje escolar y el coste individual, dado los alumnos y los dias que se van de viaje.

Los respectivos códigos de nuestros ejercicios son los siguientes: 

#Ejercicio1
```# Sucesor de un DÍA de la semana
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


#Ejercicio2

#Colocar dos números respecto a su suma y a su producto
#Dados dos números cualesquiera, pero comparables. Se pide clasificar los cuatros números
# que forman con su suma y su producto. Así enunciado, el problema se convierte en:
# clasificar cuatro números cualesquiera. Desde luego, los cuatro números no son 
# cualesquiera porque dos de ellos determinan el valor de los otros dos, pero clasificar 
# cuatro números cualesquiera permite sin lugar a dudas clasificar dos números, su suma y su producto.
# Hemos resuelto el problema para tres números y hemos obtenido el algoritmo clasificar3:
Algoritmo 1: Clasificar tres datos comparables

Algoritmo clasificar3    
    # Clasifica `a', `b' y `c' en orden creciente.
Entrada    
    a, b, c : T → COMPARABLE
precondición    
    ninguna
realización    
    si a > b entonces intercambiar(a, b) fin si # a ≤ b ; situar `c'    
    si b > c entonces intercambiar(b, c) fin si # a ≤ c ; b ≤ c    
    si a > b entonces intercambiar(a, b) fin si # a ≤ b ≤ c
postcondición    
    a ≤ b ≤ c
fin clasificar3
Sea entonces clasificar4 el algoritmo que resuelve el problema para cuatro números cualesquiera. Para responder con exactitud a la cuestión planteada, escribiremos:
    ...
    variable    
        c, d : (T, +, x) → COMPARABLE
    realización    
        ...    
        c ← a + b ; d ← a x b   
        clasificar4(a, b, c, d)    
        # a ≤ b ≤ c ≤ d
    ...
La declaración de las variables c y d indica que son de tipo T que deriva de COMPARABLE y, además, están definidas en T dos operaciones designadas por los operadores '+' y 'x'.
Entonces queremos obtener un resultado tal que a ≤ b ≤ c ≤ d. Analizamos la realización de clasificar4.
Cuando los tres números a, b y c están clasificados llamando a los servicios de clasificar3, tenemos un estado nuevo que es:
# a ≤ b ≤ c ; situar `d'
Cuando d y a no están en orden, las intercambiamos:
si    
    d < a
    entonces    
        intercambiar(a, d)    # a ≤ d ; b ≤ c    
        clasificar3(b, c, d) # a ≤ b ≤ c ≤ d
        si no
        ...
Si están en orden, todavía hay que clasificar b, c y d:
    ...
    si no    
        # a ≤ d ; b ≤ c    
        clasificar3(b, c , d) # a ≤ b ≤ c ≤ d
    fin si
    # a ≤ b ≤ c ≤ d
Observamos que en los dos estados, hay que llamar a clasificar3 para poner b, c y d en orden. Esta operación es independiente del estado descrito por la alternativa y podemos sacar la llamada a clasificar3(b, c, d) de las alternativas. Tenemos:
    # a ≤ b ≤ c ; situar `d'
    si    
        d < a
    entonces    
        # a > d ; b ≤ c    
    intercambiar(a, d)    
        # a ≤ d ; b ≤ c
    fin si
    # a ≤ d ; b ≤ c
    clasificar3(b, c , d)
    # a ≤ b ≤ c ≤ d
    
    
    #Ejercicio3
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
        precio > 500 = > Aplica descuento (8%)
        resultado precio * 8/100
    fin descuento
    
    
    
    #Ejercicio4
    Algoritmo NotaFinalAlumno
    VARIABLES
    Promedio = prom
    Primer examen = parc1
    Segundo examen = parc2
    Tercer examen = parc3
    Cuarto examen = parc4
    Nota final = NF
    Definir prom, parc1, parc2, parc3, parc4, NF Como Real

    ENTRADA
    Escribir "Ingrese la nota del examen: "
    Leer parc1
    Escribir "Ingrese la segunda nota del examen: "
    Leer parc2
    Escribir "Ingrese la tercera nota del examen: "
    Leer parc3
    Escribir "Ingrese la cuarta nota del examen: "
    Leer parc4

    PROCESOS
    Prom <- (parc1+parc2+parc3+parc4)/4

    SALIDA
    Si NF>15 Escribir "Alumno con talento"
    Si 15>=NF>=12 Escribir "Alumno con capacidad"
    Si NF<12 Escribir "Debe reorientarse"

Fin NotaFinalAlgoritmo



#Ejercicio5
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



#Ejercicio6
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
    postcondion
        numic < 10000 and cliente ==BEL => Resultado = 1%
        numic < 10000 and cliente == COMMAQ => Resultado = -2%
        10000<nunmic<= 20000 and cliente == BEL => Resultado = 11%
        10000<nunmic<= 20000 and cliente == COMMAQ => Resultado = 8%
        20000< nunmic <= 40000 and cliente == BEL => Resultado = 16%
        20000< nunmic <= 40000 and cliente == COMMAQ => Resultado = 13%
        40000< nunmic  and cliente == BEL => Resultado = 21%
        40000< nunmic and cliente == COMMAQ => Resultado = 18%
    fin PORCENT_Descuento




#Ejercicio7
# VIAJE ESCOLAR
# El coste del viaje escolar depende del numero de alumnos que vayan. El coste total es la suma
# del coste del trayecto, de la comida y del alojamiento. Si van mas de 25 personas el trayecto cuesta 61 €
# sino 67,30€. En cuanto al dinero de la comida si van mas de 35 personas son 3,50 € sino 4 €. Y por ultimo,
# el alojamiento, si es inferior a 30 personas son 4,75 € por dia y persona, si son entre 31 y 35 personas
# cuesta 4€ y si son mas de 35 seran 3,50 €.

# Nuestro algoritmo calculará el precio de coste por alumno y el coste global del viaje.

Algoritimo viaje

Entrada
    numero_alumnos: ENTERO # Numero de personas que acuden al viaje
    dias: ENTERO # Numero de dias que dura el viaje

Resultado_persona: ENTERO # Coste por alumno y coste global

REALIZACION

    Si n < 25
        coste_trayecto= 67.30
        coste_comida=4
        coste_alojamiento= 4.75
        Resultado_persona  = coste_trayecto + coste_comida + coste_alojamiento * dias
        Resultado_total = Resultado_persona * numero_alumnos
    Si 25 < n < 30
        Resultado_persona = 61 + 4 + 4,75 * dias
        Resultado_total = Resultado_persona * numero_alumnos

    Si 31 < n < 35
        Resultado_persona = 61 + 4 + 4 * dias
        Resultado_total = Resultado_persona * numero_alumnos

    Si n > 35
        Resultado_persona = 61 + 3,50 + 3,50 * dias
        Resultado_total = Resultado_persona * numero_alumnos

fin viaje




#Ejercicio 8
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
    
