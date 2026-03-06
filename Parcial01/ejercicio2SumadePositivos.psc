Algoritmo Ejercicio2SumaPositivos
	
	Definir numero, suma Como Entero
	
	suma <- 0
	
	Repetir
		Escribir "ingrese numero "
		 Leer numero 
		
		Si numero >= 0 Entonces
			suma <- suma + numero
		FinSi
	Hasta Que numero < 0
	
	Escribir "la suma de los numero positivos es: ", suma
	
	
	
FinAlgoritmo
