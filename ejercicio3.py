# Definir las variables
monto_prestamo = 0
tasa_interes_anual = 0.0
tiempo_prestamo = 0
monto_total = 0.0

# Solicitar el monto del préstamo
print("Rellene los siguientes datos")
monto_prestamo = int(input("¿Cuál es el monto del préstamo? "))

# Definir tasa de interés y tiempo
tasa_interes_anual = 0.03
tiempo_prestamo = 5

# Calcular el monto total utilizando la fórmula M = P * (1 + r)^t
monto_total = monto_prestamo * (1 + tasa_interes_anual) ** tiempo_prestamo

# Mostrar el monto total a pagar después de 5 años
print("El monto total a pagar en 5 años es de:", monto_total)