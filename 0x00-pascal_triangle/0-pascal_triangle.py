def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        previous_row = triangle[i-1]
        current_row = [1]
        for j in range(1, i):
            current_row.append(previous_row[j-1] + previous_row[j])
        current_row.append(1)
        triangle.append(current_row)

    return triangle