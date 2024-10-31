class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def delete(self, key):
        temp = self.head

        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next

        if temp is None:
            return

        if temp.prev is not None:
            temp.prev.next = temp.next
        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp == self.head:
            self.head = temp.next

        temp = None

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# 使用示例
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.display()

    print("刪除節點 2")
    dll.delete(2)
    dll.display()

    print("查找節點 3:", dll.search(3))
    print("查找節點 4:", dll.search(4))