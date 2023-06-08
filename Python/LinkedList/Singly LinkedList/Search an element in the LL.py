class Solution:
    def searchKey(self, n, head, target):
        #Code here
        temp = head
        while temp:
            if temp.data == target:
                return 1
            temp = temp.next
        
        return 0