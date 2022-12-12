

第一次考试, 包括search和sorting.  divide and conquer, graphs, 动态规划.10月20.

闭卷, 5-6个问题,不考矩阵乘法和subarray





作业5

Design an O(n log n)-time algorithm that, for given integers x and a1, a2, . . . , an, deter- mines whether or not there exist ai and aj whose difference is exactly x. Justify the time complexity of the algorithm







#### homework6

##### a

```python
n = 10
C = [0] * 5 
B = [1] * 5
A =  C+B 
# print(A )
def solution6a( arr):
    i = 0 
    j = n-1
    while i <= j :
        mid = (i +j)//2
        if arr[mid] == 1 :
            j = mid - 1
        elif arr[mid] == 0 and arr[mid +1] == 1:
            return mid 
        else:
            i = mid +1
    return i 
```

比较时间为O(1),  



Justify the time complexity of the algorithm :

 T(n) = T(n/2) + O(1)

Using Master's theorem case 2  to calculate

##### b

```python
B2 = [1] * 5000
A = C+B2
def solution6b( arr):
    i = 0
    step = 1
    dir = 1 
    while  arr[i] == 0:
        i = i +  dir * step
        if arr[i+1] == 1 and arr[i] == 0:
            return i 
        elif arr[i+1] == 0 and arr[i] == 0:
            step *=2 
    dir = -1
    step//=2
    while not ( arr[i+1] == 1 and arr[i] == 0):
        i = i +  dir * step
        if arr[i+1] == 1 and arr[i] == 0:
            return i 
        elif arr[i+1] == 0 and arr[i] == 0:
            step //=2 
            dir = 1
        elif arr[i] == 1:
            dir = -1
            step //=2 
    return i 
```



#### 作业9

Design a linear time algorithm for the following problem: for a given directed graph G, check if, for every two nodes u and v, there is a directed path from u to v or from v to u. Justify the time complexity of the algorithm.





#### homework11



12



#### 15

Design an O(n^2)-time algorithm based on dynamic programming to find the maximum length of monotonically increasing subsequence 最长上升子序列 of a sequence of n pairwise different integers. For example, (1,3,9) is a monotonically increasing subsequence of maximum length of the sequence (1, 7, 3, 2, 9). Justify the time complexity of the algorithm.





#### homework16

```python
str1 = "STATIONARY"
str2 = "TERTIARY"
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
```

so the answer is 5



## 第二次作业



8 For an undirected graph G = (V,E), a dominating set is a subset S ⊆ V such that for each vertex v ∈ V, v ∈ S or a neighbor u of v is in S. Prove that the dominating set problem DS(G, k) such that the graph G contains a dominating set S of size k is NP-complete.



DS =>VC

We say that a problem (a language) L1 ⊆ A∗ is a linear-time reducible to problem (a language) L2 ⊆ B∗ (written L1 < L2) if there exists a linear-time computable function φ : A∗ → B∗ suchthatforallα∈A∗,α∈L1 ifandonlyifφ(α)∈L2.

Suppose we know L1 < L2 (i.e., L1 is linear-time reducible to L2) and L2 < L3. Assume that the time complexity of L2 is Θ(n2).

(a) What we can say about the time complexity of L1? Justify your answer. 

L1<L2

(b) What we can say about the time complexity of L3? Justify your answer.

L2<L3



10.  an undirected graph G = (V,E), we define a clique of size k in G for some positive integer k, as a complete subgraph of G with k vertices. Prove that to find whether a graph G contains a clique of size at least k is an NP-complete problem

VC - > CLIQUE

clique 属于NP: 

检查每个vetex in clique 

clique属于NP hard. 

reduce vertex-cover 问题到clique问题.



### 9 partial recursive function



