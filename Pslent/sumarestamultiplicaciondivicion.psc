Algoritmo SumaRestaMultiplicacionDivision
	
	Definir num1, num2 Como Real
	
	Escribir  " Ingrese el primer numero "
	Leer num1
	
	Escribir " Ingrese el segundio numero "
	leer num2
	
	Escribir  "suma: ", num1 + num2
	Escribir "resta: ", num1 - num2
	Escribir "multiplicacion ", num1 * num2
	
	Si num2 <> 0 Entonces
		Escribir  "division: ", num1 / num2
	SiNo
		Escribir  " No se puede dividir entre cero."
	FinSi
FinProceso

