l = []
n = int(input("Enter total number of elements: "))
for i in range(n):
    l.append(int(input(f"Enter number {i + 1}: ")))
    
# Initialize max and min
max = l[0]
min = l[0]

# Find max and min
for i in range(n):
    if l[i] > max:
        max = l[i]
    if l[i] < min:  #
        min = l[i]
        
print(f"Max: {max}, Min: {min}")