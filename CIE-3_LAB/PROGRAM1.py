class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def is_empty(self):
        return self.front_node is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear_node is None:
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front_node.data

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        removed_data = self.front_node.data
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.rear_node = None
        return removed_data

# Interactive menu
if __name__ == "__main__":
    q = Queue()
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. if Empty")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            val = input("Enter value to enqueue: ")
            q.enqueue(val)
            print(f"{val} enqueued.")
        elif choice == "2":
            try:
                print(f"Dequeued: {q.dequeue()}")
            except IndexError as e:
                print(e)
        elif choice == "3":
            try:
                print(f"Front: {q.front()}")
            except IndexError as e:
                print(e)
        elif choice == "4":
            print("Queue is empty." if q.is_empty() else "Queue is not empty.")
        elif choice == "5":
            print("Exiting from the queue. GOODBYE!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
