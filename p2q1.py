import sys
from collections import deque

# This determines whether there exists a r-arborescence of a digraph D.

if __name__ == '__main__':
    input = sys.stdin.read().strip().split('\n')
    n, m = map(int, input[0].strip().split()) 

    # Initialize the graph in adjacency list --> O(n+m)
    adj = [[] for _ in range(n)]
    in_degree = [0] * n
    
    for line in input[1:]:
        u, v = map(int, line.strip().split())
        adj[u].append(v)   # Add arc u → v to the adjacency list
        in_degree[v] += 1   # Compute in-degrees for each vertex

    # Find potential roots (nodes with in-degree 0)
    roots = [i for i in range(n) if in_degree[i] == 0]

    if len(roots) != 1:
        print('no')
    else:
        root = roots[0]
        visited = [False] * n
        count = 1   # count the nodes visited
        queue = deque([root])

        # use BFS to check if there exists r-arborescence
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    count += 1
                    queue.append(v)

        print('yes' if count == n else 'no')