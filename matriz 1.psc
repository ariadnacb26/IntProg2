Algoritmo Ejercicio1
	definir nombre, apellido, nombre_completo Como caracter 
	definir edad, edad_dias Como entero
	definir peso, peso_kg Como real 
	
	Escribir "Ingresa los siguientes datos"
	Escribir "Nombre"
	Leer Nombre
	Escribir "Apellido"
	Leer Apellido
	Escribir "Edad"
	Leer Edad
	Escribir "Peso"
	Leer peso
	
	nombre_completo = Concatenar(apellido, " ")
	nombre_completo = Concatenar(nombre_completo, nombre)
	edad_dias = dias * 365
	peso_kg = peso / 2.204
	
	Escribir "Nombre completo ", nombre_completo
	Escribir "Edad en dias ", edad_dias
	Escribir "Peso en kG " , peso_kg
	
FinAlgoritmo
