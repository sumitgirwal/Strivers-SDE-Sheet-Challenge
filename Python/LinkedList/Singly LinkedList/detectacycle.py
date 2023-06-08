'''
Following is the structure of the Node class already defined.

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
'''

def detectCycle(head) :
    # Write your code here.
    if head == None and head.next==None:
        return False 
    
    slow = fast = head  

    while(fast!=None and fast.next!=None):
        slow = slow.next
        fast = fast.next.next
        
         
        if(slow == fast):
            return True 
    return False