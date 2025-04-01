Algoritmo Ejercicio3
	definir monto_prestamo Como Entero
	definir tasa_interes_anual Como Real
	definir tiempo_prestamo como entero 
	definir monto_total Como Real  
	
	Escribir "Rellene los siguientes datos"
	Escribir "Cual es el monto del prestamo"
	Leer monto_prestamo
	
	
	tasa_interes_anual = 0.03
	tiempo_prestamo = 5
	
	M = P * (1 + r)^t
	monto_total = monto_prestamo * (1 + tasa_interes_anual) ^ tiempo_prestamo 
	
	Escribir "El monto total a pagar en 5 años es de: ", monto_total
	
	
	
	
	
FinAlgoritmo
