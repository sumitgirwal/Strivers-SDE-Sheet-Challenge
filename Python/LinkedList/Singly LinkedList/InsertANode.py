# https://practice.geeksforgeeks.org/problems/linked-list-insertion-1587115620/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=linked-list-insertion
class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        # code here 
        newNode = Node(x)
        if head == None:
            head = newNode
            return head
        
        temp = head
        newNode.next = temp
        head = newNode
        return head
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        newNode = Node(x)
        if head == None:
            head = newNode
            return head
        temp = head
        while temp.next!=None:
            temp = temp.next
        
        temp.next = newNode
        return head