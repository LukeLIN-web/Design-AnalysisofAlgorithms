## Design & Analysis of Algorithms

 randomized算法： 快排，  global minimum cut， hushing。

P and NP： cook theorem， exmaple of NP complete

Partial recursive functions： theorem of post, diophantine equations.

Homework40%， 2次期中考30%， project 40%。

project 3-5个人， 选一个问题， 用两种算法， 就和浙大ads差不多。

前4周开题报告， 第五周提交， 第六周批准报告。 

作业也可以组队写。  如果你找到了作业答案， 你应该引用来源。

期中考， 闭卷， 5-6个问题， 上课考。

 题型， 设计算法， 分析算法， 证明， 应用算法。

第一次考的算法：

插入，merge排序。 integer multiplication，matrix 乘法，  DAG拓扑排序， 矩阵链式乘法， floyd-warshall 算法， 编辑距离， subarray 问题-最大sum和length。 

22fall不考矩阵乘法和subarray

第二次考的算法：

dijkstra，prim，huffman，选择， 快排， 压缩算法，  贪心算set cover问题， 动态规划算Maximum Independent Set problem in tree， Polynomial time algorithm for 2-SAT Problem

#### lec2

如果存在一个计算能经过该节点的输入，我们将说决策树的一个节点是 realizable。
稍后我们将假设在所考虑的决策树中，所有节点都是可实现的realizable。

为什么他们要把这些节点的数量加起来？

算数平均数大于几何平均数， 可以证明平均高度>=log2n  

LA（n） = h(D) and La avg(n) = havg(D)

 2–3树中的内部节点可以有2个子节点或3个子节点，叶子节点有1至2个数据元素.

父节点数值等于它儿子最右边的节点. 要记住是怎么插入和删除的. 

#### lec3 

插入排序复杂度  <= log2 n! + n-1  , 平均时间 也是. 

就是log2(2) + log2(3) +.. 累加. 

可以求极限,  把这个 / nlogn 求极限就 =1  , 这就是为啥要学微积分. 

#### lec4

各个符号的区别. 

大O 最重要, 要记下来,  fn =O(g(n))     存在正数c, 和n0, 使得对于所有n>n0, fn <= cg(n)
$$
fn =\Omega ((g(n)))存在常数使得cgn <= fn \\
 fn = \Theta((g(n))) 存在常数c1,c2 使得  c1gn <=fn <=c2gn\\
 这些 O,Ω,o,w,\Theta, 都是有传递性Transitivity的.\\
 O,Ω,\Theta 是有自反性reflexivity \\
 \Theta 有对称性symmetry\\
$$

 Transpose Smmetry: O和Ω,  o 和 w 

可能同时符合大O, theta和Ω. 比如 fn = pn^2 + qn +r  ,我们有fn >= pn^2 .  设t= p+q+r, fn <= tn^2. 

f(n) = o(g(n)) 对于任何c>0 都存在n0 , 对于所有n> n0有 f(n) < c(g(n))

f(n) = w(g(n))对于任何c>0 都存在n0   对于所有n> n0有 c(g(n)) < f(n)

然后考虑一些性质. 

O(n) 取log 或者 2^O(n)都是不保持大O的.

#### lec5

主定理, 

大数乘法, n bit的数, 相乘需要 O(n^2). 

我们采用分块乘.  分成左右两半, 左边的乘法是 O(n/2) , 右边的是 O(n/2) , 中间的(XL +XR)(YL +YR)就只需要乘一次.也是 O(n/2).

XLYR +XRYL = (XL +XR)(YL +YR)−XLYL −XRYR.      XLYL  和XRYR 是已经 计算了的, 

#### lec6  

矩阵乘法, 也可以用递归然后主定理, 上界达到  log2(7), n的2.37次方左右. 据说会考

 FFT 

### lec7graph

如果图中任意两点都是连通的，那么图被称作连通图.如果此图是有向图，则称为强连通图（注意：需要双向都有路径）。

无向连通图,没有环,就叫做树. 

