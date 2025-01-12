class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head         # Link the new node to current head
            self.head = new_node  # Update the head to the new node

    def insert_at_end(self, data):
        new_node = Node(data)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node

    def insert_at_position(self, position, data):
        new_node = Node(data)

        itr = self.head
        for i in range(position - 1):
            itr = itr.next

        new_node.next = itr.next
        itr.next = new_node

    def delete_at_beginning(self):
        self.head = self.head.next

    def print_list(self):
        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next

    def delete_at_end(self):
        itr = self.head
        while itr.next.next:
            itr = itr.next

        itr.next = None

    def delete_at_position(self, position):
        itr = self.head
        for i in range(position - 1):
            itr = itr.next

        itr.next = itr.next.nextdrb


# 0,0,30,60,80
ll = LinkedList()
ll.insert_at_beginning(0)
ll.insert_at_beginning(0)
ll.insert_at_end(30)
ll.insert_at_beginning(2)
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.delete_at_beginning()  # delete
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.delete_at_position(1)
ll.insert_at_position(2, 65)
ll.delete_at_beginning()  # delete
ll.delete_at_end()  # delete
ll.delete_at_end()  # delete
ll.delete_at_position(1)
ll.insert_at_end(60)
ll.insert_at_end(80)
ll.print_list()