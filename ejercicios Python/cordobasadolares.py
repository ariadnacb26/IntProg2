def convertir_cordobas_a_dolares():
    # Solicitar la cantidad en cordobas
    cordobas = float(input("Ingrese la cantidad en cordobas: "))
    
    # Solicitar el tipo de cambio
    tipo_cambio = float(input("Ingrese el tipo de cambio: "))
    
    # Realizar la conversión
    dolares = cordobas / tipo_cambio
    
    # Mostrar el resultado
    print(f"La cantidad en córdobas es: {dolares:.2f}")

# Llamar a la función
convertir_cordobas_a_dolares()
