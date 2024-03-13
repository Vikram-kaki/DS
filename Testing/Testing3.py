# Arrangement of Flower pot
# Find the ideal placement for a flower pot in a room full of flower pots. Pots are arranged such
# that all flower pots in row i have height less than or equal to ones in row i+1. Flower pots in each
# row are arranged in ascending order of their height.
# Locate a suitable position to set the flower pot such that it does not violate the ascending order
# arrangement constraint, keeping in mind the room's Length (L) and width (W). Since the room is
# full, it should be noted that when adding a new flower pot, the one in the last position of the
# room will be removed. Your task is to determine the correct spot for this new placement, with the
# starting coordinate being (0,0) and the ending coordinate being (L-1, W-1).
# Note: The higher numbered pot is to be replaced always. Example in an arrangement of 4 6
# sized pots, a pot of size 5 will replace the pot of size 6 and not the pot of size 4.
# Assume, L >= 1, W >= 1
# Input Format:
# Each input contains the following:
# L W - Length & Width of room in number. Constraints - ( L >= 1), ( W >= 1) . Consider L as
# Number of rows in the matrix, W as Number of columns in the matrix.
# Next L line contains array A of size W, where each A[i] represents the height of the flower pots.
# (1<=A[i]<=10^9)
# H - Height of the flower pot in number. Constraints - (1 <= H <= 10^9)
# Output Format:
# I J – Where I is row number, J is column number.
# Sample Test Case 1:
# Input:
# 3 5
# 1 2 3 4 5
# 6 8 9 10 11
# 12 13 14 15 16
# 7
# Output:
# 1 1
# Explanation:
# According to the information provided, the flower pots have been organized by size, starting with
#     the first pot being size 1 and incrementing in order for each subsequent pot. Our task is now to
# position a flower pot with a size of 7. From the given room setup, we observe that the sixth pot
# (sixth position) is of size 6, so the seventh pot should be placed right next to it. Therefore, the
# resulting configuration is represented as 1 1
# Sample Test Case 2:
# Input:
# 3 3
# 1 3 4
# 7 8 9
# 11 13 15
# 14
# Output:
# 2 2

# If the size of flower pot exceeds the last given flower pot. The last given
# flower pot is to be replaced.
# A program for this without run time  errors and taking the input from the user.

def flower_pot(l, w, a, h):
    if h > a[-1]:
        return l - 1, w - 1

    for i in range(l):
        for j in range(w):
            if a[i][j] > h:
                return i, j

    return -1, -1

l, w = map(int, input().split())
a = []
for i in range(l):
    a.append(list(map(int, input().split())))
h = int(input())

i, j = flower_pot(l, w, a, h)
print(i, j)


