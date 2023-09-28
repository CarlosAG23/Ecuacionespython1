import sys

def convertir_moneda(cadena):
    # Definir las tasas de conversión
    tasas = {
        "USD a EUR": 0.85,
        "EUR a USD": 1.18
    }

    # Dividir la cadena en cantidad, moneda1 y moneda2
    partes = cadena.split()
    cantidad = float(partes[0])
    moneda1 = partes[1]
    moneda2 = partes[3]

    # Verificar si la conversión es posible
    if f"{moneda1} a {moneda2}" in tasas:
        tasa = tasas[f"{moneda1} a {moneda2}"]
        cantidad_convertida = cantidad * tasa
        return cantidad_convertida
    else:
        return "Tasa de conversión no encontrada"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python nombre_del_script.py 'cantidad moneda1 a moneda2'")
        sys.exit(1)

    cadena = sys.argv[1]

    result = convertir_moneda(cadena)

    print(result)
