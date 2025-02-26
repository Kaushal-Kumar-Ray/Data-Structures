def sum_of_digits(n):
    if n == 0:
        return 0  # Base case: If number is 0, sum is 0
    return (n % 10) + sum_of_digits(n // 10)  # Add last digit + recursive call on remaining number

# Take input from the user
num = int(input("Enter a number: "))

# Print the sum of digits
print(f"Sum of digits of {num} is {sum_of_digits(num)}")
