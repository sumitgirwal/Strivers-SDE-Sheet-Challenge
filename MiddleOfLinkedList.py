class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        return self.head

    def insertAtHead(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode 
            return
        temp = self.head
        newNode = Node(data)
        newNode.next = temp
        self.head = newNode 

    def print(self):
        temp = self.head 
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

    # reverse linedlist
    def reverse(self):
        temp = self.head 
        if temp==None or temp.next==None:
            return

        curr = self.head
        prev = None  

        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr 
            curr = temp 
        
        self.head = prev 
    
    # findMiddle linedlist
    def findMiddle(self):
        temp = self.head 
        if temp==None:
            return

        slow = fast = self.head
        while(fast!=None and fast.next!=None):
            slow  = slow.next 
            fast = fast.next.next 

        temp = slow
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 




ll = LinkedList()    
ll.insertAtHead(1)
ll.insertAtHead(2)
ll.insertAtHead(3)
ll.insertAtHead(4)
ll.insertAtHead(5)
ll.insertAtHead(6)
ll.print()
ll.reverse()
ll.print()
ll.findMiddle()
ll.print()



'''
/*
Following is the class structure of the Node class:

class Node
{
public:
    int data;
    Node *next;
    Node()
    {
        this->data = 0;
        next = NULL;
    }
    Node(int data)
    {
        this->data = data; 
        this->next = NULL;
    }
    Node(int data, Node* next)
    {
        this->data = data;
        this->next = next;
    }
};
*/

Node *findMiddle(Node *head) {
    // Write your code here
    if (head==NULL) 
        return head;
    
    Node* slow = head;
    Node* fast = head;
    while(fast!=NULL && fast->next!=NULL){
        slow = slow->next;
        fast = fast->next->next;

    }
    head = slow; 
    return head;
}

'''