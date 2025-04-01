# Definir las variables
cantidad = 0.0
precio_unitario = 0.0
total = 0.0
descuento = 0.0
monto_final = 0.0

# Solicitar los datos al usuario
cantidad = float(input("Dime la cantidad de productos: "))
precio_unitario = float(input("Dime el precio unitario del producto: "))

# Calcular el total, el descuento y el monto final
total = cantidad * precio_unitario
descuento = total * 0.10
monto_final = total - descuento

# Mostrar el monto final
print("El monto final a marcar es:", monto_final)