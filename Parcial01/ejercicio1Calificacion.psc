Algoritmo Ejercicio1Calificacion
	Definir nota Como Entero
	
	Escribir  " Ingrese la nota del estudiante (0 a 10):"
	Leer nota
	
	Si nota >= 6
		Escribir "aprobado"
	SiNo
		Si nota <= 4 Entonces
			Escribir "reprobado"
		SiNo
			Si nota = 5 Entonces
				Escribir "recuperacion"
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
