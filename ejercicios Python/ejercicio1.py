# Definir las variables
nombre = ""
apellido = ""
nombre_completo = ""
edad = 0
edad_dias = 0
peso = 0.0
peso_kg = 0.0

# Solicitar los datos al usuario
print("Ingresa los siguientes datos")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
peso = float(input("Peso: "))

# Concatenar el nombre completo
nombre_completo = apellido + " " + nombre

# Calcular la edad en días y el peso en kilogramos
edad_dias = edad * 365
peso_kg = peso / 2.20462  # Convertir de libras a kilogramos

# Mostrar los resultados
print("Nombre completo:", nombre_completo)
print("Edad en días:", edad_dias)
print("Peso en kg:", peso_kg)