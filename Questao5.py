def inverter_string(s):
    inversa = ''
    for char in s:
        inversa = char + inversa  
    return inversa


entrada = input("Informe uma string: ")
resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")
