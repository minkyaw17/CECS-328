def connected_components(matrix):
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "1":  # if a 1 is found, we will explore it to see the number of connected components
                count += 1
                DFS(matrix, i, j)

    return count


def DFS(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]) or matrix[i][j] == "0":  # boundary checking
        return

    matrix[i][j] = "0"  # set the grid we're on to 0 when we see a 1, so we don't revisit it
    DFS(matrix, i - 1, j)  # up
    DFS(matrix, i + 1, j)  # down
    DFS(matrix, i, j - 1)  # left
    DFS(matrix, i, j + 1)  # right


matrix = [
  ["1", "1", "1", "0", "1"],
  ["1", "0", "0", "0", "0"],
  ["0", "0", "1", "1", "0"]
]


num = connected_components(matrix)


print("The total number of connected components is", num)
