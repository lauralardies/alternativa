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