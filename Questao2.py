def fibonacci(n):
    a, b = 0, 1
    fib_sequence = [a]

    while b <= n:
        fib_sequence.append(b)
        a, b = b, a + b

    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."


numero = int(input("Informe um número: "))
resultado = fibonacci(numero)
print(resultado)
