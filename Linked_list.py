
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def add(self, value):
        self.size += 1
        if not self.head:
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
            self.head.next.prev = self.head

    def search(self, value):
        prob = self.head
        col = 0
        while prob:
            if prob.value == value:
                col += 1
            prob = prob.next
        return col

    def delete(self, value):
        self.size -= 1
        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = None

        prob = self.head
        while prob:
            if prob.value == value:
                prob.prev.next = prob.next
                prob.next.prev = prob.prev
                return True
            prob = prob.next

        return False