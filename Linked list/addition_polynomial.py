# Define a Node class to represent each term of the polynomial
class Node:
    def __init__(self, coefficient, exponent):
        """
        Initializes a node with a coefficient, exponent, and a pointer to the next node.
        """
        self.coefficient = coefficient  # Store the coefficient of the term
        self.exponent = exponent        # Store the exponent (power of x)
        self.next = None                # Pointer to the next node (default is None)

# Define the Polynomial class to manage a polynomial as a linked list
class Polynomial:
    def __init__(self):
        """
        Initializes an empty polynomial (linked list).
        """
        self.head = None  # Head points to the first node in the linked list

    def insert_term(self, coefficient, exponent):
        """
        Inserts a new term into the polynomial in decreasing order of exponent.
        If a term with the same exponent exists, it updates the coefficient.
        """
        if coefficient == 0:
            return  # Ignore zero coefficient terms

        new_node = Node(coefficient, exponent)  # Create a new node for the term

        # If the linked list is empty or the exponent is greater than the head node
        if not self.head or self.head.exponent < exponent:
            new_node.next = self.head  # Point new node to current head
            self.head = new_node       # Update head to new node
            return

        # Traverse the list to find the correct insertion point
        current = self.head
        while current.next and current.next.exponent > exponent:
            current = current.next

        # If the same exponent exists, update the coefficient
        if current.next and current.next.exponent == exponent:
            current.next.coefficient += coefficient
            # If coefficient becomes zero, remove the node
            if current.next.coefficient == 0:
                current.next = current.next.next
        else:
            # Insert new term at the correct position
            new_node.next = current.next
            current.next = new_node

    def display(self):
        """
        Displays the polynomial in a readable format.
        """
        current = self.head  # Start from the head node
        if not current:      # If the polynomial is empty
            print("0")
            return
        
        terms = []  # List to store terms as strings
        while current:
            terms.append(f"{current.coefficient}x^{current.exponent}")  # Format each term
            current = current.next  # Move to next node
        
        print(" + ".join(terms))  # Join and print terms

    @staticmethod
    def add(p1, p2):
        """
        Adds two polynomials and returns the resulting polynomial.
        """
        result = Polynomial()  # Create a new polynomial for storing the sum
        node1, node2 = p1.head, p2.head  # Start from the heads of both polynomials

        while node1 or node2:
            if node1 and (not node2 or node1.exponent > node2.exponent):
                # If node1 has a higher exponent, insert it into the result
                result.insert_term(node1.coefficient, node1.exponent)
                node1 = node1.next  # Move node1 to the next term
            elif node2 and (not node1 or node2.exponent > node1.exponent):
                # If node2 has a higher exponent, insert it into the result
                result.insert_term(node2.coefficient, node2.exponent)
                node2 = node2.next  # Move node2 to the next term
            else:
                # If both have the same exponent, add coefficients
                sum_coeff = node1.coefficient + node2.coefficient
                if sum_coeff != 0:
                    result.insert_term(sum_coeff, node1.exponent)
                node1 = node1.next  # Move both pointers forward
                node2 = node2.next

        return result  # Return the resulting polynomial

# Example Step-by-Step Execution

# Create first polynomial P1(x) = 3x^3 + 4x^2 + 5x + 6
p1 = Polynomial()
p1.insert_term(3, 3)  # Insert 3x^3
p1.insert_term(4, 2)  # Insert 4x^2
p1.insert_term(5, 1)  # Insert 5x^1
p1.insert_term(6, 0)  # Insert 6x^0

# Create second polynomial P2(x) = 5x^3 + 2x^2 + 7x + 8
p2 = Polynomial()
p2.insert_term(5, 3)  # Insert 5x^3
p2.insert_term(2, 2)  # Insert 2x^2
p2.insert_term(7, 1)  # Insert 7x^1
p2.insert_term(8, 0)  # Insert 8x^0

# Display both polynomials
print("P1(x):", end=" ")
p1.display()

print("P2(x):", end=" ")
p2.display()

# Add the two polynomials
result = Polynomial.add(p1, p2)

# Display the result
print("P1(x) + P2(x) =", end=" ")
result.display()
