class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size  # Single array for both stacks
        self.top1 = -1  # Stack 1 starts from left
        self.top2 = size  # Stack 2 starts from right

    def push1(self, value):
        """Push to Stack 1"""
        if self.top1 + 1 < self.top2:  # Check space
            self.top1 += 1
            self.arr[self.top1] = value
        else:
            print("Stack 1 is full!")

    def push2(self, value):
        """Push to Stack 2"""
        if self.top2 - 1 > self.top1:  # Check space
            self.top2 -= 1
            self.arr[self.top2] = value
        else:
            print("Stack 2 is full!")

    def pop1(self):
        """Pop from Stack 1"""
        if self.top1 >= 0:
            value = self.arr[self.top1]
            self.top1 -= 1
            return value
        else:
            return "Stack 1 is empty!"

    def pop2(self):
        """Pop from Stack 2"""
        if self.top2 < self.size:
            value = self.arr[self.top2]
            self.top2 += 1
            return value
        else:
            return "Stack 2 is empty!"

    def peek1(self):
        """Peek top of Stack 1"""
        return self.arr[self.top1] if self.top1 >= 0 else "Stack 1 is empty!"

    def peek2(self):
        """Peek top of Stack 2"""
        return self.arr[self.top2] if self.top2 < self.size else "Stack 2 is empty!"

    def print_stacks(self):
        """Print current state of the array"""
        print("Stack Array:", self.arr)
stacks = TwoStacks(10)  # Create an array of size 10

stacks.push1(5)
stacks.push1(10)
stacks.push1(15)

stacks.push2(100)
stacks.push2(200)
stacks.push2(300)

stacks.print_stacks()

print("Popped from Stack 1:", stacks.pop1())  # Output: 15
print("Popped from Stack 2:", stacks.pop2())  # Output: 300

print("Top of Stack 1:", stacks.peek1())  # Output: 10
print("Top of Stack 2:", stacks.peek2())  # Output: 200

stacks.print_stacks()
