def inverter_string(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado

# Exemplo de uso:
entrada = input("Digite uma string para inverter: ")
print("String invertida:", inverter_string(entrada))
