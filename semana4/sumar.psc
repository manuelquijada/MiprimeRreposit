Algoritmo sumar
	// solicitar al usuario
	// que ingrese dos números enteros
	// y mostrar la suma de ambos.
	Definir NumeroEntrada1, NumeroEntrada2, numerototal Como Entero
	Escribir 'ingrese un numero para sumar '
	Leer NumeroEntrada1
	Escribir 'ingrese un numero para sumar '
	Leer NumeroEntrada2
	// las condiciones logicas son las que nos van a decir si es verdadero o falso
	// and
	// or
	// not
	total <- NumeroEntrada1+NumeroEntrada2
	Si NumeroEntrada1<0 Entonces
		total <- NumeroEntrada1+NumeroEntrada2
	FinSi
	Escribir ' El total de la suma 2 ', total
FinAlgoritmo
