l = []
n = int(input("Enter total number of elements: "))

if n < 2:
    print("List must have at least 2 elements to find second max and min.")
else:
    for i in range(n):
        l.append(int(input(f"Enter number {i + 1}: ")))

    # Initialize max and min
    max_val = min_val = l[0]

    # Find max and min
    for i in range(n):
        if l[i] > max_val:
            max_val = l[i]
        if l[i] < min_val:
            min_val = l[i]

    print(f"Max: {max_val}, Min: {min_val}")

    # Initialize second max and second min
    second_max = second_min = None

    for i in range(n):
        if l[i] != max_val:
            if second_max is None or l[i] > second_max:
                second_max = l[i]
        if l[i] != min_val:
            if second_min is None or l[i] < second_min:
                second_min = l[i]

    if second_max is None or second_min is None:
        print("Second max or second min not found (all elements might be the same).")
    else:
        print(f"Second Max: {second_max}, Second Min: {second_min}")