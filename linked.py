class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
def insert_at_front(head, new_data):
    
    new_node = Node(new_data)

    
    new_node.next = head

    
    return new_node

def print_list(head):
    curr = head
    while curr is not None:
        print(f" {curr.data}", end="")
        curr = curr.next
    print()


if __name__ == "__main__":
    # Create the linked list 2->3->4->5
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    # Print the original list
    print("Original Linked List:", end="")
    print_list(head)

    # Insert a new node at the front of the list
    print("After inserting Nodes at the front:", end="")
    data = 1
    head = insert_at_front(head, data)

    # Print the updated list
    print_list(head)
