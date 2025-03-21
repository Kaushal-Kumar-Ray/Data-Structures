class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff  # Coefficient
        self.exp = exp      # Exponent
        self.next = None    # Pointer to next term

class Polynomial:
    def __init__(self):
        self.head = None  # Start with an empty polynomial

    def add_at_head(self, coeff, exp):
        new_node = Node(coeff, exp)
        if not self.head:  
            self.head = new_node  # First term
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node  # Append new term at the end

    def print_poly(self):
        temp = self.head
        while temp:
            print(f"{temp.coeff}x^{temp.exp}", end=" → ")
            temp = temp.next
        print("None")
# Create a polynomial: 3x² + 5x + 2
poly = Polynomial()
poly.add_at_head(3, 2)
poly.add_at_head(5, 1)
poly.add_at_head(2, 0)

# Display the polynomial
print("Polynomial:")
poly.print_poly()
