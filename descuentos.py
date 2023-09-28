import sys

def calcular_precio_con_descuento(precio, descuento):
    precio_producto = float(precio)
    descuento_producto = float(descuento)
    precio_con_descuento = precio_producto - (precio_producto * (descuento_producto / 100))
    return precio_con_descuento

def precio_total_lista(lista_productos):
    precio_total = 0

    for producto in lista_productos:
        precio, descuento = producto.split()
        precio_con_descuento = calcular_precio_con_descuento(precio, descuento)
        precio_total += precio_con_descuento

    return precio_total

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python programa.py producto1 producto2 ...")
        sys.exit(1)

    lista_productos = sys.argv[1:]
    result = precio_total_lista(lista_productos)
    print(result)
