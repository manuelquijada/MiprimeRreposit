Algoritmo EjercicioDivicion
	
	Definir num1, num2, division Como Real
	
	Escribir " Ingrese el primer numero "
	Leer num1
	
	Escribir " Ingrese el segundo numero "
	Leer  num2 
	
	si num2 <> 0 Entonces
		division <- num1 / num2
	
		Escribir " La división es: ", division
	SiNo
			Escribir " Error: No se puede dividir entre 0."
			
	FinSi
FinProceso
