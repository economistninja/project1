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
#-------------
# 3. Social networks
#--------------
from collections import deque

def create_social_network():
    """Create a sample social network using adjacency list."""
    return {
        'Alice': ['Bob', 'Charlie', 'David'],
        'Bob': ['Alice', 'Emma', 'Frank'],
        'Charlie': ['Alice', 'Grace'],
        'David': ['Alice', 'Henry'],
        'Emma': ['Bob', 'Ian'],
        'Frank': ['Bob', 'Jane'],
        'Grace': ['Charlie'],
        'Henry': ['David'],
        'Ian': ['Emma'],
        'Jane': ['Frank']
    }

def find_friends_at_distance(network, person, distance):
    """Find all friends at a specific connection distance using BFS."""
    visited = set()
    queue = deque([(person, 0)])
    friends_at_distance = []
    
    while queue:
        current_person, current_distance = queue.popleft()
        
        if current_person not in visited:
            visited.add(current_person)
            
            if current_distance == distance:
                friends_at_distance.append(current_person)
            elif current_distance < distance:
                for friend in network[current_person]:
                    if friend not in visited:
                        queue.append((friend, current_distance + 1))
    
    return friends_at_distance

def find_mutual_friends(network, person1, person2):
    """Find mutual friends between two people."""
    friends1 = set(network[person1])
    friends2 = set(network[person2])
    return friends1.intersection(friends2)

def main():
    network = create_social_network()
    
    # Find friends at distance 2 (friends of friends) for Alice
    print("\nFriends of friends for Alice:")
    second_degree = find_friends_at_distance(network, 'Alice', 2)
    print(f"  {second_degree}")
    
    # Find mutual friends between Bob and Alice
    print("\nMutual friends between Alice and Bob:")
    mutual = find_mutual_friends(network, 'Alice', 'Bob')
    print(f"  {mutual}")

if __name__ == "__main__":
    main()