class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.next = None  # Pointer to the next non-zero element

class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.head = None  # Start with an empty linked list

    def insert(self, row, col, value):
        if value == 0:
            return  # Ignore zero values

        new_node = Node(row, col, value)
        if not self.head:
            self.head = new_node  # First element
        else:
            temp = self.head
            while temp.next:
                temp = temp.next  # Go to the last node
            temp.next = new_node  # Append new node

    def display_sparse(self):
        temp = self.head
        print("Sparse Matrix Representation (row, col, value):")
        while temp:
            print(f"({temp.row}, {temp.col}, {temp.value})")
            temp = temp.next

    def to_dense(self):
        matrix = [[0] * self.cols for _ in range(self.rows)]  # Initialize with zeros
        temp = self.head
        while temp:
            matrix[temp.row][temp.col] = temp.value  # Set non-zero values
            temp = temp.next
        return matrix

    def display_dense(self):
        dense_matrix = self.to_dense()
        print("\nOriginal (Dense) Matrix Representation:")
        for row in dense_matrix:
            print(row)

# Example Usage
rows, cols = 4, 4
sparse_matrix = SparseMatrix(rows, cols)

# Insert non-zero values
sparse_matrix.insert(0, 1, 5)
sparse_matrix.insert(1, 2, 8)
sparse_matrix.insert(2, 3, 3)
sparse_matrix.insert(3, 0, 6)

# Display Sparse and Dense Matrices
sparse_matrix.display_sparse()
sparse_matrix.display_dense()
