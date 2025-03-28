def cut(graph, n):
    # Initialize two sets for v in S and v not in S
    S = set()
    T = set()

    for v in range (1, n + 1):
        # Count the neighbours of v in S and T
        count_S = sum(1 for neighbour in graph[v] if neighbour in S)
        count_T = sum(1 for neighbour in graph[v] if neighbour in T)

        # Place v in the set with fewer neighbours
        if count_S <= count_T:
            S.add(v)
        else:
            T.add(v)

    return S, T


def main():
    # Read number of vertices and number of edges
    n, m = map(int, input().split())

    # Initialize graph
    graph = [[] for _ in range(n + 1)]

    # Read m edges and add them to graph
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # Call cut to find sets S and T
    S, T = cut(graph, n)

    # Output the number of vertices in S
    print(len(S))
    # Output the vertices in S
    print(" ".join(map(str, S)))

if __name__ == "__main__":
    main()