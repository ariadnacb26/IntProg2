//conversion de corobas a dolares
Algoritmo cordobasdolares
	Definir cordobas como real 
	Definir dolares como real 
	Definir tipo_cambio como real 
	
	Escribir "Ingrese la cantidad en cordobas"
	Leer cordobas
	Escribir "Ingrese el tipo de cambio"
	Leer tipo_cambio 
	
	dolares <- cordobas / tipo_cambio 
	Escribir "La cantidad en dolares es: ", dolares 
	
FinAlgoritmo