1. 树是连通图, 有n个顶点, n-1个边
2. 树有n-1个边, 没有环.

Let G be an undirected graph with n nodes. Then the following three statements are equivalent:

(a) G is connected and does not contain a cycle. (b) G is connected and has n − 1 edges.
 (c) G has n − 1 edges and does not contain a cycle.

无向图G的连通分量就是 G的一个最大连通子图. 

可以用bfs发现所有强连通分量.  看PPT3 graph, 

https://oi-wiki.org/graph/scc/

强连通分量就是从任意一个节点出发都可以到任意节点. 

 从一个节点出发, 同时bfs 图和反图得到set V1和V2, 强连通分量就是V1交V2. 

第九题, 可能没有every. 

Design a linear time algorithm for the following problem: for a given directed graph G, check if, for every two nodes u and v, there is a directed path from u to v or from v to u. Justify the time complexity of the algorithm.

就是先dfs找到强连通分量, 然后 强连通分量缩成一个点, topo排序.  O(V+E)时间就可以.

Lemma 3.11连通图p个顶点q个边, 我们有 q>= p-1

Theorem 3.12 For any planar embedding of a connected planar graph G = (V,E) with p vertices, q edges and r faces the following equality holds: p − q + r = 2.

Corollary 3.15. Let G be a connected planar graph with p ≥ 3 vertices and q edges. Then q ≤ 3p − 6.

期中考:

一个无向连通图, 失去了任意一条边就没有了连通性.  证明它是个树.

期中考那个算法, 应该要拓扑排序, dp. 

clique 问题, 二分子图问题, 最大割问题在平面图planar graph上, 有多项式解.

欧拉定理:

所有的平面连通图,  p个顶点q个边, r个面, 一定满足 p -q+r= 2 

平面图是可以画在平面上并且使得不同的边可以**互不交叠**的图. K5是最小的非平面图.

证明:  一个边最多属于两个面.   然后一个面至少要3个边形成一个环. 

graph K3,3 也不是平面图. 考过这个的证明

1930年, kuratowski发现, 一个图是planar <=>  not have  K5 or K3,3 as a minor.

### lec8动态规划

子问题, 如果子问题的数量是多项式个, 子问题的解也是多项式时间, 我们就可以找到原问题多项式时间的解. 

Floyd-Warshall algorithm 最短路径是O(n^3)

##### 矩阵乘法

(AB)C 需要 n平方+ n立方次乘法

A(BC) 就只需要n平方+ n平方次乘法

我们研究加括号问题, 怎么加乘法次数最少.
$$
C(i,j) =  min{  (C(i,k) + c(k+1,j) +  mi-1m_k m_j)}
$$


编辑距离:So, the considered algorithm makes O(mn) operations of addition and comparison of numbers.

E(i,j) = min{1+E(i−1,j),1+E(i,j−1),diff(i,j)+E(i−1,j−1)}.

we can create an algorithm for computation of F(m,n) which use O(mn) operation

### lec9 贪心算法

#### Dijkstra

求解 **非负权图** 上单源最短路径的算法。**求一个节点（称为“源节点”）到所有其它节点的最短路径**

将结点分成两个集合：已确定最短路长度的点集（记为 S集合）的和未确定最短路长度的点集（记为 T集合）。一开始所有的点都属于T 集合。

初始化 dis(s) = 0，其他点的dis均为 infinite 。

然后重复这些操作：

1. 从 T集合中，选取一个最短路长度最小的结点，移到 S集合中。
2. 对刚刚被加入S集合的结点的所有出边执行求最小操作。我们尝试用这条路径去更新最短路的长度，如果这条路径更优，就进行更新。

直到 T集合为空，算法结束。

#### 正确性证明

下面用数学归纳法证明，在 **所有边权值非负** 的前提下，Dijkstra 算法的正确性.

证明每次取出的u的距离就是最短路.

一开始S=空, 成立 , 第一个加入s, 也成立. 

假设u点为算法中第一个在取出时不满足距离是最短路的顶点.

