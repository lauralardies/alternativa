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
