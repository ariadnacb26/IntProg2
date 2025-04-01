# Definir las variables
ancho_area = 0.0
alto_area = 0.0
area_m2 = 0.0
total_ladrillos_m2 = 0.0

# Solicitar los datos al usuario
print("Ingresa los siguientes datos")
ancho_area = float(input("¿Cuál es el ancho del área? "))
alto_area = float(input("¿Cuál es el alto del área? "))

# Calcular el área en metros cuadrados y el total de ladrillos
area_m2 = ancho_area * alto_area
total_ladrillos_m2 = area_m2 * 20

# Mostrar el total de ladrillos
print("Total de ladrillos:", total_ladrillos_m2)