"""
Parte fraccionaria
"""

# Entradas
numero = float(input("Introduzca un número: "))

# Proceso
if numero // 1 == numero / 1 :
    resultado = "No tiene decimales"
else: 
    resultado = "Sí tiene decimales"
# Salidas
print(resultado)