那么存在 s ->x ->y ->u.  x属于S, y属于T. 有D(x) = dis(x). D(y) = dis(y).

因为边非负, 所以dis(y) <= D(y) <= D(u)<= dis(u). 但是如果u是第一个取出时不满足的最短路, 那么 dis(u) <= dis(y) . 矛盾, 所以每个取出的顶点, 都满足最短路. 

#### 最小生成树

#### 生成树

一个连通图的生成树是一个极小的连通子图，它包含图中全部的n个顶点，但只有构成一棵树的n-1条边。多加一条边就会产生环. 

我们定义无向连通图的 **最小生成树**（Minimum Spanning Tree，MST）为边权和最小的生成树。

##### Kruskal 算法

是一种常见并且好写的最小生成树算法，由 Kruskal 发明。该算法的基本思想是从小到大加入边，是个贪心算法。

```python
sort(edges,key =weight)
for u,v,w in edges:
	if u v not connected in the union-find set:
    connect u and v in union-find set
    result += (u,v)
return result 
```

如果使用并查集，就可以得到时间复杂度为O(m logm ) 的 Kruskal 算法。

证明: n=1 最小生成树存在. https://oi-wiki.org/graph/mst/ 

##### Prim 算法

Prim 算法是另一种常见并且好写的最小生成树算法。该算法的基本思想是从一个结点开始，不断加点（而不是 Kruskal 算法的加边）。

具体来说，每次要选择距离最小的一个结点，以及用新的边更新其他结点的距离。

其实跟 Dijkstra 算法一样，每次找到距已知最小的一个点，可以暴力找也可以用堆维护。不同之处在于prim是到点集中任意一点最短的点,  dijkstra是到source点的距离最短的点. 注意!!!  是已知节点, 不是起始节点.

proof:

从任意一个结点开始，将结点分成两类：已加入的，未加入的。

每次从未加入的结点中，找一个与已加入的结点之间边权最小值最小的结点。

然后将这个结点加入，并连上那条边权最小的边。

重复 n-1次即可。

证明最优 : <=> 证明在每一步，都存在一棵最小生成树包含已选边集。

基础：只有一个结点的时候，显然成立。

归纳：如果某一步成立，当前边集为F ，属于 T这棵 MST，接下来要加入边e 。

如果 e属于T，那么成立。

否则考虑 T+e 环上另一条可以加入当前边集的边f 。

首先， f的权值一定不小于e 的权值，否则就会选择 f而不是 e了。

然后，f 的权值一定不大于 的权值，否则 T+e-f就是一棵更小的生成树了。

因此， e和 f的权值相等，T+e-f 也是一棵最小生成树，且包含了F 。

#### Huffman 

注意是prefix-free的编码, 让我们通过一个反例来理解前缀代码。假设有a、b、c、d四个字符，它们对应的变长编码分别为00、01、0、1。这种编码会导致歧义，因为分配给c的编码是分配给a、b的编码的前缀.

统计所有字符的频率, 每个字符作为一个节点放入到堆,  然后从频率最小的两个节点开始, 得到一个新节点, 放回到堆, 再拿出两个频率最小的字符...   最后得到树.最后别忘记把所有字符转换为编码. 

### lec10 随机化算法

PPT6,  对于一个网络流图，其割的定义为一种**点的划分方式**：将所有的点划分为S 和 T =V-S 两个集合.

割的容量 :  我们的定义割 (S,T)的容量c(S,T) 表示所有从 S到T 的边的容量之和.

#### 最小割

最小割就是求得一个割 使得割的容量 最小。全局最小cut

####  contraction算法

a randomized algorithm with simple structure for min-cut finding. This is Contraction Algorithm which was discovered by David Karger in 1992.

