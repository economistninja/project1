import itertools

def print_combinations_and_permutations():
    # Define input elements
    elements = ['a', 'b', 'c']

    # Get all permutations of the list
    permutations = list(itertools.permutations(elements))
    print("\nPermutations of elements:")
    for perm in permutations:
        print(f"  {perm}")

    # Get all combinations of 2 elements
    combinations = list(itertools.combinations(elements, 2))
    print("\nCombinations of 2 elements:")
    for combo in combinations:
        print(f"  {combo}")

if __name__ == "__main__":
    print_combinations_and_permutations() 
#-------------
# 2. Graphs
#--------------
from collections import deque

def create_graph():
    """Create a sample graph using adjacency list."""
    return {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

def dfs(graph, start, visited=None):
    """Depth-First Search traversal of graph."""
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def bfs(graph, start):
    """Breadth-First Search traversal of graph."""
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            queue.extend([n for n in graph[vertex] if n not in visited])
    print()

def main():
    """Execute graph traversals."""
    graph = create_graph()
    
    print("\nDFS Traversal starting from A:")
    dfs(graph, 'A')
    print("\n")
    
    print("BFS Traversal starting from A:")
    bfs(graph, 'A')

if __name__ == "__main__":
    main()