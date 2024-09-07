class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        itr = self.head
        if self.head is None:
            print("Linked list is empty")
            return
        while itr is not None:
            print(itr.data)
            itr = itr.next

    def append(self, data):
        new_node = Node(data)
        # when linked list is empty
        if self.head is None:
            self.head = new_node
            return
        # when linked is not empty
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = new_node

    def insert_at_begin(self, data):
        new_node = Node(data)
        # when list is empty
        if self.head is None:
            self.head = new_node
            return
        # when there are node in the list
        new_node.next = self.head
        self.head = new_node

    def insert_node_before(self, data, value):
        new_node = Node(data)
        # when list is empty
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        # when insert node before head node
        if self.head.data == value:
            new_node.next = self.head
            self.head = new_node
            return
        itr = self.head
        while itr.next is not None:
            if itr.next.data == value:
                break
            itr = itr.next
        # # insert before the value
        if itr.next is not None:
            new_node.next = itr.next
            itr.next = new_node

    def insert_node_after(self, data, value):
        new_node = Node(data)
        # if list is empty
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return
        # when list is not empty
        itr = self.head
        while itr is not None:
            if itr.data == value:
                break
            itr = itr.next
        # insert node after the value
        if itr is not None:
            new_node.next = itr.next
            itr.next = new_node

    def delete_node_begin(self):
        # when list is empty
        if self.head is None:
            return
        # remove head, assign head to next node
        self.head = self.head.next

    def delete_last(self):
        # when list is empty
        if self.head is None:
            return
        # when only node in list
        if self.head.next is None:
            self.head = None
            return
        # remove the last node in the list
        itr = self.head
        while itr.next.next is not None:
            itr = itr.next
        itr.next = None

    def delete_node_value(self, value):
        # empty list
        if self.head is None:
            return
        # when delete head node
        if self.head.data == value:
            self.head = self.head.next
            return
        # when delete node in btw by value
        itr = self.head
        while itr.next is not None:
            if itr.next.data == value:
                break
            itr = itr.next
        # when found value
        if itr.next is not None:
            itr.next = itr.next.next

    def get_total(self):
        count = 0
        itr = self.head
        if self.head is None:
            return 0
        while itr is not None:
            count += 1
            itr = itr.next
        return count


if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_at_begin(2)
    ll.insert_at_begin(1)
    ll.append(3)

    ll.insert_node_before(4, 3)
    ll.insert_node_after(6, 4)

    ll.delete_node_begin()

    ll.delete_last()

    ll.delete_node_value(2)

    ll.print_list()
    total = ll.get_total()
    print(f'total node: {total}')