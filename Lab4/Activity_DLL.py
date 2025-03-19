class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_node(self, data):
        if not self.head:
            return
        current = self.head
        while current and current.data != data:
            current = current.next
        if not current:
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:
            self.head = current.next

    def traverse_backward(self):
        if not self.head:
            return
        last = self.head
        while last.next:
            last = last.next
        while last:
            print(last.data, end=" ")
            last = last.prev

# Example usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.delete_node(2)
dll.traverse_backward()  # Output: 3 1
