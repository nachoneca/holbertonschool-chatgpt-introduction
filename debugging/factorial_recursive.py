#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcula el factorial de un número utilizando recursión.

    Args:
        n (int): El número para calcular su factorial.

    Returns:
        int: El factorial de n.

    """
    # Caso base: factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: n * factorial(n-1)
    else:
        return n * factorial(n-1)

# Verifica si se proporciona un argumento al script
if len(sys.argv) != 2:
    print("Uso: {} <numero>".format(sys.argv[0]))
    sys.exit(1)

try:
    # Intenta calcular el factorial del argumento proporcionado
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    # Si el argumento no es un número entero, muestra un mensaje de error
    print("Por favor, ingrese un número entero como argumento.")
    sys.exit(1)
