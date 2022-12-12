两次考试都是midterm

第一次考试, 包括search和sorting.  divide and conquer, graphs, 动态规划.10月20.

闭卷, 5-6个问题,不考矩阵乘法和subarray

##### 第一题

快排最坏复杂度是O(n^2) , 用mergesort可以保证.

##### 第二题

先拓扑排序. O(v+e)

vi 没有入度. 

ni = 0 如果vi !=s,  

vi 有k个入度

ni = nj1+ ... + njk  if vi != s

ni = nj1 + .... njk+ 1   if vi ==s

最多经过n个节点, O(V)

最多加E次, 所以O(e) , 总共 O(V+E)

##### 第三题

假设不连通, 那么一定有两个节点没有path, 那么在这里加一条边.就没有cycle, 

#### 第二次考试

贪心, randomized 算法,  5678 ppt .

包括: 

1. dijkstra 算法
2. prim 算法
3. huffman 算法
4. greedy algorithhm for set cover problem
5. 动态规划 for 最大独立集 
6. 多项式时间 解2SAT 问题.

要求会证明, 会分析, 会应用

1. Let G be a connected undirected weighted graph such that no two edges have the same weight. Prove that G has a unique minimum cost spanning tree.

设这个树的边为T,  假如存在别的边f,  f不属于T.  如果f加入T, 由于T是树, 就有循环. 循环中的一个边e,   f不能比原来的路径e大, 因为要求最小cost, 不能比e小, 否则T就应该选择f.  但是又没有相等的边, 所以不存在这个f. 

或者第二种写法: 

假设有2个最小成本生成树𝐴，𝐵在𝐺，边𝑒连接𝐴中的节点𝛼，𝛽。另外，我们假设边𝑒具有最小的成本。所以，很明显，𝑒不在𝐵中，并且在𝐵中应该有一条从𝛼, 𝛽出发的路径𝑖。如果我们把𝑒加到𝐵，那么𝐵中就有一个循环。同样地，如果我们把𝑖加到𝐴中，𝐴中也有一个循环。考虑到𝐴中的循环，我们知道最小成本生成树不包含循环。因此，循环中至少有一条边𝑒′不在𝐴中，根据定义，𝑒′的成本应该大于𝑒的成本。那么，如果我们选择e ，那么我们可以得到𝐴中成本最小的生成树。所以，只有一条路径连接𝛼和𝛽 ,不会用e'，这意味着𝐺有一个唯一的最小成本生成树。

greedy algorithhm for set cover problem  就是每次计算成本. 

动态规划 for 最大独立集  从下往上计算即可.  不要忘了计算数值, 还要写出选择了那些点!!!! 
