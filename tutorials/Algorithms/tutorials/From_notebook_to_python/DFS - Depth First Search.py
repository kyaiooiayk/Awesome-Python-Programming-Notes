#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Data-structures" data-toc-modified-id="Data-structures-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Data structures</a></span></li><li><span><a href="#Graph" data-toc-modified-id="Graph-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Graph</a></span></li><li><span><a href="#DFS-for-graphs-vs.-DFS-for-trees" data-toc-modified-id="DFS-for-graphs-vs.-DFS-for-trees-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>DFS for graphs vs. DFS for trees</a></span></li><li><span><a href="#DFS---Depth-First-Search-algorithm" data-toc-modified-id="DFS---Depth-First-Search-algorithm-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>DFS - Depth First Search algorithm</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** DFS - Depth First Search
# 
# </font>
# </div>

# # Data structures
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - A data structure is a storage that is used to store and organize data. It is a way of arranging data on a computer so that it can be accessed and updated efficiently.
# - A data structure is not only used for organizing the data. It is also used for processing, retrieving, and storing data.
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# # Graph
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - A Graph is a non-linear data structure consisting of vertices and edges.
# - The vertices are sometimes also referred to as nodes and the edges are lines or arcs that connect any two nodes in the graph. More formally a Graph is composed of a set of vertices( V ) and a set of edges( E ).
# - The graph is denoted by G(E, V).
# - Graphs are used to solve many real-life problems. Graphs are used to represent networks. The networks may include paths in a city or telephone network or circuit network.
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# # DFS for graphs vs. DFS for trees
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree. 
# - The only catch here is, that, unlike trees, graphs may contain cycles (a node may be visited twice). 
# 
# </font>
# </div>

# # DFS - Depth First Search algorithm
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - Depth-first search is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking. 
# 
# - So the basic idea is to start from the root or any arbitrary node and mark the node and move to the adjacent unmarked node and continue this loop until there is no unmarked adjacent node. Then backtrack and check for other unmarked nodes and traverse them. Finally, print the nodes in the path.
# 
# </font>
# </div>

# ![image.png](attachment:image.png)

# 
# - Input: n = 4, e = 6 
# - Graph: 2 -> 0, 0 -> 2, 1 -> 2, 0 -> 1, 3 -> 3, 1 -> 3 
# - Output: DFS from vertex 2 : 2 0 1 3  

# In[19]:


from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        print("Following is DFS from (starting from vertex:", v)
        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)


# In[22]:


# Construct the graph
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


# In[24]:


# Print connectivity
g.graph


# In[21]:


# Get the deepest connected path starting from  node 2
g.DFS(2)


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [Data structures](https://www.geeksforgeeks.org/data-structures/?ref=shm)
# - [Graph data structure](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/?ref=ghm)
# - [Depth First Search or DFS for a Graph](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)
# 
# </font>
# </div>

# In[ ]:




