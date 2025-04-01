l=[]
n = int(input("Enter total number of elements: "))
for i in range(n):
    l.append(int(input(f"Enter number {i + 1}: ")))
    
max =l[0]
min=l[0]
for i in range (n):
    if l[i]>max:
        max=l[i]
    if l[i]<min:
        min=l[i]
print(max,min)
# Initialize second max and second min
smax=-1000
smin=1000
for i in range(n):
    if l[i]>smax and l[i]!=max:
        smax=l[i]
    if l[i]<smin and l[i]!=min:
        smin=l[i]
print(smax,smin)