#!/usr/bin/env python
# coding: utf-8

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Dijkstra’s algorithm for finding minimum distance path
#
# </font>
# </div>

# # Constraints
# <hr style = "border:2px solid black" ></hr>

# - Complete the function `minimum_distance_approximation` to return a list of positions in which gives the minimum cost as defined in the function `distance_cost`.
# - Each path can only move 1 coordinate at a time and must visit all vertices in the graph.

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[2]:


import numpy as np
import networkx as nx
from typing import Tuple
import matplotlib.pyplot as plt
from matplotlib import colors


# # Graph
# <hr style = "border:2px solid black" ></hr>

# - The values at the diagonal are all zero, as this is the distance of each node wrt themself.
# - Consider the first row: the values after the first one coord(0,1) represent the length of the path to the next node equal to 71. This is the distance of the first node wrt the second one.
# - The matrix is a `10x10` matrix.

# In[3]:


graph = [
    [0, 71, 24, 86, 95, 99, 88, 36, 26, 4],
    [56, 0, 22, 66, 35, 54, 47, 67, 4, 47],
    [74, 27, 0, 59, 74, 15, 52, 92, 95, 48],
    [18, 97, 11, 0, 7, 92, 54, 39, 8, 31],
    [73, 92, 58, 64, 0, 5, 55, 15, 14, 94],
    [64, 90, 52, 8, 2, 0, 80, 68, 63, 91],
    [46, 68, 60, 38, 92, 55, 0, 43, 67, 7],
    [88, 62, 92, 10, 12, 87, 44, 0, 79, 25],
    [19, 95, 75, 63, 58, 51, 85, 67, 0, 26],
    [1, 54, 64, 28, 10, 13, 91, 93, 97, 0],
]


# In[49]:


matrix = np.array(graph)
M = matrix

G = nx.from_numpy_array(matrix)


# - If you run it multiple times the distribution will always be different!
# - This is expected as the matrix does not encode the (x,y) directly but only the distance and the connectivity.

# In[5]:


nx.draw(G, with_labels=True, font_weight="bold")


# In[6]:


nx.draw(G, with_labels=True, font_weight="bold")


# In[7]:


# How many nodes?
G.nodes


# In[8]:


# What is the degree, connectivity of each node?
G.degree


# In[9]:


# Edges
G.edges


# In[10]:


# Is directed? If False is unidirected
G.is_directed()


# In[11]:


G.is_multigraph()


# - We can also represent the graph with a coloured matrix.
# - In this case, the larger the number in the cell (representing the distance) the more red the cell becomes.

# In[12]:


fig, ax = plt.subplots(figsize=(8, 8))
ax.matshow(matrix, cmap=plt.cm.Reds, vmin=0, vmax=20)
for i in range(10):
    for j in range(10):
        c = matrix[j, i]
        ax.text(i, j, str(c), va="center", ha="center")


# # Distance cost and constraints
# <hr style = "border:2px solid black" ></hr>

# - The `distance_cost` function is nothing more a way to encode the constraints mentioned in the description:
#     - Start from the top left corner of the matrix.
#     - You can only move one coordinate at the time.
#     - You must visit all the nodes.

# In[13]:


def distance_cost(graph, path):
    # First tuple is (0,0)
    assert path[0] == starting

    """
    Compute the sum of each tuple in list
    Get the diffence for adjacent values: out[i] = a[i+1] - a[i] 
    Check the resulting np.array has all element = 1
    """
    assert np.all(np.diff([(x[0] + x[1]) for x in path]) == 1)

    """
    The set of the integers in the path must be equal to {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    This is a way to check you have visited all the nodes.
    """
    assert set(range(10)) == set([cord for p in path for cord in p])

    # Return the sum of the distance encoded in the each tuple
    return sum(graph[x[0]][x[1]] for x in path)


# # Example of paths that respect the distance cost function
# <hr style = "border:2px solid black" ></hr>

# - Just playing around with some human-made alternative paths to get a feeling of how the objective function works:
# - This helped me understand that the example provided was really one of the many possible paths available, but not necessarily the shortest one.

# In[14]:


# Example
example = [
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (2, 7),
    (2, 8),
    (2, 9),
]
distance_cost(graph, example)


# In[15]:


# Example
example = [
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (0, 5),
    (0, 6),
    (0, 7),
    (0, 8),
    (0, 9),
]
distance_cost(graph, example)


# In[16]:


# Example
example = [
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (0, 5),
    (0, 6),
    (0, 7),
    (0, 8),
    (0, 9),
]
distance_cost(graph, example)


# In[17]:


# Example
example = [
    (0, 0),
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (0, 5),
    (1, 5),
    (1, 6),
    (1, 7),
    (2, 7),
    (2, 8),
    (2, 9),
]
distance_cost(graph, example)


# In[18]:


# Example
example = [
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (2, 7),
    (2, 8),
    (2, 9),
]
distance_cost(graph, example)


# In[19]:


# Example
example = [
    (0, 0),
    (0, 1),
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (2, 7),
    (2, 8),
    (2, 9),
]
distance_cost(graph, example)


# # Startup code
# <hr style = "border:2px solid black" ></hr>

# - Please note that variable `minimum_path_positions` was before the place where I was asked to contribute my code; I assumed this was intended and the interviewers wanted me to start the path from there.
# - **I took the liberty to call the function differently, the result is anyway the same.**

# In[20]:


starting = (0, 0)


def minimum_distance_approximation(graph, starting):  # -> list[Tuple]:
    minimum_path_positions = [(0, 0)]

    # Your Code To Generate Minimum Cost Here
    # -------

    return minimum_path_positions


minimum_distance_approximation(graph, starting)


# # Helper functions
# <hr style = "border:2px solid black" ></hr>

# In[21]:


def plot_interactive(M, M1, M2, M3, M4, minpost):
    """Plot interactive.

    Just a way to visualise what the algoithm is doing.

    Parameters
    ----------
    M : matrix
         Matrix representing the original graph encoding
         distances btw nodes
    M1 : matrix
        Matrix of booleans values. True and False for
        visited and not visited respectively
    M2 : matrix
        Position of total length of minimum path's head
    M3 : matrix
        Current stencil of nodes wrt which the distance is
        calculated
    M4 : matrix
        Update the position (x,y) vs. stencil

    minpost : list of list
        Coordinates of the minimum path's head

    Returns
    -------
    None
    """

    # Initialise figure
    fig, ax = plt.subplots(2, 2, figsize=(12, 12))
    min_val, max_val = 0, 10

    # Plot original graph
    ax[0, 0].set_title("Original")
    ax[0, 0].matshow(M, cmap=plt.cm.Blues, vmin=0, vmax=20)
    for i in range(max_val):
        for j in range(max_val):
            ax[0, 0].text(i, j, str(M[j, i]), c="r", va="center", ha="center")

    # Plot visited cells
    ax[0, 1].set_title("Visited + plus yellow stencil cells")
    cmap = colors.ListedColormap(["white", "black"])
    ax[0, 1].matshow(M1, cmap=cmap)
    ax[0, 1].matshow(M3, cmap=colors.ListedColormap(["yellow"]))
    for i in range(10):
        for j in range(10):
            ax[0, 1].text(i, j, str(M1[j, i]), c="r", va="center", ha="center")

    # Position of total length of minimum path's head
    ax[1, 0].set_title("Position and total length of minimum path's head")
    # ax[0, 1].matshow(M2, cmap=colors.ListedColormap(['white']))

    # Highlightin the minimum path head
    M2_ = np.ones((max_val, max_val), dtype=int) * -np.Infinity
    M2_[minpost[0], minpost[1]] = 100

    ax[1, 0].matshow(M2_, cmap=colors.ListedColormap(["black"]))

    for i in range(10):
        for j in range(10):
            ax[1, 0].text(i, j, str(M2[j, i]), c="r", va="center", ha="center")

    ax[1, 1].set_title("Update the position (x,y) vs. stencil")
    ax[1, 1].matshow(M4, cmap=colors.ListedColormap(["green"]))
    for i in range(10):
        for j in range(10):
            ax[1, 1].text(i, j, str(M4[j, i]), c="r", va="center", ha="center")

    fig.tight_layout()


# In[39]:


def get_path(M):
    """
    - In order to visualise the path, we are going to place a "1"
    in the path followed. This is to help us visualise the path
    followed. Essentially if you use a grey scale, this will be
    coloured in grey and the other will be coloured in white.
    """

    # Start backtracking to plot the path
    mattemp = M.astype(float)
    max_val = 10
    x, y = max_val - 1, max_val - 1
    path = []

    mattemp = np.zeros((max_val, max_val))
    mattemp[int(x), int(y)] = 1

    while x > 0.0 or y > 0.0:
        path.append([int(x), int(y)])
        xxyy = np.unravel_index(int(M[int(x), int(y)]), (max_val, max_val))
        x, y = xxyy[0], xxyy[1]
        mattemp[int(x), int(y)] = 1  # -np.inf

    # Add the last one as soon as you come out from the loop
    path.append([int(x), int(y)])

    return [(i[0], i[1]) for i in path[::-1]], mattemp


# In[47]:


def visualise_path(mattemp, M):
    fig, ax = plt.subplots(figsize=(8, 8))
    max_val = 10
    ax.matshow(mattemp, cmap="binary", vmin=0, vmax=20)
    for i in range(max_val):
        for j in range(max_val):
            c = M[j, i]
            ax.text(i, j, str(c), c="r", va="center", ha="center")


# # Dijkstra’s algorithm
# <hr style = "border:2px solid black" ></hr>

# In[41]:


starting = (0, 0)


def minimum_distance_approximation(
    graph, starting, plot=False, interactive=False, verbose=False
):
    minimum_path_positions = [(0, 0)]

    # Your Code To Generate Minimum Cost Here
    # -------

    # Renaming matrix and turn it into an numpy array
    M = np.array(graph)

    # Setting min and max values
    min_val, max_val = 0, 10

    # Initialise auxiliary arrays
    distmap = np.ones((max_val, max_val), dtype=int) * np.Infinity
    distmap[0, 0] = 0
    originmap = np.ones((max_val, max_val), dtype=int) * np.nan

    # Initialise cell we have visited
    visited = np.zeros((max_val, max_val), dtype=bool)

    # Where do we want to start? (0,0)
    x, y = int(0), int(0)

    count = 0
    finished = False

    # Loop until all nodes have been visited
    while not finished:
        # Instantiate it at each iteration
        stencil = np.ones((max_val, max_val), dtype=int) * np.nan

        if verbose:
            print("\n| Iteration:", count, "| current position (x,y): ", x, y)

        # Move to x+1,y
        if x < max_val - 1:
            # Move along on side of the stencil
            stencil[x + 1, y] = 1
            # Perform checks
            if (
                distmap[x + 1, y] > M[x + 1, y] + distmap[x, y]
                and not visited[x + 1, y]
            ):
                distmap[x + 1, y] = M[x + 1, y] + distmap[x, y]
                # Print only if the pass is actually done
                if verbose:
                    print("|-- Moving along x+1: ", x + 1, y)

                # How far into the array it is, if the index were flattened!
                originmap[x + 1, y] = np.ravel_multi_index([x, y], (max_val, max_val))
                # print(x,y, np.ravel_multi_index([x, y], (max_val, max_val)))

        # Move to x-1,y
        if x > 0:
            # Move along on side of the stencil
            stencil[x - 1, y] = 1
            # Perform checks
            if (
                distmap[x - 1, y] > M[x - 1, y] + distmap[x, y]
                and not visited[x - 1, y]
            ):
                distmap[x - 1, y] = M[x - 1, y] + distmap[x, y]
                # Print only if the pass is actually done
                if verbose:
                    print("|-- Moving along x-1: ", x - 1, y)
                originmap[x - 1, y] = np.ravel_multi_index([x, y], (max_val, max_val))
        # Move to x,y+1
        if y < max_val - 1:
            # Move along on side of the stencil
            stencil[x, y + 1] = 1
            # Perform checks
            if (
                distmap[x, y + 1] > M[x, y + 1] + distmap[x, y]
                and not visited[x, y + 1]
            ):
                distmap[x, y + 1] = M[x, y + 1] + distmap[x, y]
                # Print only if the pass is actually done
                if verbose:
                    print("|-- Moving along y+1: ", x, y + 1)
                originmap[x, y + 1] = np.ravel_multi_index([x, y], (max_val, max_val))

        # Move to x,y-1
        if y > 0:
            # Move along on side of the stencil
            stencil[x, y - 1] = 1
            # Perform checks
            if (
                distmap[x, y - 1] > M[x, y - 1] + distmap[x, y]
                and not visited[x, y - 1]
            ):
                distmap[x, y - 1] = M[x, y - 1] + distmap[x, y]
                # Print only if the pass is actually done
                if verbose:
                    print("|-- Moving along x-1: ", x, y - 1)
                originmap[x, y - 1] = np.ravel_multi_index([x, y], (max_val, max_val))

        # Marked the visited cell as True
        visited[x, y] = True
        dismaptemp = distmap
        dismaptemp[np.where(visited)] = np.Infinity

        # Find coords of the shortest path so far
        minpost = np.unravel_index(np.argmin(dismaptemp), np.shape(dismaptemp))

        # Update position, to where the minimum is and restart looping from there
        x, y = minpost[0], minpost[1]

        if verbose:
            print(
                "|-- Position of head of min path: (row, col)=",
                minpost,
                "| current sum=",
                str(np.min(dismaptemp)),
                " looking down!",
            )

        # End algorithm once you visited all nodes;
        if x == max_val - 1 and y == max_val - 1:
            finished = True
            if verbose:
                print("\n|- FINISHED!")

        # Update counter
        count = count + 1

        if plot:
            plot_interactive(M, visited, distmap, stencil, originmap, minpost)
            plt.show()

        if interactive:
            input("Press Enter to continue...")

    minimum_path_positions, mattemp = get_path(originmap)

    return minimum_path_positions, mattemp


# # Usage
# <hr style = "border:2px solid black" ></hr>

# ## Silent

# In[42]:


minimum_path_positions, mattemp = minimum_distance_approximation(
    graph, starting, plot=False, interactive=False, verbose=False
)


# In[43]:


minimum_path_positions


# ## Verbose

# In[44]:


minimum_path_positions, mattemp = minimum_distance_approximation(
    graph, starting, plot=False, interactive=False, verbose=True
)


# ## Interactive plot

# - Pat attentino as it takes more than 70 iterations!

# In[51]:


minimum_path_positions, mattemp = minimum_distance_approximation(
    graph, starting, plot=True, interactive=True, verbose=True
)


# # Verify that all constraints were satisfied
# <hr style = "border:2px solid black" ></hr>

# In[45]:


distance_cost(graph, minimum_path_positions)


# # Visualise the shortest path
# <hr style = "border:2px solid black" ></hr>

# - Those cell tagged as `-inf` will be coloured white on a binary whiet-black coloure scale.
# - Any other way  would have worked equally well here.

# In[50]:


visualise_path(mattemp, M)


# # References
# <hr style = "border:2px solid black" ></hr>

# - https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

# In[ ]:
