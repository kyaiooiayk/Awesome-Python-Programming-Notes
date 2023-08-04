#!/usr/bin/env python
# coding: utf-8

# # Introduction to Greedy Algorithms

# The subfamily of *Greedy Algorithms* is one of the main paradigms of algorithmic problem solving next to *Dynamic Programming* and *Divide & Conquer Algorithms*. The main goal behind greedy algorithms is to implement an efficient procedure for often computationally more complex, often infeasible brute-force methods such as exhaustive search algorithms. 
# 
# The main outline of a greedy algorithms consists of 3 steps:
# 
# - make a greedy choice
# - reduce the problem to a subproblem (a smaller problem of the similar type as the original one)
# - repeat
# 
# So, greedy algorithms are essentially a problem solving heuristic, an iterative process of tackling a problem in multiple stages while making an locally optimal choice at each stage. In practice, and depending on the problem task, making this series of locally optimal ("greedy") choices must not necessarily lead to a globally optimal solution.

# ## Example 1: Coin Changer
# 
# To look at a first, naive example of a greedy algorithm, let's implement a simple coin changing machine. Given a money value in cents, we want to return the minimum possible number of coins, whereas the possible denominations are 1, 5, 10, and 20 cents.

# In[3]:


def coinchanger(cents, denominations=[1, 5, 10, 20]):
    coins = {d: 0 for d in denominations}
    for c in sorted(coins.keys(), reverse=True):
        coins[c] += cents // c 
        cents = cents % c
        if not cents:
            total_coins = sum([i for i in coins.values()])
            return sorted(coins.items(), reverse=True), total_coins


# The funtion above creates a dictionary, `coins`, which tracks the number of coins of each denomination to be returned. Then, we iterate though the denominations in descending order of their value. Now, in a "greedy" fashion, we count the highest possible number of coins from the largest denomination in the first step. We repeat this process until we reached the smallest denomination or the number of remaining `cents` reaches 0. 

# In[4]:


coinchanger(cents=100)


# Calling out `coinchanger` function with 100 cents as input, it returns 5 coins a 20 cents, the smallest, possible number of coins that can be returned in this case. Below are some more examples: 

# In[5]:


coinchanger(cents=5)


# In[6]:


coinchanger(cents=4)


# In[7]:


coinchanger(cents=23)


# ## Example 2: Knapsack

# Now, let us take a look at a classic, combinatorial optimization problem, the so-called "knapsack" problem. Here, we can think of a "knapsack" as a rucksack, and our goal is to fill it with items so that the rucksack's contents have the highest possible value. Of course, the knappsack has a certain weight capacity, and each item is associated with a certain value and a weight. In other words, we want to maximize the value of the knapsack subject to the constraint that we don't exceed its weight capacity.
# 
# As trivial as it sounds, the knapsack problem is still one of the most popular algorithmic problems in the modern computer science area. There are numerous applications of knapsack problems, and to provide an intuitive real-world example: We could think of sports betting or daily fantasy soccer predictions as a knapsack problem, where we want to construct a squad of players with the highest possible points to salary ratio.

# ### 0-1 Knapsack

# Let's us take a look the probably simplest variation of the knapsack problem, the 0-1 knapsack, and tackle it using a "greedy" strategy. In the 0-1 knapsack, we have a given set of items, $i_1, i_2, ..., i_m$, that we can use to fill the knapsack. Again, the knapsack has a fixed capacity, and the items are associated with weights, $w_1, w_2, ..., w_m$, and values $v_1, v_2, ..., v_m$. While our goal is still to pack the knapsack with a combination of items so that it carries the highest possible value, the 0-1 knapsack variation comes with the constraint that we can only carry 1 copy of each item. Thus, the runtime complexity of this algorithm is $O(nW)$, where $n$ is the number of items in the list and $W$ is the maximum capacity of the knapsack.
# 
# For example, if we are given 3 items with weights $[w_1: 20, w_2: 50, w_3: 30]$ and values
# $[v_1: 60, v_2: 100, v_3: 120]$, a knapsack with capacity 50 may carry to 1 copy of item 1 and 1 copy of item 3 to maximize its value (180) in contrast to just carrying 1 copy of item 2 (value: 100).

# Let's see how one "greedy" code implementation may look like:

# In[8]:


def knapsack_01(capacity, weights, values):
    val_by_weight = [value / weight 
                     for value, weight in zip(values, weights)]
    sort_idx = [i[0] for i in sorted(enumerate(val_by_weight), 
                                     key=lambda x:x[1], 
                                     reverse=True)]
    knapsack = [0 for _ in values]
    total_weight, total_value = 0, 0

    for i in sort_idx:
        if total_weight + weights[i] <= capacity:
            knapsack[i] = 1
            total_weight += weights[i]
            total_value += values[i]
        if total_weight == capacity:
            break

    return knapsack, total_weight, total_value


# We start by creating an array `val_by_weight`, which contains the value/weight values of the items. Next, we create an array of index positions by sorting the value/weight array; here, we can think of the item with the highest value/weight ratio as the item that gives us the "best bang for the buck." Using a for-loop, we then iterate over the `sort_idx` and check if a given items fits in our knapsack or not, that is, if we can carry it without exceeding the knapsack's capacity. After we checked all items, or if reach the capacity limit prematurely, we exit the for-loop and return the contents of the knapsack as well as its current weight and total value, which we've been tracking all along. 
# 
# A concrete example:

# In[9]:


weights = [20, 50, 30]
values = [60, 100, 120] 
knapsack_01(capacity=50, weights=weights, values=values)


# Running the `knapsack_01` function on the example input above returns a knapsack containing item 1 and item 3, with a total weight equal to its maximum capacity and a value of 180.

# Let us take a look at another example:

# In[10]:


weights = [40, 30, 20]
values = [70, 40, 35] 

knapsack_01(capacity=50, weights=weights, values=values)


# Notice the problem here? Our greedy algorithm suggests packing item 1 with weight 40 and a value of 70. Now, our knapsack can't pack any of the other items (weights 20 and 30), without exceeding its capacity. This is an example of where a greedy strategy leads to a globally suboptimal solution. An optimal solution would be to take 1 copy of item 2 and 1 copy of item 3, so that our knapsack carries a weight of 50 with a value of 75.

# ### Fractional Knapsack

# Now, let's implement a slightly different flavor of the knapsack problem, the fractional knapsack, which is guaranteed to find the optimal solution. Here, the rules are slightly different from the 0-1 knapsack that we implemented earlier. Instead of either just *including* or *excluding* an item in the knapsack, we can also add fractions $f$ of an item, subject to the constraint $0 \geq f \leq 1$.

# Now, let's take our 0-1 knapsack implementation as a template and make some slight modifications to come up with a fractional knapsack algorithm:

# In[11]:


def knapsack_fract(capacity, weights, values):
    val_by_weight = [value / weight 
                     for value, weight in zip(values, weights)]
    sort_idx = [i[0] for i in sorted(enumerate(val_by_weight), 
                                     key=lambda x:x[1], 
                                     reverse=True)]
    knapsack = [0 for _ in values]
    total_weight, total_value = 0, 0

    for i in sort_idx:
        if total_weight + weights[i] <= capacity:
            knapsack[i] = 1
            total_weight += weights[i]
            total_value += values[i]
        else:
            allowed = capacity - total_weight
            frac = allowed / weights[i]
            knapsack[i] = round(frac, 4)
            total_weight += allowed
            total_value += frac * values[i]           
        if total_weight == capacity:
            break

    return knapsack, total_weight, round(total_value, 4)


# Let's give it a whirl on a simple example first:

# In[13]:


weights = [20, 50, 30]
values = [60, 100, 120] 
knapsack_fract(capacity=50, weights=weights, values=values)


# The solution is an optimal solution, and we notice that it is the same as the one we got by using the 0-1 knapsack previously.

# To demonstrate the difference between the 0-1 knapsack and the fractional knapsack, let's do a second example:

# In[182]:


weights = [30]
values = [500] 

knappsack_fract(capacity=10, weights=weights, values=values)


# ## Example 3: Point-Cover-Interval Problem

# The classic Point-Cover-Interval problem is another example that is well suited for demonstrating greedy algorithms. Here, we are given a set of Intervals *L*, and we want to find the minimum set of points so that each interval is covered at least once by a given point as illustrated in the example below:
# 
# ![](./images/point-cover-interval-ex.png)

# Our greedy strategy, which finds the optimal solution for this problem, can be as follows:
# 
# - sort intervals in increasing order by the value of their endpoints
# - for interval in interval-set:
#     - if interval is not yet covered:
#         - add interval-endpoint to the set of points

# In[2]:


def min_points(intervals):
    s_ints = sorted(intervals, key=lambda x: x[1])

    points = [s_ints[0][-1]]

    for interv in s_ints:
        if not(points[-1] >= interv[0] and points[-1] <= interv[-1]):
            points.append(interv[-1])
        
    return points


# In[4]:


pts = [[2, 5], [1, 3], [3, 6]] 
min_points(pts)


# In[5]:


pts = [[4, 7], [1, 3], [2, 5], [5, 6]]
min_points(pts)


# # References
# - https://nbviewer.org/github/rasbt/algorithms_in_ipython_notebooks/blob/master/ipython_nbs/essentials/greedy-algorithm-intro.ipynb

# In[ ]:




