# this is based on 
# https://github.com/Bhanupriya-art/CSE408-Coursera-Answers/blob/main/Approximation%20Algorithms%20and%20Linear%20Programming/Week%203/Problem-Set-3.ipynb

import sys

def find_balanced_cut(n, adj_list): 
    # start with an initial cut that places first n/2 nodes in S1 and rest in S2.
    cut = [True if i < n/2 else False for i in range(n + 1)]
    cut[0] = False  # ignore index 0
    # Helper function to find imbalanced vertices
    def find_imbalanced_vertices(cut):
        imbalanced_vertices = []
        for i in range(1, n + 1):
            # Count the number of edges crossing the cut for vertex i
            num_edges_crossing_cut = sum(cut[i] != cut[j] for j in adj_list[i])
            # If the vertex is imbalanced, add it to the list
            if 2 * num_edges_crossing_cut < len(adj_list[i]):
                imbalanced_vertices.append(i)
        return imbalanced_vertices

    # Run the greedy algorithm
    while True:
        imbalanced_vertices = find_imbalanced_vertices(cut)
        # If there are no imbalanced vertices, we are done
        if not imbalanced_vertices:
            break
        # Otherwise, move the first imbalanced vertex to the other set
        cut[imbalanced_vertices[0]] = not cut[imbalanced_vertices[0]]

    return cut

if __name__ == '__main__':
    input = sys.stdin.read().strip().split('\n')
    n, m = map(int, input[0].strip().split())

    # Initialize the graph in adjacency list --> O(n+m)
    adj = [[] for _ in range(n + 1)]
    
    for line in input[1:]:
        u, v = map(int, line.strip().split())
        adj[u].append(v)   
        adj[v].append(u)
    
    S = find_balanced_cut(n, adj)
    result = [u for u in range(1, n + 1) if S[u]]
    print(len(result))
    print(' '.join(map(str, result)))