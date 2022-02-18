
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
