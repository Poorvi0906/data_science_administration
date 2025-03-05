# Node class to represent a single element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class to manage the linked list operations
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to append a node at the end of the list
    def append_node(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_node

    # Method to search for a node with a particular value
    def search_node(self, data):
        current = self.head
        while current:  # Traverse through the list
            if current.data == data:  # Check if the value matches
                return True  # Node found
            current = current.next
        return False  # Node not found

    # Method to display the elements of the list
    def display_list(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:  # Traverse through the list
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

# Example usage of the LinkedList class
if __name__ == "__main__":
    ll = LinkedList()

    # Append nodes to the linked list
    ll.append_node(10)
    ll.append_node(20)
    ll.append_node(30)

    # Display the linked list
    print("Linked List:")
    ll.display_list()

    # Search for nodes in the linked list
    print("\nSearch for 20:", "Found" if ll.search_node(20) else "Not Found")
    print("Search for 40:", "Found" if ll.search_node(40) else "Not Found")
