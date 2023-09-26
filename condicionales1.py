def clothing_type(temp):
    if temp >= 70:
        clothing = "T-Shirt"
    elif temp >= 50:
        clothing = "Sweatshirt"
    elif temp >= 32:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing

print(clothing_type(72)) # Debería imprimir "T-Shirt"
print(clothing_type(55)) # Debería imprimir "Sweatshirt"
print(clothing_type(65)) # Debería imprimir "Sweatshirt"
print(clothing_type(50)) # Debería imprimir "Jacket"
print(clothing_type(45)) # Debería imprimir "Jacket"
print(clothing_type(32)) # Debería imprimir "Heavy Coat"
print(clothing_type(0)) # Debería imprimir "Heavy Coat"
