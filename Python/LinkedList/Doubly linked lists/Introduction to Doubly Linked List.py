class Solution:
    def __init__(self):
        self.head=None
        
    def constructDLL(self, arr):
         
        # Code here
        if len(arr)>=1:
            newNode = Node(arr[0])
            self.head = newNode
        temp = self.head
        for i in range(1, len(arr)):
            newNode = Node(arr[i])
            temp.next = newNode
            newNode.prev = temp
            temp=temp.next
        
        return self.head