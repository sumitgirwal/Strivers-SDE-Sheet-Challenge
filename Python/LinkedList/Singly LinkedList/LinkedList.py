class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:

    def __init__(self):
        self.head = None 

    def print(self):
        temp = self.head 
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
        print()

    # insert at start position
    def insertAtStart(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode 
            return 

        temp = self.head 
        newNode.next = temp 
        self.head = newNode

    # insert at end position
    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode 
            return 

        temp = self.head 
        while temp.next:
            temp = temp.next 
        
        temp.next = newNode 

    # reverse 
    def reverse(self):
        if self.head == None:
            return 
        
        curr = self.head 
        prev = temp = None 

        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp

        self.head = prev 

    # middle of ll
    def middle(self):
        if self.head == None:
            return None
        
        slow = self.head 
        fast = self.head.next 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next != None:
                fast = fast.next
        
        return slow.data

               




if __name__=='__main__':
    ll = LinkedList()
    ll.insertAtStart(1)
    ll.insertAtStart(2)
    ll.insertAtStart(3)
    ll.insertAtStart(4)
    ll.insertAtStart(5)
    ll.insertAtStart(6)
    ll.insertAtStart(7)
    ll.reverse()
    ll.print()
    print(f"Middle element of LL: {ll.middle()}")