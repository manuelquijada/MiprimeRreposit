Algoritmo Ejercicio3_DiaSemana
		
	Definir numero Como Entero
	//elejimos un numero del 1 al 7.
		
		Escribir "Ingrese un numero del 1 al 7:"
		Leer numero
		// definimos los dias de la semana por numero.
		Segun numero Hacer
			1:
				Escribir "Lunes"
			2:
				Escribir "Martes"
			3:
				Escribir "Miercoles"
			4:
				Escribir "Jueves"
			5:
				Escribir "Viernes"
			6:
				Escribir "Sabado"
			7:
				Escribir "Domingo"
				// usamos de otro modo para que si elegimos un numero distinto de uno a 7 ej 8 nos de numero invalido.
			De Otro Modo:
				Escribir "Numero invalido"
		FinSegun
	// finalisamos nuestro Algoritmo .
FinAlgoritmo
