
# Define a Node class to represent each non-zero element in the sparse matrix
class Node:
    def __init__(self, row, col, value):
        """
        Initializes a node with row index, column index, value, and a pointer to the next node.
        """
        self.row = row        # Row index of the non-zero element
        self.col = col        # Column index of the non-zero element
        self.value = value    # Value of the element
        self.next = None      # Pointer to the next non-zero element

# Define SparseMatrix class to store and manage the sparse matrix
class SparseMatrix:
    def __init__(self, rows, cols):
        """
        Initializes an empty sparse matrix with given dimensions.
        """
        self.rows = rows  # Total number of rows in the matrix
        self.cols = cols  # Total number of columns in the matrix
        self.head = None  # Head of the linked list storing non-zero elements

    def insert(self, row, col, value):
        """
        Inserts a non-zero element into the sparse matrix.
        If an element already exists at (row, col), it updates the value.
        """
        if value == 0:
            return  # No need to store zero values

        new_node = Node(row, col, value)  # Create a new node

        # If the linked list is empty, insert at the head
        if not self.head:
            self.head = new_node
            return

        # Traverse the list to find the correct position
        current = self.head
        prev = None

        while current:
            # If the same row and column already exists, update the value
            if current.row == row and current.col == col:
                current.value = value
                return

            # Find the correct position to insert (sorted order)
            if (current.row > row) or (current.row == row and current.col > col):
                break

            prev = current
            current = current.next

        # Insert new node at the correct position
        if prev is None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = prev.next
            prev.next = new_node

    def display(self):
        """
        Displays the sparse matrix in tuple format (row, col, value).
        """
        current = self.head  # Start from the head node
        if not current:      # If there are no non-zero elements
            print("Empty Matrix")
            return
        
        print("Sparse Matrix Representation (row, col, value):")
        while current:
            print(f"({current.row}, {current.col}, {current.value})")
            current = current.next

    def to_dense(self):
        """
        Converts the sparse matrix back to a 2D dense matrix format.
        """
        matrix = [[0] * self.cols for _ in range(self.rows)]  # Initialize with zeros

        current = self.head  # Start from the head node
        while current:
            matrix[current.row][current.col] = current.value  # Set non-zero values
            current = current.next

        return matrix  # Return the reconstructed matrix


# Create a 4x4 sparse matrix
sparse_matrix = SparseMatrix(4, 4)

# Insert non-zero values into the matrix
sparse_matrix.insert(0, 1, 5)   # Insert 5 at (0,1)
sparse_matrix.insert(1, 2, 8)   # Insert 8 at (1,2)
sparse_matrix.insert(2, 3, 3)   # Insert 3 at (2,3)
sparse_matrix.insert(3, 0, 6)   # Insert 6 at (3,0)

# Display the sparse matrix in linked list format
sparse_matrix.display()

# Convert to dense matrix and display
dense_matrix = sparse_matrix.to_dense()
print("\nDense Matrix Representation:")
for row in dense_matrix:
    print(row)



