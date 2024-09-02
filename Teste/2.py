def is_fibonacci(n):
    if n < 0:
        return False

    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Exemplo de uso:
numero = int(input("Digite um número: "))
if is_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
