from multiprocessing.sharedctypes import Value
import copy


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        old_llist = copy.copy(self)
        self.head = new_node
        node = old_llist.head
        while node is not None:
            self.append(node.value)
            node = node.next

llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")

llist.prepend("New First Node")

print(llist.head.value)
print(llist.head.next.value)
print(llist.head.next.next.value)
print(llist.head.next.next.next.value)
