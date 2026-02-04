Output 1
from collections import defaultdict, deque

  for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

def topological_sort(vertices, edges):
    # Step 1: Build graph and in-degree array
    graph = defaultdict(list)
    indegree = {v: 0 for v in vertices}

def topological_sort(vertices, edges):
    # Step 1: Build graph and in-degree array
    graph = defaultdict(list)
    indegree = {v: 0 for v in vertices}


    
    # Step 2: Queue all vertices with in-degree 0
    queue = deque([v for v in vertices if indegree[v] == 0])
    topo_order = []
for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1



    # Step 3: Process vertices
    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Cycle check
    if len(topo_order) != len(vertices):
        print("Graph contains a cycle. Topological sort not possible.")
        return None

    return topo_order


# -----------------------------
# Example DAG
# -----------------------------
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
    ('A', 'C'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'E'),
    ('D', 'F'),
    ('E', 'F')
]

# Run Topological Sort
result = topological_sort(vertices, edges)

if result:
    print("Topological Order:", result)
