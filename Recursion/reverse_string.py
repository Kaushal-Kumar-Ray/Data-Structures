def reverse_string(s):
    if len(s) == 0:  # Base Case: If the string is empty, return empty string
        return ""
    return s[-1] + reverse_string(s[:-1])  # Last character + Reverse of remaining string

# Example Usage
string = input("Enter a string: ")
print(f"Reversed string: {reverse_string(string)}")
