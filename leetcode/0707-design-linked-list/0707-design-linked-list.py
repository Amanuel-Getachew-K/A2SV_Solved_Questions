class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

        # eshi = self.head
        # while eshi:
        #     print(eshi.val)
        #     eshi = eshi.next
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.size += 1
        # eshi = self.head
        # while eshi:
        #     print(eshi.val)
        #     eshi = eshi.next
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size :
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        
        new_node = Node(val)
        curr = self.head
        i = 0
        while curr and i < index - 1:
            curr = curr.next
            i += 1
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1
        
        # eshi = self.head
        # while eshi:
        #     print(eshi.val)
        #     eshi = eshi.next
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size :
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
    
        curr = self.head
        i = 0
        while curr and i < index - 1:
            curr = curr.next
            i += 1

        curr.next = curr.next.next
        self.size -= 1
        # eshi = self.head
        # while eshi:
        #     print(eshi.val)
        #     eshi = eshi.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)