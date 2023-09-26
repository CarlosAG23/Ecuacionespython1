def identify_IP(IP_address):
    if IP_address == "192.168.1.1":
        IP_description = "Network router"
    elif IP_address == "8.8.8.8" or IP_address == "8.8.4.4":
        IP_description = "Google DNS server"
    elif IP_address == "142.250.191.46":
        IP_description = "Google.com"
    else:
        IP_description = "unknown"
    return IP_description

print(identify_IP("8.8.4.4")) # Debería imprimir 'Google DNS server'
print(identify_IP("142.250.191.46")) # Debería imprimir 'Google.com'
print(identify_IP("192.168.1.1")) # Debería imprimir 'Network router'
print(identify_IP("8.8.8.8")) # Debería imprimir 'Google DNS server'
print(identify_IP("10.10.10.10")) # Debería imprimir 'unknown'
print(identify_IP("")) # Debería imprimir 'unknown'