该算法的思想是基于[边收缩的概念]   通俗地说，边的收缩合并了节点![你](https://wikimedia.org/api/rest_v1/media/math/render/svg/c3e6bb763d22c20916ed4f0bb6bd49d7470cffd8)和化为一，将图的节点总数减一。所有其他边连接![你](https://wikimedia.org/api/rest_v1/media/math/render/svg/c3e6bb763d22c20916ed4f0bb6bd49d7470cffd8)或者![v](https://wikimedia.org/api/rest_v1/media/math/render/svg/e07b00e7fc0847fbd16391c778d65bc25c452597)被“重新附加”到合并的节点，有效地产生一个[多图](https://en.wikipedia.org/wiki/Multigraph)。Karger 的基本算法迭代收缩随机选择的边，直到只剩下两个节点；这些节点代表原始图中的[切割](https://en.wikipedia.org/wiki/Cut_(graph_theory))。通过将该基本算法迭代足够次数，可以[以高概率](https://en.wikipedia.org/wiki/With_high_probability)找到最小切割。

#### 算法执行次数

第一个是k/n , step是n/k次. 第二个是k-1/n , step是n/k-1次. 

### lec12 NP 问题

注意, NP问题不是P问题的补集!!!! NP问题不是非P类问题!   NP问题是指可以在多项式的时间里验证一个解的问题。NP问题的另一个定义是，可以在多项式的时间里猜出一个解的问题

Proposition 7.2.  L1<= p L2 , L2 属于P  =>  L1属于P

Proposition 7.3. L1<= p L2 , L2 不属于P  =>  L1不属于P

#### NP hard

定义:  如果 L' <= pL 对于所有L' 属于 NP . 那么 L 是NP hard,

最重要的性质:

1. 如果L是NP hard, L属于 P .  那么  NP =P
2. 如果L是NP hard, NP != P  .  那么  L不属于P

#### NP完全

定义:  如果 L 属于 NP  并且 L是NPhard , 那么 L 是NP complete 

要证明一个问题L1是NP完全的, 只需要证明它属于NP, 并且找到一些NP hard问题 L2,  L2<=p L1, 就可以推出.

#### independent set problem

是NP完全的.

##### 规约的证明

可以规约到clique问题. 团（clique）是一个[图](https://zh.wikipedia.org/wiki/图论)中两两相邻的一个顶点[集](https://zh.wikipedia.org/wiki/集合)，或是一个[完全](https://zh.wikipedia.org/wiki/完全圖)子图（complete subgraph）证明这问题是[NP完备](https://zh.wikipedia.org/wiki/NP完備)，我们可以很简单的将[独立顶点集问题](https://zh.wikipedia.org/w/index.php?title=獨立頂點集問題&action=edit&redlink=1)(Independent set problem)归约成这个问题。因为存在一个大小是*k*以上的分团，等价于它的[补图](https://zh.wikipedia.org/wiki/補圖)中存在一个大小是*k*以上的[独立集](https://zh.wikipedia.org/wiki/独立集)。 

由图G(V,E)和整数k组成的clique问题的每一个实例都可以转换为独立集问题所需的图G'(V',E')和k'。我们将按以下方式构建图 G'：

> V' = V 即图 G 的所有顶点都是图 G' 的一部分
> E' = 边 E 的补集，即原始图 G 中不存在的边。

图G'是G的补图。计算补图G'所需的时间需要遍历所有的顶点和边。这个的时间复杂度是O(V+E)。

一个独立集是一个图中一些两两不相邻的顶点所形成的集合。换句话说，独立集S由图中若干顶点组成，且S中任两个顶点之间没有边。等价地，图中的每条边至多有一个端点属于S。一个独立集的基数Cardinality是它包含顶点的数目。

动态规划的解法, PPT8 20页. 

Maximum independent set in tree有O(|V| + |E|) 解法. 

#### vertex cover 问题

Let G = (V,E) be a undirected graph. We say that a set S ⊆ V is a vertex cover if every edge e ∈ E has at least one end in S.

Vertex Cover问题指的是给定一个N个点，M条边的无向图G（点的编号从1至N），问是否存在一个不超过K个点的集合S，使得G中的每条边都至少有一个点在集合S中.

Vertex Cover belongs to NP: certificate is a subset with at most k nodes; the verification algorithm checks that each edge has at least one end among these nodes.

可以规约到独立集问题, 

Let S be an independent set. Then, evidently, for each e ∈ E, at least one end of e belongs to V \S. Therefore V \S is a vertex cover. Let V \ S be a vertex cover. Then there is no edge for which both ends belongs to S, and S is an independent set.

有线性算法, 可以得到树上的最小vertex cover. 其实和最大独立集是一样的. 

#### set cover problem

**集合覆盖问题**（ **Set covering problem**，**SCP**） 是NP 完全问题. 

给定全集u，以及一个包含n个集合且这n集合的并集为全集的集合 。集合覆盖问题要找到一个最小的子集，使得他们的并集等于全集。

贪心估计就是计算成本, 然后每次选择成本最少的, 见https://www.geeksforgeeks.org/set-cover-problem-set-1-greedy-approximate-algorithm/

证明是NP的: polynomial time可以确认解的正确性.

证明是NP hard : Let G= (V,E) , k be an instance of Vertex cover. We can create an instance of set cover. where U =E. Family  F for each u 属于 V, Fu contains the edges adjacent to u.  Thus, vertex cover <= p set cover.     

#### SAT问题

SAT是NP-complete 问题 ,  cook1971年,证明很复杂.  

对于特殊的形式, 可以 Polynomial-time reduction of Vertex Cover to Set Cover. 看PPT7 ,29页. 构造一个图.

> **SAT问题**：就是给一些布尔变量赋值，使得所有给你的条件成立的问题---*适定性(Satisfiability)问题*。
>
> 可以证明k>2时候为NP完全问题，而k=2的时候存在多项式解法。

> **2−SAT问题** ： 就是对于每一个条件，最多只于两个变量的真假性有关，

多项式时间 解2SAT 问题. 看2-SAT - 后缀自动机张的文章 - 知乎 https://zhuanlan.zhihu.com/p/50211772 

给出n 个集合，每个集合有两个元素，已知若干个 < a,b >，表示 a与 b矛盾（其中 a与 b属于不同的集合）。然后从每个集合选择一个元素，判断能否一共选 n个两两不矛盾的元素。显然可能有多种选择方案，一般题中只需要求出一种即可。

> 题面：有 n 对夫妻被邀请参加一个聚会，因为场地的问题，每对夫妻中只有1 人可以列席。在 2n个人中，某些人之间有着很大的矛盾（当然夫妻之间是没有矛盾的），有矛盾的 2个人是不会同时出现在聚会上的。有没有可能会有 n个人同时列席？

 从一个节点出发, 同时bfs图和反图得到set V1和V2, 强连通分量就是V1交V2.  对于所有**未访问过的结点**，重复上述过程。 判断强连通分量是否包括xi和xi' 即可.  两次dfs 也可以. O(n+m)

#### 第二次作业

1. 连通无向加权图, 没有两条边有相同weight.  求证 G 有一个unique 最小生成树. 



第三次作业

1.Show that if f is a function of one variable that is recursive, nondecreasing, and unbounded, then its range is an infinite recursive set.



#### 停机问题

是否存在一个算法, 对于给定的输入, 能判定任意算法会停机? 

不存在.  停机问题是不可计算问题. 

  there exists a partial recursive function which can not be extended up to a total recursive function.

#### recursive set

在[可计算性理论](https://zh.wikipedia.org/wiki/可计算性理论)中，一个[自然数的子集](https://zh.wikipedia.org/wiki/可数集合)被称为**递归的**、**可计算的**或具[可判定性](https://zh.wikipedia.org/wiki/可判定性)，如果我们可以构造一个[算法](https://zh.wikipedia.org/wiki/算法)，使之能在有限时间内终止并判定一个给定元素是否属于这个集合。更一般的集合的类叫做[递归可枚举集合](https://zh.wikipedia.org/wiki/递归可枚举集合)。这些集合包括**递归集合**，对于这种集合，只需要存在一个算法，当某个元素位于这个集合中时，能够在有限时间内给出正确的判定结果，但是当元素不在这个集合中时，算法可能会永远运行下去（但不会给出错误答案）

