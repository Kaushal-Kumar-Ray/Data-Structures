from collections import deque

# Graph Representation using an Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BFS Traversal:", end=' ')
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Depth-First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# Run the traversals
if __name__ == "__main__":
    bfs(graph, 'A')
    print("\nDFS Traversal:", end=' ')
    dfs(graph, 'A')
