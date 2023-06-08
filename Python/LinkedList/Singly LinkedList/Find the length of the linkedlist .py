class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head):
        #code here
        if head == None:
            return 0
        count = 0
        temp = head
        while temp!=None:
            temp = temp.next
            count+=1
        return count