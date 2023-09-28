import sys

def max_customers(n, times):
    # Crear una lista para almacenar todos los tiempos junto con su tipo (llegada o salida)
    all_times = []
    for t in times:
        all_times.append((t[0], 'arrival'))
        all_times.append((t[1], 'departure'))
    
    # Ordenar la lista de tiempos en orden ascendente
    all_times.sort()

    max_customers = 0  # Inicializar el número máximo de clientes
    current_customers = 0  # Inicializar el número actual de clientes
    
    for t in all_times:
        if t[1] == 'arrival':
            current_customers += 1  # Un cliente llega
            max_customers = max(max_customers, current_customers)  # Actualizar el máximo
        else:
            current_customers -= 1  # Un cliente sale
    
    return max_customers

def to_tuple(el): 
    arrival, departure = map(int, el.strip().split(' '))
    return (arrival, departure)

if __name__ == '__main__':
    x = int(sys.argv[1])
    times = list(map(to_tuple, sys.argv[2:]))

    result = max_customers(x, times)

    print(result)
