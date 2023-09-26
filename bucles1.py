def odd_numbers(maximum):
    return_string = ""  # Inicializa la variable como una cadena vacía

    # Completa el bucle for con un rango que incluya todos
    # los números impares hasta el valor "maximum".
    for number in range(1, maximum + 1, 2):  # Usamos un paso de 2 para obtener solo números impares

        # Completa el cuerpo del bucle anexando el número impar
        # seguido de un espacio a la variable "return_string".
        return_string += str(number) + " "

    # Este comando .strip eliminará el espacio final " " al final del "return_string".
    return return_string.strip()

print(odd_numbers(6))  # Debería ser "1 3 5"
print(odd_numbers(10)) # Debería ser "1 3 5 7 9"
print(odd_numbers(1))  # Debería ser "1"
print(odd_numbers(3))  # Debería ser "1 3"
print(odd_numbers(0))  # No se muestran números, debería ser una cadena vacía
