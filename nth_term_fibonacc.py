def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0 
    elif n == 2:
        return 1 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
num = int(input("Enter the term number: "))
print(f"The {num}th Fibonacci number is {fibonacci(num)}")
