# huge-average
内存中有 1000万 个 (a,b) pair，a 和 b 都是整数，b 相同的 pair 属于同一个 group，要求快速计算每个 group 中 a 的平均值，并且输出这个平均值和 b 组成的新的 pair，也就是：(avg(a), b)

注意：
1. 输入的 pair 不一定按照 b 有序
2. 输出的 pair 不要求有序
3. 某个 group 的数据量可能非常大
4. 请使用多线程实现

一个输入输出样例：
输入 (a, b) pair 序列，例如：
1, 1
4, 2
2, 1
5, 2
3, 1
6, 2

输出：(avg(a), b) 序列，上面例子的输出的结果是：
2, 1
5, 2
-----------------------------------------------------------我的做法是先在pairs里去除重复的b值，然后对于每个独特的b值开一个线程并计算其对应所有a值的平均值。
这样做的好处是算法可读性高，但是没有针对我的机器或云服务器的运算节点个数开相应的线程数，效率不是很好。我也查阅了一些资料，但还是不太确定开多少线程最高效，希望接下来在这方面再了解多点。
