# Definir las variables
promedio1 = 0.0
promedio2 = 0.0
promedio3 = 0.0
promedio4 = 0.0
promedio5 = 0.0

Acorte1 = 0.0
Acorte2 = 0.0
Acorte3 = 0.0

Bcorte1 = 0.0
Bcorte2 = 0.0
Bcorte3 = 0.0

Ccorte1 = 0.0
Ccorte2 = 0.0
Ccorte3 = 0.0

Dcorte1 = 0.0
Dcorte2 = 0.0
Dcorte3 = 0.0

Ecorte1 = 0.0
Ecorte2 = 0.0
Ecorte3 = 0.0

# Solicitar las notas de los 3 cortes de la primera asignatura
print("Dime tus notas de los 3 cortes de la primera asignatura")
Acorte1 = float(input("Primer corte: "))
Acorte2 = float(input("Segundo corte: "))
Acorte3 = float(input("Tercer corte: "))
promedio1 = (Acorte1 + Acorte2 + Acorte3) / 3

# Solicitar las notas de los 3 cortes de la segunda asignatura
print("Dime tus notas de los 3 cortes de la segunda asignatura")
Bcorte1 = float(input("Primer corte: "))
Bcorte2 = float(input("Segundo corte: "))
Bcorte3 = float(input("Tercer corte: "))
promedio2 = (Bcorte1 + Bcorte2 + Bcorte3) / 3

# Solicitar las notas de los 3 cortes de la tercera asignatura
print("Dime tus notas de los 3 cortes de la tercera asignatura")
Ccorte1 = float(input("Primer corte: "))
Ccorte2 = float(input("Segundo corte: "))
Ccorte3 = float(input("Tercer corte: "))
promedio3 = (Ccorte1 + Ccorte2 + Ccorte3) / 3

# Solicitar las notas de los 3 cortes de la cuarta asignatura
print("Dime tus notas de los 3 cortes de la cuarta asignatura")
Dcorte1 = float(input("Primer corte: "))
Dcorte2 = float(input("Segundo corte: "))
Dcorte3 = float(input("Tercer corte: "))
promedio4 = (Dcorte1 + Dcorte2 + Dcorte3) / 3

# Solicitar las notas de los 3 cortes de la quinta asignatura
print("Dime tus notas de los 3 cortes de la quinta asignatura")
Ecorte1 = float(input("Primer corte: "))
Ecorte2 = float(input("Segundo corte: "))
Ecorte3 = float(input("Tercer corte: "))
promedio5 = (Ecorte1 + Ecorte2 + Ecorte3) / 3

# Mostrar los promedios de las 5 asignaturas
print("Promedio de la primera asignatura:", promedio1)
print("Promedio de la segunda asignatura:", promedio2)
print("Promedio de la tercera asignatura:", promedio3)
print("Promedio de la cuarta asignatura:", promedio4)
print("Promedio de la quinta asignatura:", promedio5)