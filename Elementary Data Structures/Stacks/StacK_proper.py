class Stack:
    def __init__(self):
        self.values = []  

    def push(self, x):
        self.values.append(x)  # Add to the end

    def pop(self):
        if not self.values:
            return "Stack is empty!"
        return self.values.pop()  # Remove from the end (LIFO)

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(s.values)  # Output: [10, 20, 30, 40]

print(s.pop())   # Output: 40
print(s.values) 
print("Top element (by peek):",s.values[-1])# Output: [10, 20, 30]
