Proceso  RestarHastaPar
	Definir num1, num2, resultado Como Entero
	Definir esPar Como Logico
	
	Escribir "ingrese el primer numero:"
	Leer num1
	
	Escribir "ingrese  el segundo numero:"
	Leer num2
	
	resultado <- num1 - num2
	
	esPar <- Falso
	
	Mientras esPar = Falso Hacer
		Si resultado MOD 2 = 0 Entonces
			
			esPar <- Verdadero
		SiNo
			Escribir "el resultado es impar: ", resultado
			Escribir "Ingrese otro numero para restar:"
			Leer num2
			resultado <- resultado - num2
		FinSi
		
	FinMientras
	
	Escribir  "El resultado final es par: ", resultado
	
FinProceso

