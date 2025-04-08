class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        print(f"Enqueued: {value}")

    def dequeue(self):
        if not self.queue:
            print("Queue Underflow! Cannot dequeue.")
            return
        removed = self.queue.pop(0)
        print(f"Dequeued: {removed}")

    def peek(self):
        if not self.queue:
            print("Queue is empty!")
            return
        print(f"Front element: {self.queue[0]}")

    def display(self):
        if not self.queue:
            print("Queue is empty!")
            return
        print("Queue:", self.queue)
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()   # Queue: [10, 20, 30]

q.dequeue()   # Dequeued: 10
q.peek()      # Front element: 20
q.display()   # Queue: [20, 30]
