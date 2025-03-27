filename="test2.txt"
with open(filename, "r") as file:
        lines = file.readlines()
def has_arborescence(n, edges):
    
    adj = [[] for _ in range(n)]
    in_degree = [0] * n
    
    for a, b in edges:
        adj[a].append(b)
        in_degree[b] += 1
    
    roots = [i for i in range(n) if in_degree[i] == 0]
    if len(roots) != 1:
        return "no"

    root = roots[0]

    queue = [root]
    visited = set(queue)
    while queue:
        node = queue.pop(0)  
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    
    return "yes" if len(visited) == n else "no"



n,m= map(int, lines[0].split())
edges = [list(map(int, line.split())) for line in lines[1:]]


print(has_arborescence(n, edges))
