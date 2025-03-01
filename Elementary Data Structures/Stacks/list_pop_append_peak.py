stack = []  # Stack using a list

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)  # Output: [10, 20, 30]

# Pop elements
print("Popped:", stack.pop())  # Output: 30
print("Popped:", stack.pop())  # Output: 20

# Peek (Check top element)
print("Top element:", stack[-1])  # Output: 10

# Pop elements
print("Popped:", stack.pop())




# Try to peek on empty stack
if stack:
    print("Top element:", stack[-1])
else:
    print("Stack is empty!")  # Output: Stack is empty!



'''
               +------------------+
        |      Start       |
        +------------------+
                 |
                 v
        +------------------+
        |  Create Empty    |
        |  Stack (List)    |
        +------------------+
                 |
                 v
     +---------------------+
     | Push 10            |
     +---------------------+
                 |
                 v
     +---------------------+
     | Push 20            |
     +---------------------+
                 |
                 v
     +---------------------+
     | Push 30            |
     +---------------------+
                 |
                 v
     +---------------------+
     | Print Stack        |
     | Stack: [10, 20, 30] |
     +---------------------+
                 |
                 v
     +---------------------+
     | Pop Element (30)   |
     | Print: Popped 30   |
     +---------------------+
                 |
                 v
     +---------------------+
     | Pop Element (20)   |
     | Print: Popped 20   |
     +---------------------+
                 |
                 v
     +---------------------+
     | Peek Top Element   |
     | Print: Top = 10    |
     +---------------------+
                 |
                 v
     +---------------------+
     | Pop Element (10)   |
     | Print: Popped 10   |
     +---------------------+
                 |
                 v
     +---------------------+
     | Peek Operation?     |
     | Is Stack Empty?     |
     +---------------------+
            /   \
          Yes   No
          |       |
  +---------------------+
  | Print: Stack Empty! |
  +---------------------+
          |
          v
  +------------------+
  |       End       |
  +------------------+

'''

