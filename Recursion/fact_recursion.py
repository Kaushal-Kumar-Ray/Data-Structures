def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

# Take input from the user
num = int(input("Enter a number: "))

# Calculate and print the factorial
print(f"Factorial of {num} is {factorial(num)}")
