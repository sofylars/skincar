print("sofia larios rodriguez")
def fibonacci_series(n):
    """
    Genera la serie de Fibonacci hasta el enésimo término.
    :param n: Número de términos
    :return: Lista con la serie de Fibonacci
    """
    fib = [0, 1]  # Los primeros dos números de Fibonacci
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Ejemplo de uso
n = 10  # Número de términos deseados
print("Serie de Fibonacci:", fibonacci_series(n))
