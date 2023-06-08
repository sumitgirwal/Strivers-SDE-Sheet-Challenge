class Solution:
    def deleteNode(self,head, x):
        # Code here
        temp = head
        if x == 1:
            head.next.prev = None
            temp = temp.next
            return temp
        x = x-1
        while x:
            x-=1
            temp = temp.next
        
        if temp == None:
            return
        if temp.prev!=None:
            temp.prev.next = temp.next
        if temp.next!=None:
            temp.next.prev = temp.prev
        return head