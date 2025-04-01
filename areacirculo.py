import math


def calcular_area_circulo():
    # Solicitar el radio del círculo
    radio = float(input("Digite el radio del círculo: "))
    
    # Calcular el área
    area = math.pi * radio ** 2
    
    # Mostrar el resultado
    print(f"El área de un círculo con radio {radio} es: {area:.2f}")

# Llamar a la función
calcular_area_circulo()
