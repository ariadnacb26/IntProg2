def convertir_dolares_a_cordobas():
    # Solicitar la cantidad en dólares
    dolares = float(input("Ingrese la cantidad en dólares: "))
    
    # Solicitar el tipo de cambio
    tipo_cambio = float(input("Ingrese el tipo de cambio: "))
    
    # Realizar la conversión
    cordobas = dolares * tipo_cambio
    
    # Mostrar el resultado
    print(f"La cantidad en córdobas es: {cordobas:.2f}")

# Llamar a la función
convertir_dolares_a_cordobas()
