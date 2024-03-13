# Further explanation for rowPointers - Matrix has m=7 rows.
# Array [0, 1, 3, 4, 7, 8, 9, 11] is of length m + 1 = 8 and defines 7 ranges.
# i. Range [0, 1) of size 1 for the first row containing single element ‘a’ at
# index 0 in targets.
# ii. Range [1, 3) of size 2 for the second row containing 2 elements ‘b’ &
# ‘c’ at index 1 & 2 in targets.
# iii. Range [3, 4) of size 1 for the third row containing single element ‘d’
# at index 3 in targets.
# iv. Range [4, 7) of size 3 for the fourth row containing 3 elements ‘e’, ‘f’
# & ‘g’ at index 4, 5 & 6 in targets.
# v. Range [7, 8) of size 1 for the fifth row containing single element ‘h’ at
# index 7 in targets.
# vi. Range [8, 9) of size 1 for the sixth row containing single element ‘i’ at
# index 8 in targets.
# vii. Range [9, 11) of size 2 for the last seventh row containing 2
# elements ‘j’ and ‘k’ at index 9 & 10 in targets.
# Image for visual understanding
#     Your task is - given m, n, targets, columnIndices and rowPointers , return a m
# x n matrix representing the enemy targets on the battlefield. All elements of the
# matrix which are not enemy targets should be assumed to be safe zones
# represented by letter ‘z’.
# A program for this.


def war(m, n, targets, column_indices, row_pointers):
    matrix = []
    for i in range(m):
        matrix.append(['z'] * n)

    for i in range(m):
        for j in range(row_pointers[i], row_pointers[i + 1]):
            matrix[i][column_indices[j]] = targets[j]

    return matrix


m = int(input())
n = int(input())
targets = list(map(str, input().split()))
column_indices = list(map(int, input().split()))
row_pointers = list(map(int, input().split()))

answer = war(m, n, targets, column_indices, row_pointers)
for i in range(m):
    print(*answer[i])

# print(war(7, 7, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'],
#           [5, 1, 6, 3, 3, 4, 5, 0, 5, 3, 5], [0, 1, 3, 4, 7, 8, 9, 11]))
