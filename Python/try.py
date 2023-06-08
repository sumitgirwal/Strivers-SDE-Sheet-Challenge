class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  
  
class LinkedList:
  
    def __init__(self):
        self.head = None
  
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
  
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0
  
        # While both list exists
        while(first is not None or 
              second is not None):
  
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata
  
            # Update carry for next calculation
            carry = 1 if Sum >= 10 else 0
  
            # Update sum if it is greater than 10
            Sum = Sum if Sum < 10 else Sum % 10
  
            # Create a new node with sum as data
            temp = Node(Sum)
  
            # if this is the first node then set 
            # it as head of resultant list
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
  
            # Set prev for next insertion
            prev = temp
  
            # Move first and second pointers to 
            # next nodes
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
  
        if carry > 0:
            temp.next = Node(carry)
  
    # Utility function to print the 
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
        print()
  
# Driver code
first = LinkedList()

  
# Create first list
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
first.printList()
  
# Create second list
second = LinkedList()
second.push(4)
second.push(8)
second.printList()
  
# Add the two lists and see result
res = LinkedList()
res.addTwoLists(first.head, second.head)
res.printList()