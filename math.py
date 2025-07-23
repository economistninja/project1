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