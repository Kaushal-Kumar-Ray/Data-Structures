def josephus_recursive(people, k, index=0):
    """Recursive function to solve Josephus problem and print eliminations."""
    if len(people) == 1:
        return people[0]  # Base case: last person remaining is the survivor

    # Calculate the next person to eliminate
    index = (index + k - 1) % len(people)
    eliminated = people.pop(index)  # Remove the person at index
    print(f"Eliminating: {eliminated}")  # Print elimination step

    return josephus_recursive(people, k, index)  # Recurse on remaining people

# **Example Execution**
n, k = 7, 3  # 7 people, every 3rd person eliminated
people = list(range(1, n + 1))  # Create list of people [1,2,3,4,5,6,7]

# Find the survivor
survivor = josephus_recursive(people, k)
print(f"The survivor is at position: {survivor}")
