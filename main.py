
def dot_product(m1: list[int], m2: list[int]) -> int:
    if len(m1) != len(m2):
        return
    else:
        dot = 0
        for ind in range(len(m1)):
            dot += m1[ind] * m2[ind]
        return dot


def matrix_multiplication(m1: list[list[int]], m2:list[list[int]]) -> list[list[int]]:
    if len(m1[0]) != len(m2):
        return
    res = [[0] * len(m1) for _ in range(len(m2[0]))]
    for r in range(len(m1)):
        for c in range(len(m2[0])):
            for k in range(len(m2)):
                res[r][c] += m1[r][k] * m2[k][c]
    return res

l1 = [1,2,3]
l2 = [4,5,6]
print(dot_product(l1, l2))

m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

m2 = [[0,0,0],
      [1,2,3],
      [4,5,6]]
print(matrix_multiplication(m1, m2))