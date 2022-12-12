# We are given an array A[1..n], which stores a sequence of 0’s and then followed by a sequence of 1’s.
# (a) (3 points) Design an O(logn)-time algorithm to find the location of the last 0, i.e, find k
# such that A[k] = 0 and A[k + 1] = 1. Justify the time complexity of the algorithm.
# (b) (5 points) Suppose that k is much smaller than n. Is it possible to improve the running time
# of our algorithm to O(log k) instead of O(log n)? Justify your answer.

n = 10
C = [0] * 5
B = [1] * 5
A = C+B
# print(A )


def solution6a(arr):
    i = 0
    j = n-1
    while i <= j:
        mid = (i + j)//2
        if arr[mid] == 1:
            j = mid - 1
        elif arr[mid] == 0 and arr[mid + 1] == 1:
            return mid
        else:
            i = mid + 1
    return i


# solutiona(A )
# print(solutiona(A))
# Justify the time complexity of the algorithm.
#   T(n) = T(n/2) + O(1)
# Using Master's theorem case 2  计算
B2 = [1] * 5000
A = C+B2


def solution6b(arr):
    i = 0
    step = 1
    dir = 1
    while arr[i] == 0:
        i = i + dir * step
        if arr[i+1] == 1 and arr[i] == 0:
            return i
        elif arr[i+1] == 0 and arr[i] == 0:
            step *= 2
    dir = -1
    step //= 2
    while not (arr[i+1] == 1 and arr[i] == 0):
        i = i + dir * step
        if arr[i+1] == 1 and arr[i] == 0:
            return i
        elif arr[i+1] == 0 and arr[i] == 0:
            step //= 2
            dir = 1
        elif arr[i] == 1:
            dir = -1
            step //= 2
    return i


# print(solution6b(A))


# 从头开始走，一开始步长为 1，走一步后如果还是 0，步长乘 2，否则步长除以 2 然后向回走，每次之后步长除以 2


# reference: https://stackoverflow.com/questions/53437095/strongly-connected-components-with-bfs
#  one topo bfs, vistied , and then reverse graph https://oi-wiki.org/graph/scc/
# https://leetcode.cn/submissions/detail/189908577/

adjs = [
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0]
]
n = 7


def solution11(adjs, n):
    visited = [False] * n
    


str1 = "STATIONARY"
str2 = "TERTIARY"

# 16


def minDistance(word1: str, word2: str) -> int:
    n1, n2 = len(word1), len(word2)
    dp = [[0 for i in range(n2 + 1)]for j in range(n1+1)]
    for i in range(n2+1):
        dp[0][i] = i
    for i in range(n1+1):
        dp[i][0] = i

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] - 1)
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[n1][n2]

print(minDistance(str1,str2))
