#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) < 2:
    print("Por favor, proporciona un número como argumento.")
    sys.exit(1)

try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Por favor, ingrese un número entero como argumento.")
    sys.exit(1)
