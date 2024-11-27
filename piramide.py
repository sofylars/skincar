print("sofia larios rodriguez")
def pascal_triangle(rows):
    """
    Genera el Triángulo de Pascal con el número de filas indicado.
    :param rows: Número de filas
    :return: Lista de listas representando el Triángulo de Pascal
    """
    triangle = [[1]]  # Primera fila
    for i in range(1, rows):
        row = [1]  # Cada fila empieza con 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Cada fila termina con 1
        triangle.append(row)
    return triangle

# Ejemplo de uso
rows = 5  # Número de filas deseadas
triangle = pascal_triangle(rows)
print("Triángulo de Pascal:")
for row in triangle:
    print(row)
