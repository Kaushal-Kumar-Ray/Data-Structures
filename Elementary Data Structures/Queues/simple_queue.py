size =  5# Define fixed queue size
queue = [None] * size  # Create a list with fixed size
front = -1
rear = -1

# Enqueue operations
rear = rear+ 1
if front == -1:
    front = 0
queue[rear] = 10  # Enqueue 10

rear = rear+ 1
queue[rear] = 20  # Enqueue 20

rear = rear+ 1
queue[rear] = 30

# Display queue
print("Queue:", queue[front:rear + 1])

# Dequeue operation
if front > rear or front == -1:
    print("Queue Underflow! Cannot dequeue.")
else:
    print("Dequeued:", queue[front]) 
    front += 1    # dequeue operation
   

# Peek operation (Checking front element)
if front > rear or front == -1:
    print("Queue is empty!")
else:
    print("Front element after dequeue:", queue[front])

# Display queue after dequeue
print("Queue after dequeue:", queue[front:rear + 1])



'''
        +------------------+
        |      Start       |
        +------------------+
                 |
                 v
        +------------------+
        |  Define Queue    |
        |  Size = 5        |
        |  Front = -1      |
        |  Rear = -1       |
        +------------------+
                 |
                 v
     +----------------------+
     | Enqueue 10          |
     | Rear = 0, Front = 0 |
     +----------------------+
                 |
                 v
     +----------------------+
     | Enqueue 20          |
     | Rear = 1            |
     +----------------------+
                 |
                 v
     +----------------------+
     | Enqueue 30          |
     | Rear = 2            |
     +----------------------+
                 |
                 v
     +----------------------+
     | Print Queue         |
     | Output: [10, 20, 30]|
     +----------------------+
                 |
                 v
     +----------------------+
     | Dequeue Operation   |
     | Dequeued: 10        |
     | Front = 1           |
     +----------------------+
                 |
                 v
     +----------------------+
     | Peek Front Element  |
     | Output: 20          |
     +----------------------+
                 |
                 v
     +----------------------+
     | Print Queue Again   |
     | Output: [20, 30]    |
     +----------------------+
                 |
                 v
        +------------------+
        |       End        |
        +------------------+

'''